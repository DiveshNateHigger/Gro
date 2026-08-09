from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__, 
           template_folder='../templates',
           static_folder='../static')

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../data/plant_disease.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'plant_disease_detection_app_secret_key'

# Initialize database
db = SQLAlchemy(app)

# Import routes at the end to avoid circular imports
from app import routes 