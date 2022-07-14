from flask_app.config.mysqlconnection import connectToMySQL
# Might need to import the other model files
from flask_app.models import animal
# from flask_app import app # Might need to import the app in certain cases
from flask import flash # For flash messages

class Zoo:
    db_name = "animals_zoos_schema" # Use a class variable later on - it'd be nice to not have to change the schema name a million times (hint)

    def __init__(self,data): # data is a DICTIONARY
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

    @classmethod # Don't forget this decorator!
    def add_zoo(cls, data): # Class method to add a zoo to the DB; need "data" as query depends on various values
        query = "INSERT INTO zoos (name, city, size, visitor_capacity, opening_date) VALUES (%(name)s, %(city)s, %(size)s, %(visitor_capacity)s, %(opening_date)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_zoos(cls): # No data parameter here as the query below doesn't need any specific values like id, name, etc.
        query = "SELECT * FROM zoos;"
        results = connectToMySQL(cls.db_name).query_db(query) # No data parameter needed
        if len(results) == 0: # If list is empty, return []
            return [] # Empty list because we return a list with any number of items (Zoos)
        else: # At least one zoo found
            # List that will hold objects that are Zoos
            zoo_objects = []
            for this_zoo_dictionary in results:
                # Create the Zoo object
                new_zoo_object = cls(this_zoo_dictionary)
                # Add the Zoo object to the list
                zoo_objects.append(new_zoo_object)
            return zoo_objects # Watch your indentation!

    @classmethod
    def get_one_zoo(cls, data):
        query = "SELECT * FROM zoos WHERE id = %(id)s;" # NEED id so we know which zoo to grab
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return None # None because we can only return one item at most
        else:
            # Create class instance from a dictionary at index 0 in the list of dictionaries called "results"
            return cls(results[0]) # Need [0] because "results" is a list, but we need a dictionary, which is at index 0

    @classmethod
    def get_one_zoo_with_animals(cls, data):
        query = "SELECT * FROM zoos LEFT JOIN animals ON zoos.id = animals.zoo_id WHERE zoos.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0:
            return None
        else: # A zoo was found
            # Create the Zoo object
            zoo_instance = cls(results[0])
            # Loop through all the animals that have been found
            for this_animal_dictionary in results:
                if this_animal_dictionary["animals.id"] == None: # Edge case: no animals linked to this Zoo
                    break # Exit for loop early - no Animals found
                # Create the Animal
                new_animal_dictionary = {
                    "id": this_animal_dictionary["animals.id"],
                    "species": this_animal_dictionary["species"],
                    "name": this_animal_dictionary["animals.name"],
                    "weight": this_animal_dictionary["weight"],
                    "color": this_animal_dictionary["color"],
                    "height": this_animal_dictionary["height"],
                    "created_at": this_animal_dictionary["animals.created_at"],
                    "updated_at": this_animal_dictionary["animals.updated_at"],
                }
                this_animal_object = animal.Animal(new_animal_dictionary)
                # Add this Animal to the list of animals found in this zoo
                zoo_instance.animals.append(this_animal_object)
            # Return the Zoo
            return zoo_instance

    @classmethod
    def edit_zoo(cls, data):
        query = "UPDATE zoos SET name = %(name)s, city = %(city)s, size = %(size)s, visitor_capacity = %(visitor_capacity)s, opening_date = %(opening_date)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_zoo(cls, data):
        query = "DELETE FROM zoos WHERE id = %(id)s;" # Don't forget the ID here!!
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_zoo(form_data):
        is_valid = True
        # Validating name
        if len(form_data["name"]) < 2: # Name has to be 2 or more characters
            flash("Name of zoo must be 2 or more characters")
            is_valid = False
        return is_valid