x = 5
print(x) # Shows the value 5 in the terminal

"""
Called a docstring, technically

This is a
multi-line
comment.
"""

x = "First string"
y = "Second string"
print("Incorrect answer:")
print(x+y) # If you use the + symbol, you HAVE to add the space yourself
print("Correct answer #1:")
print(x + " " + y)
print("Correct answer #2:")
print(x, y) # Using a comma will automatically add the space for you

z = 40
print(f'The value of z is {z}')

my_list = [10, "Adrian", True, False, None, 14.8]

print(my_list[5])
print(my_list[-1]) # Another (weird) correct way to do it
# print(my_list[-7]) # ERROR - can't go past -6 in terms of index

# List slicing
print(my_list[2:]) # Get [True, False, None, 14.8]
print(my_list[:3]) # Get [10, "Adrian", True] - NO False
print(my_list[1:4]) # Get ["Adrian", True, False] - None is excluded

my_dictionary = {
    "name": "Adrian",
    "food": "Pizza",
    "integer": 88,
    "city": "Seattle",
    "is_happy": True,
    "my_colors": ["Red","Orange","Brown"],
}

print(my_dictionary["food"])

print(my_dictionary["my_colors"]) # Print entire list
print(my_dictionary["my_colors"][0]) # Print "Red"