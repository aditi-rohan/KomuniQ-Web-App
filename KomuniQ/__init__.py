from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
  #initialize flask
  app = Flask(__name__)
  #encrypt/secure cookies and session data with secret key
  app.config['SECRET_KEY'] = '%#Hd6B2mR%n7R!m$6Mc4x?5@3iAY9y'
  #SQLAlchemy database is stored at f'sqlite:///{DB_NAME}' and thus will be stored inside the KomuniQ folder
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  #initialize database
  db.init_app(app)

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')

  from .models import User, Note

  with app.app_context():
    db.create_all()

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))

  return app


def create_database(app):
  if not path.exists('KomuniQ/' + DB_NAME):
    db.create_all(app=app)
    print('Created Database!')
