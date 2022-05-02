# web_app/routes/home_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.college_data import get_data

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("homes.html")


@home_routes.route("/college/data")
def university():
    print("URL PARAMS:", dict(request.form))

    form_data = dict(request.form)
    data = request.args.get("College") 

    results = get_data(val=data)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid Geography. Please try again."}), 404
