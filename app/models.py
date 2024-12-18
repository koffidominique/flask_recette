from app import db
from datetime import datetime


class Category(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable= False)
    recipes = db.relationship('Recipe',backref ='category', lazy=True)

    def __repr__(self):
        return f"Category('{self.name}')"
    

class Recipe (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable= False)
    description = db.Column(db.Text, nullable= False)
    prepa_time = db.Column(db.Integer, nullable = False)
    ingredients= db.Column(db.Text, nullable= False)
    instructions = db.Column(db.Text, nullable= False)
    create_at = db.Column(db.DateTime, default = datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category_id'), nullable = False)


    def __repr__(self):
        return f'<Recipe {self.title}>'