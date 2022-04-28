# web_app/routes/home_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.college_data import get_data

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("homes.html")


@home_routes.route("/collegedata")
def university():
    print("WEATHER FORECAST (API)...")
    print("URL PARAMS:", dict(request.args))

    country_code = request.args.get("country_code") or "US"
    zip_code = request.args.get("zip_code") or "20057"

    results = get_data(val=val)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid Geography. Please try again."}), 404
