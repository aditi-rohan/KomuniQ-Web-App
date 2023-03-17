from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  #import db from __init__.py
from flask_login import login_user, login_required, logout_user, current_user

#initialize blueprint
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    #get the username and password from user
    username = request.form.get('username')
    password = request.form.get('password')

    #find the first database entry with a matching username
    user = User.query.filter_by(username=username).first()
    #if user exists/ is found in the database
    if user:
      #check if password entered matches the hashed password in the db
      if check_password_hash(user.password, password):
        #if passwords match print flash message
        flash('Has iniciado sesión!', category='success')
        login_user(user, remember=True)
        return redirect(url_for('views.dashboard'))
      #if password entered and password in database do NOT match...
      else:
        #...print flash message
        flash(
          'Usuario no es reconocido, el nombre de usuario o la contraseña esta incorrecta.',
          category='error')
    #if user does not exist (username NOT found in db)...
    else:
      #...print flash message
      flash('Esta cuenta no existe.', category='error')

    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))


@auth.route('/ajustes', methods=['GET', 'POST'])
def change_password():
  if request.method == 'POST':
    username = request.form.get('username')  #??necessary??
    password = request.form.get('password')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    #find the first database entry with a matching username
    user = User.query.filter_by(username=username).first()
    #if user exists/ is found in the database
    if user:
      #check if password entered matches the hashed password in the db
      if check_password_hash(user.password, password):
        #if passwords match print flash message
        flash('Has sido autenticado/a!', category='success')
        if len(password1) < 8:
          flash(
            'Contraseña es muy corta. La contraseña debe tener más de 8 caracteres, intente de nuevo.',
            category='error')
        elif password1 == password2:
          updated_password = User(
            password=generate_password_hash(password1, method='sha256'))
          db.session.add(updated_password)
          db.session.commit()
          flash('La contraseña ha sido cambiada!', category='success')
          return redirect(url_for('views.dashboard'))
        else:
          flash(
            'La contraseña no se pudo cambiar porque el campo de la nueva contraseña y el campo de confirmacion no coinciden.',
            category='error')
      #if password entered and password in database do NOT match...
      else:
        #...print flash message
        flash(
          'Usuario no es reconocido, el nombre de usuario o la contraseña esta incorrecta.',
          category='error')
    #if user does not exist (username NOT found in db)...
    else:
      #...print flash message
      flash('Esta cuenta no existe.', category='error')

  return render_template("ajustes.html", user=current_user)