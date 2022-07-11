from flask_app.config.mysqlconnection import connectToMySQL
# Might need to import the other model files
# from flask_app.models import ???
# from flask_app import app # Might need to import the app in certain cases

class User:
    db_name = "" # Replace this with the name of your schema name

    def __init__(self,data): # data is a DICTIONARY
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # self.recipes = [] # Empty list holding many items for this user, e.g. Recipes; add as many attributes as needed
