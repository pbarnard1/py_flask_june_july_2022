# Useful links in chat and Discord:
# self vs. cls (thank you Justina!):
# https://www.pythonpool.com/python-cls-vs-self/#:~:text=cls%20refers%20to%20the%20class,instance%20variables%20in%20a%20class

class Zoo:
    organization = "Zoo Foundation" # Class variable - shared by all instances of your class

    def __init__(self, city, name, size, visitor_capacity, opening_date):
        self.city = city
        self.name = name
        self.size = size # Acreage
        self.visitor_capacity = visitor_capacity
        self.opening_date = opening_date # When the zoo opened for the first time
        self.animals = [] # NEW: Hold a list of Animals


class Animal:
    sponsor = "World Wildlife Foundation"

    def __init__(self, species, name, weight, color, height, birth_date = None):
        self.species = species
        self.name = name
        self.weight = weight
        self.color = color
        self.height = height
        self.birth_date = birth_date
        self.zoo = None # NEW: Linking one Zoo to this Animal

    def eat(self, food): # Instance method where ONE object - a specific Animal - eats
        # Notice the self.attribute_name, such as self.species!  "food" is a parameter passed into the function
        print(f"{self.species} named {self.name} is eating {food}")
        return self # To allow for chaining

    @classmethod # Note the decorator!
    def rename_sponsor(cls, new_name): # Class method (notice the "cls" instead of "self")
        cls.sponsor = new_name

    @staticmethod # Notice the decorator
    def is_affordable(costs, budget): # No cls or self!
        if costs > budget:
            print("Cannot accept this animal, sadly - too expensive to take care of")
            return False
        else:
            print("Yay!  The zoo can take this animal!")
            return True



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

# Class variable - accessing
print(Animal.sponsor)

# Static method
print(Animal.is_affordable(50000,100000))

# Link the penguin and the panda to Portland's zoo
portland_zoo.animals.append(this_panda)
portland_zoo.animals.append(famous_penguin)

# Loop through all the animals in Portland's zoo
for this_animal in portland_zoo.animals:
    print(f"{this_animal.species} named {this_animal.name}")

# Link a zoo to an animal
this_panda.zoo = portland_zoo
famous_penguin.zoo = portland_zoo

# Print the name of the Zoo for this Animal
print(famous_penguin.zoo.name)