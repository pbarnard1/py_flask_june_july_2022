from flask_app.config.mysqlconnection import connectToMySQL
# Might need to import the other model files
from flask_app.models import zoo
# from flask_app import app # Might need to import the app in certain cases

class Animal:
    # Use a class variable later on - it'd be nice to not have to change the schema name a million times (hint)
    db_name = "animals_zoos_schema"
    def __init__(self, data): # data is a dictionary - a row of data from your database
        self.id = data["id"]
        self.species = data["species"]
        self.name = data["name"]
        self.weight = data["weight"]
        self.color = data["color"]
        self.height = data["height"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.zoo = None # NEW: Linking one Zoo to this Animal

    @classmethod
    def add_animal(cls, data):
        query = "INSERT INTO animals (name, species, weight, color, height, zoo_id) VALUES (%(name)s, %(species)s, %(weight)s, %(color)s, %(height)s, %(zoo_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_animals_with_zoos(cls):
        query = "SELECT * FROM animals JOIN zoos ON animals.zoo_id = zoos.id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        print(results)
        if len(results) == 0: # No animals found
            return []
        else: # At least one animal is found
            all_animal_objects = []
            # Loop through the list of animal dictionaries
            for this_animal_dictionary in results:
                # Create the Animal object
                new_animal_object = cls(this_animal_dictionary)
                # Create the Zoo object
                this_zoo_dictionary = {
                    "id": this_animal_dictionary["zoos.id"], # Need table name as that column name is duplicated
                    "city": this_animal_dictionary["city"],
                    "name": this_animal_dictionary["zoos.name"],
                    "size": this_animal_dictionary["size"], # Acreage
                    "visitor_capacity": this_animal_dictionary["visitor_capacity"],
                    "opening_date": this_animal_dictionary["opening_date"], # When the zoo opened for the first time
                    "created_at": this_animal_dictionary["zoos.created_at"],
                    "updated_at": this_animal_dictionary["zoos.updated_at"],
                }
                new_zoo_object = zoo.Zoo(this_zoo_dictionary)
                # Link this Zoo to this Animal
                new_animal_object.zoo = new_zoo_object
                # Add this Animal to the list of all Animals
                all_animal_objects.append(new_animal_object)
            return all_animal_objects

    @classmethod
    def get_one_animal_with_zoo(cls, data):
        query = "SELECT * FROM animals JOIN zoos ON animals.zoo_id = zoos.id WHERE animals.id = %(id)s;" # Need table name after WHERE clause!!!
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0: # No animals found
            return None
        else: # At least one animal is found
            # Create the Animal object
            new_animal_object = cls(results[0]) # Need 0 because we need a DICTIONARY!
            # Create the Zoo object
            this_zoo_dictionary = {
                "id": results[0]["zoos.id"], # Need table name as that column name is duplicated
                "city": results[0]["city"],
                "name": results[0]["zoos.name"],
                "size": results[0]["size"], # Acreage
                "visitor_capacity": results[0]["visitor_capacity"],
                "opening_date": results[0]["opening_date"], # When the zoo opened for the first time
                "created_at": results[0]["zoos.created_at"],
                "updated_at": results[0]["zoos.updated_at"],
            }
            new_zoo_object = zoo.Zoo(this_zoo_dictionary)
            # Link this Zoo to this Animal
            new_animal_object.zoo = new_zoo_object
            return new_animal_object

    @classmethod
    def edit_animal(cls, data):
        query = "UPDATE animals SET name = %(name)s, species = %(species)s, weight = %(weight)s, color = %(color)s, height = %(height)s, zoo_id = %(zoo_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_animal(cls, data):
        query = "DELETE FROM animals WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
