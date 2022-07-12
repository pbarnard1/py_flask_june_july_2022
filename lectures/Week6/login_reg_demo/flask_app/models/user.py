from flask_app.config.mysqlconnection import connectToMySQL
# Might need to import the other model files
# from flask_app.models import ???
# from flask_app import app # Might need to import the app in certain cases
from flask import flash # Need this for validating the form data
import re # For the regex module (for checking emails)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db_name = "users_schema_july_2022" # Replace this with the name of your schema name

    def __init__(self,data): # data is a DICTIONARY
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # self.recipes = [] # Empty list holding many items for this user, e.g. Recipes; add as many attributes as needed

    # Validate the user
    @staticmethod
    def validate_user(form_data):
        is_valid = True # Assume FOR NOW everything is good
        # Check each field individually
        if len(form_data["first_name"]) < 3:
            is_valid = False # Form is now no good
            flash("First name must be 3 or more characters")
        if len(form_data["last_name"]) < 3:
            is_valid = False # Form is now no good
            flash("Last name must be 3 or more characters")
        # Check to see if email is in correct format
        if not EMAIL_REGEX.match(form_data['email']):
            is_valid = False # Form is now no good
            flash("Email is not in correct format")
        # Check to see if email is not already taken (done Wednesday)

        # Check to see if password is long enough
        if len(form_data["password"]) < 8:
            is_valid = False # Form is now no good
            flash("Password must be 8 or more characters")
        # Check to see if the passwords agree
        if form_data["password"] != form_data["confirm_password"]:
            is_valid = False
            flash("Passwords must agree")
        return is_valid
