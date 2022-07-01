from flask_app.config.mysqlconnection import connectToMySQL
# Might need to import the other model files
from flask_app.models import zoo
# from flask_app import app # Might need to import the app in certain cases

class Animal:
    # Use a class variable later on - it'd be nice to not have to change the schema name a million times (hint)

    def __init__(self, data): # data is a dictionary - a row of data from your database
        self.id = data["id"]
        self.species = data["species"]
        self.name = data["name"]
        self.weight = data["weight"]
        self.color = data["color"]
        self.height = data["height"]
        self.birth_date = data["birth_date"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.zoo = None # NEW: Linking one Zoo to this Animal

    # We will write our queries here and talk to MySQL