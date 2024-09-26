from flask import Flask, jsonify, render_template, request
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

api_secret_key = {
    "topSecretKey":"Gojovssukuna23"
}




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
@app.route("/add-cafe/<int:cafe_id>", methods = ["POST"])
def add_new_cafe(cafe_id):
    # Get user's json parameters.
    json_params = request.get_json()
    json_params["id"] = cafe_id

    # Create new row that consist our json parameters with specific cafe id.
    new_cafe = Cafe(**json_params)

    # Add new row to database.
    db.session.add(new_cafe)
    db.session.commit()

    returned_text = """Successful add for\n\n"""

    for col_name in json_params:
        returned_text += f"{col_name}:{json_params[col_name]}\n"

    return returned_text

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods = ["PATCH"])
def update_new_price(cafe_id):
    # Get specific row from cafe_id input value.
    selected_cafe = db.get_or_404(Cafe, cafe_id)
    old_coffee_price = selected_cafe.coffee_price

    # Get json parameters.
    json_params = request.get_json()

    # Check if 'coffee_price' didn't exist in parameters, it will return error json message.
    if "coffee_price" not in json_params:
        return jsonify(
            {
                "error":"new 'coffee_price' are required."
            }
        )
    
    # Assign new price to determined row.
    selected_cafe.coffee_price = f"£{str(json_params['coffee_price'])}"
    db.session.commit()

    return f"Successful edit for {selected_cafe.id} {selected_cafe.name}.\nbefore:{old_coffee_price}$.\nAfter editing:{selected_cafe.coffee_price}."

@app.route("/update/<int:cafe_id>", methods = ["PATCH"])
def update_specific_column(cafe_id):
    '''In this case we will editing multiple column in each row.'''
    # Get parameters from users and selected row from cafe table.
    json_params = request.get_json()
    selected_cafe = db.get_or_404(Cafe, cafe_id)

    # Set new value that have been determined by json_params into selected row. 
    for param_name in json_params:
        selected_cafe.__setattr__(param_name, json_params[param_name])

    db.session.commit()

    return f"Edit data for {cafe_id} has been done."

# HTTP DELETE - Delete Record
@app.route("/delete-cafe/<int:cafe_id>", methods = ["DELETE"])
def delete_specific_cafe(cafe_id):
    # Check header's parameters if users type incorrect api key we will return error text with 403 status code.
    if request.headers.get("x-api-key") != api_secret_key["topSecretKey"]:
        return jsonify(
            {
                "status_code":403,
                "error":"Invalid token attemp."
            }
        ), 403

    # Get specific cafe from cafe_id.
    selected_cafe = db.get_or_404(Cafe, cafe_id) 
    # Delete determined row.
    db.session.delete(selected_cafe)
    db.session.commit()

    return f"Deleting id:{cafe_id} process has already successful"

if __name__ == '__main__':
    app.run(debug=True)
