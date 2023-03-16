from flask import Flask
from views import views

from replit import db

db["key"] = "value"

app = Flask(__name__)

#register blueprint
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")
