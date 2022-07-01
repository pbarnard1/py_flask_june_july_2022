from flask_app.config.mysqlconnection import connectToMySQL
# Might need to import the other model files
from flask_app.models import animal
# from flask_app import app # Might need to import the app in certain cases

class Zoo:
    # Use a class variable later on - it'd be nice to not have to change the schema name a million times (hint)

    def __init__(self,data):
        self.id = data["id"]
        self.city = data["city"]
        self.name = data["name"]
        self.size = data["size"] # Acreage
        self.visitor_capacity = data["visitor_capacity"]
        self.opening_date = data["opening_date"] # When the zoo opened for the first time
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.animals = [] # NEW: Hold a list of Animals

    # We will write our queries here and talk to MySQL