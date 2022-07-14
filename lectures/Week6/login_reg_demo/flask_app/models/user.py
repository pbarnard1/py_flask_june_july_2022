from flask_app.config.mysqlconnection import connectToMySQL
# Might need to import the other model files
# from flask_app.models import ???
from flask import flash # Need this for validating the form data
import re # For the regex module (for checking emails)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask_bcrypt import Bcrypt
from flask_app import app # Need to import app for Bcrypt
bcrypt = Bcrypt(app)

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

    @classmethod
    def register_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return None
        else:
            return cls(results[0]) # Need [0] to grab a dictionary from the list called "results"

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return None
        else:
            return cls(results[0]) # Need [0] to grab a dictionary from the list called "results"

    # Validate the registration of a new user
    @staticmethod
    def validate_registration(form_data):
        is_valid = True # Assume FOR NOW everything is good
        # Check each field individually
        if len(form_data["first_name"]) < 3:
            is_valid = False # Form is now no good
            flash("First name must be 3 or more characters", "register")
        if len(form_data["last_name"]) < 3:
            is_valid = False # Form is now no good
            flash("Last name must be 3 or more characters", "register")
        # Check to see if email is in correct format
        if not EMAIL_REGEX.match(form_data['email']):
            is_valid = False # Form is now no good
            flash("Email is not in correct format", "register")
        # Check to see if email is not already taken (done Wednesday)
        email_data = {
            "email": form_data["email"] # New dictionary with just the email only
        }
        found_user_or_none = User.get_user_by_email(email_data)
        if found_user_or_none != None: # If a user with that email IS found - so we do NOT get None back
            is_valid = False # Form is now no good
            flash("Email is already taken", "register")
        # Check to see if password is long enough
        if len(form_data["password"]) < 8:
            is_valid = False # Form is now no good
            flash("Password must be 8 or more characters", "register")
        # Check to see if the passwords agree
        if form_data["password"] != form_data["confirm_password"]:
            is_valid = False
            flash("Passwords must agree", "register")
        return is_valid

    @staticmethod
    def validate_login(form_data):
        # Check to see if we can find a user with the given email - if not, don't bother checking the password
        email_data = {
            "email": form_data["email"]
        }
        # We'll get the found user as an object OR None if no user was retrieved
        found_user_or_none = User.get_user_by_email(email_data)
        if found_user_or_none == None: # No user found - that means a value of None
            flash("Invalid login credentials", "login") # Leave intentionally vague message to not tip off hackers
            return False
        # If we find someone with that email, then we can check the password
        if not bcrypt.check_password_hash(found_user_or_none.password, form_data['password']):
            flash("Invalid login credentials", "login")
            return False
        return found_user_or_none