# Where we define our routes!
from flask_app import app # Needed for @app.route() among other things
from flask_app.models import animal, zoo # Import models
from flask import render_template, redirect, request, session # Import methods from Flask

# VISIBLE routes
@app.route("/animals") # Route shows ALL the animals from our database in a page
def all_animals_page(): 
    return render_template("all_animals.html", all_animals = animal.Animal.get_all_animals_with_zoos())

@app.route("/animals/new") # Shows the form where one can add a animal
def new_animal_page():
    return render_template("add_animal_page.html", all_zoos = zoo.Zoo.get_all_zoos())

@app.route("/animals/<int:id>/view") # Shows the page where we can examine a specific animal
def view_one_animal_page(id):
    data = {
        "id": id
    }
    return render_template("view_one_animal.html", this_animal = animal.Animal.get_one_animal_with_zoo(data))

@app.route("/animals/<int:id>/edit") # Shows the form where a specific animal can be edited
def edit_one_animal_page(id):
    data = {
        "id": id
    }
    return render_template("edit_animal_page.html", this_animal = animal.Animal.get_one_animal_with_zoo(data), all_zoos = zoo.Zoo.get_all_zoos())

# INVISIBLE or HIDDEN routes
@app.route("/animals/<int:id>/delete") # Route that will delete an animal from the database
def delete_animal(id):
    data = {
        "id": id
    }
    animal.Animal.delete_animal(data)
    return redirect("/animals")

@app.route("/animals/add_animal_to_db", methods=["POST"]) # POST route that will add an animal to the database
def add_animal_to_db():
    # Starting week 6, remember to check if someone is logged in AND
    # check to see if the validations pass
    # Data from the form
    data = {
        "name": request.form["name"],
        "species": request.form["species"],
        "weight": request.form["weight"],
        "color": request.form["color"],
        "height": request.form["height"],
        "zoo_id": request.form["zoo_id"],
    }
    animal.Animal.add_animal(data) # Call on model to add this animal to DB
    return redirect("/animals") # Go to all animals page

@app.route("/animals/<int:id>/edit_animal_in_db", methods=["POST"]) # POST route where an animal will be edited in the database
def update_animal_in_db(id):
    data = {
        "name": request.form["name"],
        "species": request.form["species"],
        "weight": request.form["weight"],
        "color": request.form["color"],
        "height": request.form["height"],
        "zoo_id": request.form["zoo_id"],
        "id": id # MUST INCLUDE ID OF animal!!!
    }
    animal.Animal.edit_animal(data) # Edit animal in DB
    return redirect(f"/animals/{id}/view")