import os
import requests
import json
import pandas as pd
from datetime import datetime
from app import db
from app.models import Scheme

# URL for government data API
# Update this with the actual API endpoint when available
GOV_API_URL = "https://data.gov.in/api/datastore/resource.json"

# If using a CSV file instead of an API
SCHEMES_CSV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/scheme_info.csv')

def fetch_schemes_from_api(api_key=None):
    """
    Fetch scheme data from government API
    Returns a list of scheme dictionaries
    """
    try:
        # API parameters
        params = {
            'resource_id': 'your-resource-id',  # Replace with actual resource ID
            'api-key': api_key or os.environ.get('GOV_API_KEY')
        }
        
        response = requests.get(GOV_API_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        data = response.json()
        
        # Process the data and convert to our schema
        schemes = []
        for item in data.get('records', []):
            scheme = {
                'name': item.get('scheme_name', ''),
                'description': item.get('description', ''),
                'category': item.get('category', 'Government'),
                'ministry': item.get('ministry', ''),
                'website_url': item.get('website', ''),
                'eligibility': item.get('eligibility', ''),
                'benefits': item.get('benefits', ''),
                'last_updated': datetime.now()
            }
            schemes.append(scheme)
        
        return schemes
    
    except requests.RequestException as e:
        print(f"API Request Error: {e}")
        return []

def fetch_schemes_from_csv():
    """
    Load scheme data from a CSV file
    Returns a list of scheme dictionaries
    """
    try:
        if not os.path.exists(SCHEMES_CSV_PATH):
            print(f"CSV file not found: {SCHEMES_CSV_PATH}")
            return []
        
        df = pd.read_csv(SCHEMES_CSV_PATH, encoding='utf-8')
        
        schemes = []
        for _, row in df.iterrows():
            scheme = {
                'name': row.get('scheme_name', ''),
                'description': row.get('description', ''),
                'category': row.get('category', 'Government'),
                'ministry': row.get('ministry', ''),
                'website_url': row.get('website_url', ''),
                'eligibility': row.get('eligibility', ''),
                'benefits': row.get('benefits', ''),
                'last_updated': datetime.now()
            }
            schemes.append(scheme)
        
        return schemes
    
    except Exception as e:
        print(f"CSV Loading Error: {e}")
        return []

def update_schemes_database():
    """
    Update the database with the latest scheme information
    """
    try:
        # Try to fetch from API first
        schemes = fetch_schemes_from_api()
        
        # If API fails or returns no data, fall back to CSV
        if not schemes:
            schemes = fetch_schemes_from_csv()
        
        if not schemes:
            print("No scheme data available from API or CSV")
            return False
        
        # Clear existing schemes
        Scheme.query.delete()
        
        # Add new schemes
        for scheme_data in schemes:
            scheme = Scheme(**scheme_data)
            db.session.add(scheme)
        
        db.session.commit()
        print(f"Successfully updated {len(schemes)} schemes in the database")
        return True
    
    except Exception as e:
        db.session.rollback()
        print(f"Error updating schemes database: {e}")
        return False

# Function to create sample data for testing
def create_sample_schemes():
    """
    Create sample scheme data for development/testing
    """
    sample_schemes = [
        {
            'name': 'Pradhan Mantri Fasal Bima Yojana',
            'description': 'A crop insurance scheme that provides financial support to farmers in case of crop failure due to natural calamities.',
            'category': 'Government',
            'ministry': 'Ministry of Agriculture & Farmers Welfare',
            'website_url': 'https://pmfby.gov.in/',
            'eligibility': 'All farmers growing notified crops in notified areas.',
            'benefits': 'Insurance coverage and financial support to farmers in case of crop failure.',
            'last_updated': datetime.now()
        },
        {
            'name': 'Pradhan Mantri Krishi Sinchai Yojana',
            'description': 'Aims to provide improved access to irrigation for farmers across the country with the motto of "More crop per drop".',
            'category': 'Government',
            'ministry': 'Ministry of Agriculture & Farmers Welfare',
            'website_url': 'https://pmksy.gov.in/',
            'eligibility': 'All farmers with focus on small and marginal farmers.',
            'benefits': 'Improved access to irrigation, water use efficiency, precision irrigation.',
            'last_updated': datetime.now()
        },
        {
            'name': 'Soil Health Card Scheme',
            'description': 'Provides information to farmers on nutrient status of their soil along with recommendations on appropriate dosage of nutrients for improving soil health and fertility.',
            'category': 'Government',
            'ministry': 'Ministry of Agriculture & Farmers Welfare',
            'website_url': 'https://soilhealth.dac.gov.in/',
            'eligibility': 'All farmers.',
            'benefits': 'Soil testing and recommendations for improving soil health and fertility.',
            'last_updated': datetime.now()
        },
        {
            'name': 'Paramparagat Krishi Vikas Yojana',
            'description': 'Promotes organic farming practices and improves soil health through the use of organic inputs.',
            'category': 'Government',
            'ministry': 'Ministry of Agriculture & Farmers Welfare',
            'website_url': 'https://pgsindia-ncof.gov.in/pkvy/index.aspx',
            'eligibility': 'All farmers with special focus on farmers who want to adopt organic farming.',
            'benefits': 'Financial assistance, training, and certification for organic farming.',
            'last_updated': datetime.now()
        },
        {
            'name': 'Kisan Credit Card',
            'description': 'Provides farmers with affordable credit for their agricultural operations and other needs.',
            'category': 'Financial',
            'ministry': 'Ministry of Finance',
            'website_url': 'https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=4432&Mode=0',
            'eligibility': 'All farmers, tenant farmers, sharecroppers, and oral lessees.',
            'benefits': 'Easy and timely credit for agricultural operations, consumption needs, and allied activities.',
            'last_updated': datetime.now()
        },
        {
            'name': 'Agriculture Infrastructure Fund',
            'description': 'A financing facility for investment in post-harvest management infrastructure and community farming assets.',
            'category': 'Financial',
            'ministry': 'Ministry of Agriculture & Farmers Welfare',
            'website_url': 'https://agriinfra.dac.gov.in/',
            'eligibility': 'Farmers, FPOs, PACS, Marketing Cooperative Societies, SHGs, and more.',
            'benefits': 'Interest subvention and credit guarantee for loans up to ₹2 crore.',
            'last_updated': datetime.now()
        }
    ]
    
    try:
        # Clear existing schemes
        Scheme.query.delete()
        
        # Add sample schemes
        for scheme_data in sample_schemes:
            scheme = Scheme(**scheme_data)
            db.session.add(scheme)
        
        db.session.commit()
        print(f"Successfully added {len(sample_schemes)} sample schemes to the database")
        return True
    
    except Exception as e:
        db.session.rollback()
        print(f"Error creating sample schemes: {e}")
        return False 