# Useful links in chat and Discord (thanks Jacob and Calico!):
# Class vs static methods:
# https://www.geeksforgeeks.org/class-method-vs-static-method-python/
# Python classes
# https://www.w3schools.com/python/python_classes.asp
# Naming:
# https://google.github.io/styleguide/pyguide.html#316-naming

class Zoo:
    organization = "Zoo Foundation" # Class variable - shared by all instances of your class

    def __init__(self, city, name, size, visitor_capacity, opening_date):
        self.city = city
        self.name = name
        self.size = size # Acreage
        self.visitor_capacity = visitor_capacity
        self.opening_date = opening_date # When the zoo opened for the first time


class Animal:
    def __init__(self, species, name, weight, color, height, birth_date = None):
        self.species = species
        self.name = name
        self.weight = weight
        self.color = color
        self.height = height
        self.birth_date = birth_date

    def eat(self, food):
        # Notice the self.attribute_name, such as self.species!  "food" is a parameter passed into the function
        print(f"{self.species} named {self.name} is eating {food}")
        return self # To allow for chaining


portland_zoo = Zoo("Portland", "The Oregon Zoo", 64, 10000, "1888-08-15")
seattle_zoo = Zoo("Seattle","Woodland Park Zoo", 92, 15000, "1940-03-05")
print(Zoo.organization)
print(seattle_zoo.organization)

# Test with accessing 
# seattle_zoo.organization = "New Foundation" # ONLY changes the organization for seattle_zoo
# Zoo.organization = "Brand new name" # Changes the organization for ALL zoos
# print("Test")
# print(Zoo.organization)
# print(seattle_zoo.organization)
# print(portland_zoo.organization)


famous_penguin = Animal("Penguin", "Adrian", 20, "Mixed", 50)
this_panda = Animal("Panda", "Jane", 250, "Mixed", 75, "1985-03-11")

print(this_panda.birth_date)

this_panda.eat("bamboo").eat("leaves") # Chaining demo