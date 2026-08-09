import os
import pandas as pd
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from app import app, db
from app.models import Disease, Supplement, Scheme
from models.model_utils import load_model, predict_disease
from app.data_fetcher import create_sample_schemes, update_schemes_database

# Create uploads directory if it doesn't exist
os.makedirs('static/uploads', exist_ok=True)

# Load the model
MODEL_PATH = os.path.join(app.root_path, '../models/plant_disease_model_1.pt')
try:
    model = load_model(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None

# Load data from CSV files if database is empty
def initialize_data():
    if Disease.query.count() == 0:
        try:
            # Load disease information
            disease_df = pd.read_csv(os.path.join(app.root_path, '../data/disease_info.csv'), encoding='cp1252')
            supplement_df = pd.read_csv(os.path.join(app.root_path, '../data/supplement_info.csv'), encoding='cp1252')
            
            # Add diseases to the database
            for _, row in disease_df.iterrows():
                disease = Disease(
                    id=row['index'],
                    name=row['disease_name'],
                    description=row['description'],
                    possible_steps=row['Possible Steps'],
                    image_url=row['image_url']
                )
                db.session.add(disease)
            
            # Add supplements to the database
            for _, row in supplement_df.iterrows():
                # Skip empty rows
                if pd.isna(row['supplement name']):
                    continue
                    
                supplement = Supplement(
                    disease_id=row['index'],
                    name=row['supplement name'],
                    image_url=row['supplement image'],
                    buy_link=row['buy link']
                )
                db.session.add(supplement)
            
            db.session.commit()
            print("Database initialized with disease and supplement data")
        except Exception as e:
            db.session.rollback()
            print(f"Error initializing database: {str(e)}")
    
    # Initialize schemes data if empty
    if Scheme.query.count() == 0:
        try:
            # Try to update from real API/CSV first
            if not update_schemes_database():
                # Fall back to sample data if real data not available
                create_sample_schemes()
            print("Database initialized with schemes data")
        except Exception as e:
            print(f"Error initializing schemes data: {str(e)}")

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Disease prediction page
@app.route('/predict', methods=['GET'])
def predict_page():
    return render_template('predict.html')

# API endpoint for image upload and prediction
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['image']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    # Secure the filename to prevent any security issues
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.root_path, '../static/uploads', filename)
    
    # Save the file
    file.save(file_path)
    
    # Perform prediction
    try:
        if model is None:
            raise RuntimeError("Model not loaded")
        
        prediction_idx, _ = predict_disease(model, file_path)
        
        # Redirect to results page
        return redirect(url_for('prediction_result', prediction_id=prediction_idx, image=filename))
    except Exception as e:
        return render_template('error.html', error=str(e))

# Results page
@app.route('/result/<int:prediction_id>/<image>')
def prediction_result(prediction_id, image):
    # Get disease information from database
    disease = Disease.query.get_or_404(prediction_id)
    
    # Get supplement information for this disease
    supplement = Supplement.query.filter_by(disease_id=prediction_id).first()
    
    return render_template('result.html', 
                           disease=disease,
                           supplement=supplement,
                           image_file=image)

# Supplements page
@app.route('/supplements')
def supplements_page():
    supplements = Supplement.query.all()
    diseases = Disease.query.all()
    
    return render_template('supplements.html', 
                           supplements=supplements,
                           diseases=diseases)

# About page
@app.route('/about')
def about_page():
    return redirect(url_for('about_contact_page'))

# Contact page
@app.route('/contact')
def contact_page():
    return redirect(url_for('about_contact_page'))

# Combined About & Contact page
@app.route('/about-contact')
def about_contact_page():
    return render_template('about_contact.html')

# Schemes page
@app.route('/schemes')
def schemes_page():
    # Get schemes from database
    government_schemes = Scheme.query.filter_by(category='Government').all()
    financial_schemes = Scheme.query.filter_by(category='Financial').all()
    
    return render_template('schemes.html',
                          government_schemes=government_schemes,
                          financial_schemes=financial_schemes)

# Community page
@app.route('/community')
def community_page():
    return render_template('community.html')

# Schemes update - Admin function to refresh the schemes data
@app.route('/admin/update-schemes', methods=['GET', 'POST'])
def update_schemes():
    # Get current scheme counts
    government_schemes_count = Scheme.query.filter_by(category='Government').count()
    financial_schemes_count = Scheme.query.filter_by(category='Financial').count()
    
    if request.method == 'POST':
        success = update_schemes_database()
        if success:
            flash('Schemes database updated successfully!', 'success')
        else:
            flash('Failed to update schemes database.', 'danger')
    
    return render_template('admin/update_schemes.html',
                          government_schemes=government_schemes_count,
                          financial_schemes=financial_schemes_count)

# Serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(app.root_path, '../static/uploads'), filename)

# Initialize the database
with app.app_context():
    db.create_all()
    initialize_data() 