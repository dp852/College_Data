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


@home_routes.route("/college/data", methods=["POST"])
def university():
    print("URL PARAMS:", dict(request.form))

    form_data = dict(request.form)
    college_name = form_data["College"] 

    results = get_data(val=college_name)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid Geography. Please try again."}), 404


@home_routes.route("/help")
def help():
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    return render_template("help.html")


@home_routes.route("/api/college/data")
def data_api():
    print("URL PARAMS:", dict(request.args))

    url_params = dict(request.args)
    college_name = url_params["College"] 

    results = get_data(val=college_name)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid Geography. Please try again."}), 404