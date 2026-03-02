# models.py
from .db import db

class Astillero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(50))
    año_fundacion = db.Column(db.Integer)
    veleros = db.relationship('Velero', backref='astillero', lazy=True)

class Disennador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    nacionalidad = db.Column(db.String(50))
    año_nacimiento = db.Column(db.Integer)
    veleros = db.relationship('Velero', backref='disennador', lazy=True)

class Velero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    eslora = db.Column(db.Float)
    manga = db.Column(db.Float)
    calado = db.Column(db.Float)
    año_fabricacion = db.Column(db.Integer)
    astillero_id = db.Column(db.Integer, db.ForeignKey('astillero.id'))
    disennador_id = db.Column(db.Integer, db.ForeignKey('disennador.id'))