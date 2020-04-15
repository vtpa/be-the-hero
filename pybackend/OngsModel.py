from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from app import app

db = SQLAlchemy(app)

class Ongs(db.Model):

  __tablename__ = 'ongs'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(80), nullable=False)
  whatsapp = db.Column(db.String(80), nullable=False)
  city = db.Column(db.String(80), nullable=False)
  uf = db.Column(db.String(2), nullable=False)

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'email': self.email,
      'whatsapp': self.whatsapp,
      'city': self.city,
      'uf': self.city
    }

  def add_ong(_name, _email, _whatsapp, _city, _uf):
    new_ong = Ongs(name=_name, email=_email, whatsapp=_whatsapp, city=_city, uf=_uf)
    db.session.add(new_ong)
    db.session.commit()
    return Ongs.json(new_ong)

  def get_all_ongs():
    return [Ongs.json(ong) for ong in Ongs.query.all()]    

  def delete_ong(_id):
    try:
      Ongs.query.filter_by(id=_id).delete()
      db.session.commit()
      return True
    except:
      return False

  def __repr__(self):
    ong_object = {
      'id': self.id,
      'name': self.name,
      'email': self.email,
      'whatsapp': self.whatsapp,
      'city': self.city,
      'uf': self.city
    }
    return json.dumps(ong_object)