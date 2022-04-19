# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    #return "About Me"
    return render_template("about.html")

@home_routes.route("/another")
def another():
    print("Here is another page"),
    return "Here is another page"


@home_routes.route("/hello")
def hello_world():
    print("HELLO...", dict(request.args))
   
   #Go check url params for one called "name" and use it if possible, otherwise use a default value
   #If no name parameter is specified, use a default value
    name = request.args.get("name") or "World"
   
    message = f"Hello, {name}!"
    #return message
    return render_template("hello.html")

