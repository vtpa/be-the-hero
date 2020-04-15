from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
import app

db = SQLAlchemy(app)

class Incident(db.Model):

  __tablename__ = 'case'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), nullable=False)
  description = db.Column(db.String(80), nullable=False)
  value = db.Column(db.Float)

  def get_all_incidents():
    return [Incident.json(incident) for incident in Incident.query.all()]