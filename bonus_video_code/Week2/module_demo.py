# import random # One way to import a module

# # Generate a single random number
# for i in range(100):
#     print(f"Trial number {i+1}: {random.randint(1,10)}") # Need the name of the module

from random import randint # Other way to import - specifically a function from the module
import my_oop_classes
from my_files import my_values # Imports a module (file) from a package (folder)

# Generate a single random number
for i in range(100):
    print(f"Trial number {i+1}: {randint(1,10)}") # Do NOT need the name of the module

my_library = my_oop_classes.Library("Seattle","Wallingford Public Library")
print(my_library.name)

my_book = my_oop_classes.Book("The Old Man and the Sea", "Ernest Hemingway", 200)
print(my_book.author)

print(my_values.x)
print(my_values.y)

my_computer = my_values.Computer("HP",32)
print(my_computer.brand)