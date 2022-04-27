# web_app/routes/home_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash
#from app.college_data import fetch_data

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("homes.html")