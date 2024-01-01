from flask import Flask, jsonify, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import random
import secrets
'''
python -m pip install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

## Connect to Database
# Please bears in mind your path location in command prompt is very importance!!!!!
# You must set you path location into your same path as your project.
# Ex: 
# 
# C_
#   |
#   |___instance
#       |__cafes.db (2)
#   |project
#       |
#       |__main.py
#       |__instance
#           |__cafes.db (1)
# 
# if you command prompt current path is C:\project
# when you run: app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
# it will connect to cafes.db (1) in C:\project\instance
# but if you command prompt current path is C:
# when you run: app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
# it will connect to cafes.db (2) in C:\instance instead.

app = Flask(__name__)
os.chdir("C:\Gittest\python_learning_after_sec_21\pythonjourney\section28_create_api_with_flask")
app.secret_key = secrets.token_hex()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)

## Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

# Create all table that you have storged in db.Model to connected database.
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

# Get randomaly cafe from database.
@app.route("/random")
def get_random_cafe():
    # Get all cafes form database.
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()

    # Structering cafe data into jsonify's available form.
    randomaly_cafe = {} 
    randomaly_cafe["cafe"] = random.choice(all_cafes).__dict__
    randomaly_cafe["cafe"].pop("_sa_instance_state")

    return jsonify(randomaly_cafe)

# Get all cafes from database.
@app.route("/all")
def get_all_cafes():
    all_cafes_list = db.session.execute(db.select(Cafe)).scalars().all()
    all_cafes_dict = {"cafe":[]} 

    # Structuring every cafes data
    for cafe in all_cafes_list:
        appened_cafe = cafe.__dict__
        appened_cafe.pop("_sa_instance_state")

        all_cafes_dict["cafe"].append(appened_cafe)

    return jsonify(all_cafes_dict)

@app.route("/search")
def get_particular_loc_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    location = request.args.get("loc")
    particular_loc_cafes = {"cafe":[]} 

    if location == None:
        return jsonify({
            "error":"Parameters are required, please checking informations about http requests."
            })


    for cafe in all_cafes:
        if cafe.location == location:
            appended_cafe = cafe.__dict__
            appended_cafe.pop("_sa_instance_state")
            particular_loc_cafes["cafe"].append(appended_cafe)

    if len(particular_loc_cafes["cafe"]) == 0:
        return jsonify({
            "error":"Sorry, we don't have cafe in that locations"
            })

    return jsonify(particular_loc_cafes)

## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
