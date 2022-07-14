# Where we define our routes!
from flask_app import app # Needed for @app.route() among other things
from flask_app.models import user # Import models
from flask import render_template, redirect, request, session # Import methods from Flask
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Routes defined in the office hour

# VISIBLE ROUTES
@app.route("/")
def index(): # Root route that displays the login/registration page
    return render_template("login_reg.html")

@app.route("/dashboard")
def dashboard():
    # IMPORTANT NOTE: If nobody is logged in, send them back to the login/register route 
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": session["user_id"]
    }
    return render_template("dashboard.html", this_user = user.User.get_user_by_id(data))

@app.route("/new_route")
def new_route_page():
    # IMPORTANT NOTE: If nobody is logged in, send them back to the login/register route 
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": session["user_id"]
    }
    return render_template("new_route.html", this_user = user.User.get_user_by_id(data))

# INVISIBLE/HIDDEN ROUTES
@app.route("/register", methods=["POST"]) # POST route where we register the user
def register_user():
    print(request.form)
    # 1: Validate the form data to make sure everything is good
    if not user.User.validate_registration(request.form):
        # If it's no good, we send the user back
        return redirect("/") # Send back to login/reg
    # If it's good, then we can register the user
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form['password']), # REMEMBER TO HASH YOUR PASSWORD!
    }
    # Save the user in the DB, then save the ID of the user in session
    session["user_id"] = user.User.register_user(data)
    # Redirect the user to the dashboard
    return redirect("/dashboard")

@app.route("/login", methods=["POST"]) # POST route where we log in a user
def login_user():
    # Validation the login stuff
    found_user_or_false = user.User.validate_login(request.form)
    if found_user_or_false == False:
        # If it's no good, we send the user back
        return redirect("/") # Send back to login/reg
    # Grab the user, then save the ID in session
    session["user_id"] = found_user_or_false.id
    # Send to the dashboard
    return redirect("/dashboard")

@app.route('/logout')
def logout(): # We need to clear session, then go to the login/reg page
    session.clear()
    return redirect("/")