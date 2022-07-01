# Where we define our routes!
from flask_app import app # Needed for @app.route() among other things
from flask_app.models import animal, zoo # Import models
from flask import render_template, redirect, request, session # Import methods from Flask

# VISIBLE routes
@app.route("/animals") # Route shows ALL the animals from our database in a page
def all_animals_page(): 
    pass

@app.route("/animals/new") # Shows the form where one can add a animal
def new_animal_page():
    pass

@app.route("/animals/<int:id>/view") # Shows the page where we can examine a specific animal
def view_one_animal_page(id):
    pass

@app.route("/animals/<int:id>/edit") # Shows the form where a specific animal can be edited
def edit_one_animal_page(id):
    pass

# INVISIBLE or HIDDEN routes
@app.route("/animals/<int:id>/delete") # Route that will delete an animal from the database
def delete_animal(id):
    pass

@app.route("/animals/add_animal_to_db", methods=["POST"]) # POST route that will add an animal to the database
def add_animal_to_db():
    pass

@app.route("/animals/<int:id>/edit_animal_in_db", methods=["POST"]) # POST route where an animal will be edited in the database
def update_animal_in_db(id):
    pass