# Where we define our routes!
from flask_app import app # Needed for @app.route() among other things
from flask_app.models import user # Import models
from flask import render_template, redirect, request, session # Import methods from Flask

# Routes defined in the office hour

# VISIBLE ROUTES
@app.route("/")
def index(): # Root route that displays the login/registration page
    return render_template("login_reg.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/new_route")
def new_route_page():
    return render_template("new_route.html")

# INVISIBLE/HIDDEN ROUTES
@app.route("/register", methods=["POST"]) # POST route where we register the user
def register_user():
    print(request.form)
    # 1: Validate the form data to make sure everything is good
    if not user.User.validate_user(request.form):
        # If it's no good, we send the user back
        return redirect("/") # Send back to login/reg
    # If it's good, then we can register the user

    # Save the user

    # Redirect the user to the dashboard
    return redirect("/dashboard")

@app.route("/login", methods=["POST"]) # POST route where we log in a user
def login_user():
    pass

@app.route('/logout')
def logout(): # We need to clear session, then go to the login/reg page
    pass