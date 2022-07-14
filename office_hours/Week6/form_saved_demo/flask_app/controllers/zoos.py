# Where we define our routes!
from flask_app import app # Needed for @app.route() among other things
from flask_app.models import animal, zoo # Import models
from flask import render_template, redirect, request, session # Import methods from Flask

@app.route("/") # Root route that will redirect to the /zoos route
def index():
    return redirect("/zoos")

# VISIBLE routes
@app.route("/zoos") # Route shows ALL the zoos from our database in a page
def all_zoos_page(): 
    # Grab the zoos from the database and send it to the HTML file
    return render_template("all_zoos.html", all_zoos = zoo.Zoo.get_all_zoos())

@app.route("/zoos/new") # Shows the form where one can add a zoo
def new_zoo_page():
    return render_template("add_zoo_page.html")

@app.route("/zoos/<int:id>/view") # Shows the page where we can examine a specific zoo
def view_one_zoo_page(id):
    data = {
        "id": id # Need ID for the query
    }
    return render_template("view_one_zoo.html", this_zoo = zoo.Zoo.get_one_zoo_with_animals(data))

@app.route("/zoos/<int:id>/edit") # Shows the form where a specific zoo can be edited
def edit_one_zoo_page(id):
    data = {
        "id": id # Need ID for the query
    }
    return render_template("edit_zoo_page.html", this_zoo = zoo.Zoo.get_one_zoo(data))

# INVISIBLE or HIDDEN routes
@app.route("/zoos/<int:id>/delete") # Route that will delete a zoo from the database
def delete_zoo(id):
    data = {
        "id": id # Need ID for delete query
    }
    zoo.Zoo.delete_zoo(data)
    return redirect("/zoos")

@app.route("/zoos/add_zoo_to_db", methods=["POST"]) # POST route that will add a zoo to the database
def add_zoo_to_db():
    # Starting week 6, remember to check if someone is logged in AND
    # check to see if the validations pass
    # Save each input into session - just in case the validations fail
    session["name"] = request.form["name"]
    session["city"] = request.form["city"]
    session["size"] = request.form["size"]
    session["visitor_capacity"] = request.form["visitor_capacity"]
    session["opening_date"] = request.form["opening_date"]
    if not zoo.Zoo.validate_zoo(request.form):
        return redirect("/zoos/new")
    # If the validations succeed, there's no need to hold on these values
    session.pop("name")
    session.pop("city")
    session.pop("size")
    session.pop("visitor_capacity")
    session.pop("opening_date")
    # data dictionary that will hold the data from the form (mostly) and
    # possibly more
    data = {
        "name": request.form["name"],
        "city": request.form["city"],
        "size": request.form["size"],
        "visitor_capacity": request.form["visitor_capacity"],
        "opening_date": request.form["opening_date"],
    }
    # Call on the model file to add the zoo to the database
    zoo.Zoo.add_zoo(data) # file_name.Class_Name.method_name()
    # Redirect to the all zoos page
    return redirect("/zoos")

@app.route("/zoos/<int:id>/edit_zoo_in_db", methods=["POST"]) # POST route where a zoo will be edited in the database
def update_zoo_in_db(id):
    # Data dictionary that will hold the data from the form (mostly) and
    # possibly more - in this case, we need the id from the path variable as well!
    data = {
        "name": request.form["name"],
        "city": request.form["city"],
        "size": request.form["size"],
        "visitor_capacity": request.form["visitor_capacity"],
        "opening_date": request.form["opening_date"],
        "id": id # NEED THIS to properly update this specific zoo
    }
    # Call on the model file to send the query to the database
    zoo.Zoo.edit_zoo(data) # Call on the model to edit the zoo
    # Redirect to the individual zoo's page - notice the f string!
    return redirect(f"/zoos/{id}/view")