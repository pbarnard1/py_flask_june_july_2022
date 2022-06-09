# If statement demo
exit_number = 5

if exit_number == 6:
    print("Time to get off freeway")
    print("Time to slow down")
else:
    print("Stay on freeway")

my_grade = 95
if my_grade >= 90:
    print("You got an A! Well done!!")
elif my_grade >= 80:
    print("You got a B!  Very nice!!")
elif my_grade >= 70:
    print("Not bad at all!")
else:
    print("That's okay!")

# Demo of "or"/"and"
number = 6
if number > 10 or number < 0: # Order of checking could be important
    print("Number must be from 0 to 10")

if number >= 8 and number <= 10: # Order of checking could be important
    print("Good score!")


x = [8, 4, 5, 10, 12]

for num in x: # num will be 8, then 4, then 5, etc. - no index necessary
    if num % 2 == 0:
        print(f"{num} is even") # Review of f-strings!
    else:
        print(num, "is odd")

for i in range(len(x)): # range(5) -> 0, 1, 2, 3, 4
    if x[i] % 2 == 0: 
        print(f"{x[i]} is even")
    else:
        print(x[i], "is odd")

def sum_list(lst):
    total = 0 # Need to define BEFORE the loop to keep track of the running sum
    for item in lst:
        total += item # Add current value to sum
        print(f"Total is now {total}")
    return total # Return AFTER the for loop is over - notice how it's tabbed

print(sum_list([5, 3]))