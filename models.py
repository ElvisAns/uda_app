from database_setup import db


class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    espece = db.Column(db.String(20))
    age = db.Column(db.Integer)
    couleur = db.Column(db.String(15))

