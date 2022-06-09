my_list = [8, 5, "Hello there!", True, {"name": "Adrian", "city": "Seattle"}, [2, 3, 5]]

print(my_list[2])
print(my_list[4])
print(my_list[5])

print(my_list[5][1]) # Accessing a value in a nested list

print(my_list[4]["name"])

# Number of items in a list
print(len(my_list)) # len(list) is equivalent to array.length in JS

print(len(my_list[5])) # Count the number of items in the list at index 5 - [2, 3, 5] -> give you 3 values

# Add the string "Yay!" to the end of my_list
my_list.append("Yay!") # .append is equivalent to .push in JS
print(my_list)

my_dictionary = {
    "name": "Adrian",
    "city": "Seattle",
    "age": 50,
    "is_hungry": True,
    "my_favorite_foods": ["Pizza","Rice","Hamburgers"]
}

print(my_dictionary["age"])

# Print Hamburgers
print(my_dictionary["my_favorite_foods"][2]) # Key MUST be in quotes (unless you use a variable holding the name of the key)

# Alternate way
this_key = "my_favorite_foods"
print(my_dictionary[this_key][2])