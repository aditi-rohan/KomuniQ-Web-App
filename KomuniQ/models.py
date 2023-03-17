# from this package import db
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


#database model for user and content
class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(8))
  password = db.Column(db.String(150))
  nombre = db.Column(db.String(150))
  apellido = db.Column(db.String(150))
  permiso = db.Column(db.String(1))
  #references notes in user
  mensajes = db.relationship('Note')


class Message(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone=True), default=func.now)
  #establishes many to one relationship with User class (there can be many notes to one user)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
