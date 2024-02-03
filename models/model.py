from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://site.db'
db = SQLAlchemy(app)

class Ropa(db.Model):
    id = db.Colum(db.integer, primary_key=True)
    name = db.Colum(db.string(20), unique=True, nullable=False)
    tipo = db.Colum(db.string(10), unique=True, nullable=False)
    descripcion = db.Colum(db.string(200), unique=True, nullable=False)