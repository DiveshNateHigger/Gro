from app import db

class Disease(db.Model):
    """Model for plant disease information"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    possible_steps = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<Disease {self.name}>'

class Supplement(db.Model):
    """Model for supplement information related to plant diseases"""
    id = db.Column(db.Integer, primary_key=True)
    disease_id = db.Column(db.Integer, db.ForeignKey('disease.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    buy_link = db.Column(db.String(255), nullable=True)
    
    # Define relationship with Disease model
    disease = db.relationship('Disease', backref=db.backref('supplements', lazy=True))
    
    def __repr__(self):
        return f'<Supplement {self.name}>'

class Scheme(db.Model):
    """Model for government agricultural schemes"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'Government', 'Financial'
    ministry = db.Column(db.String(100), nullable=True)
    website_url = db.Column(db.String(255), nullable=True)
    eligibility = db.Column(db.Text, nullable=True)
    benefits = db.Column(db.Text, nullable=True)
    last_updated = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f'<Scheme {self.name}>' 