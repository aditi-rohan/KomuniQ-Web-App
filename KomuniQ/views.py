from flask import Blueprint, render_template, request, jsonify, flash
from flask_login import login_required, current_user
from .models import Message
from . import db
import json

#initialize blueprint
views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
@login_required
def dashboard():
  if request.method == 'POST':
    #gets message from html
    message = request.form.get('message')

    if len(message) < 1:
      flash('El mensaje esta vacio!', category='error')
    else:
      #provide schema for message
      new_message = Message(data=message, user_id=current_user.id)
      #add message to database
      db.session.add(new_message)
      db.session.commit()
      flash('Mensaje fue enviado!', category='success')

  return render_template('dashboard.html')
  #TODO: change this function to be mensajes() and to render to mensajes.html


@views.route('/delete-mensaje', methods=['POST'])
def delete_mensaje():
  #function expects a JAOn from the INDEX.js file
  message = json.loads(request.data)
  messageId = message['messageId']
  message = Message.query.get(messageId)
  if message:
    if message.user_id == current_user.id:
      db.session.delete(message)
      db.session.commit()
  return jsonify({})