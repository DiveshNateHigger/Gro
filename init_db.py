from app import app, db
from app.data_fetcher import create_sample_schemes
from app.models import Scheme

def init_db():
    print("Initializing database...")
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if schemes already exist
        if Scheme.query.count() == 0:
            print("Creating sample schemes...")
            create_sample_schemes()
            print("Sample schemes created successfully!")
        else:
            print(f"Schemes already exist in the database. Found {Scheme.query.count()} schemes.")
        
        # Print scheme counts by category
        government_schemes = Scheme.query.filter_by(category='Government').count()
        financial_schemes = Scheme.query.filter_by(category='Financial').count()
        print(f"Government Schemes: {government_schemes}")
        print(f"Financial Schemes: {financial_schemes}")
    
    print("Database initialization complete!")

if __name__ == "__main__":
    init_db() 