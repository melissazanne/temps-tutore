from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Classe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(200), nullable=False)
    sessions = db.relationship('Session', backref='classe', lazy=True)

    def __init__(self, nom):
        self.nom = nom

        
class Manager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(200), nullable=False)
    prenom = db.Column(db.String(200), nullable=False)

    def __init__(self, prenon, nom):
        self.nom = nom
        self.prenom = prenom

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(200), nullable=False)
    fin = db.Column(db.DateTime)
    debut = db.Column(db.DateTime)
    classe_id = db.Column(db.Integer, db.ForeignKey('classe.id'), nullable=False)
    
    def __init__(self, nom, debut, fin ):
        self.nom =nom
        self.fin = fin
        self.debut = debut