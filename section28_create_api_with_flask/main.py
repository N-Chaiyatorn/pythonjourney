from flask import Flask, jsonify, render_template, request
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sq
import random

'''
python -m pip install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''



app = Flask(__name__)

## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


response = db.Table(
    "response",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("map_url", db.String(500), nullable=False),
    db.Column("img_url", db.String(500), nullable=False)
)


# Cafe TABLE Configuration
class Cafes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()

cafes = Cafes()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def show_random_cafe():
    random_cafe = jsonify(random.choice(db.session.execute(db.select(Cafes)).scalars().all()))
    return random_cafe

# HTTP GET - Read Record
@app.route("/all")
def show_all_cafes():
    all_cafes = jsonify(db.session.execute(db.select(Cafes)).scalars().all())
    return all_cafes

@app.route("/search")
def show_particular_area_cafes():
    particular_area = request.args.get("loc")

    if particular_area == None:
        raise ValueError("Parameters 'loc' are required.")
        
    else:
        return particular_area


# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
    
