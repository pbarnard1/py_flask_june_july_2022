# https://docs.python.org/3/library/typing.html (optional article regarding typing: -> )
# Video on inheritance (thanks Justina!!): https://www.youtube.com/watch?v=C2QfkDcQ5MU&t=626s

class Television:
    seller = "MyStore" # Class variable holding the store that's selling these TVs
    approver = "FCC" # Class variable holding the group that is responsible for approving the selling of these TVs
    def __init__(self, brand, size, price, is_on = False):
        self.brand = brand
        self.size = size
        self.price = price
        self.is_on = is_on # Assume the TV isn't already on when it's created or bought
        self.volume = 25 # Current volume
        self.channel = 3 # Starting TV channel

    def turn_on(self):
        if self.is_on == True: # You could leave out " == True"
            print("TV is already on")
        else:
            print("Turning TV on")
            self.is_on = True
        return self # Allow for chaining

    def turn_off(self):
        if self.is_on:
            print("Turning TV off")
            self.is_on = False
        else:
            print("TV is already off")
        return self # Allow for chaining

    def raise_volume(self):
        self.volume += 1
        return self # Allow for chaining

    def lower_volume(self):
        self.volume -= 1
        return self # Allow for chaining



my_tv = Television("Samsung", 42, 250)
print("Adrian's TV:")
print(my_tv.is_on)
grays_monitor = Television("Sony", 32, 50, True)
print("Justina's TV:")
print(grays_monitor.is_on)

my_tv.turn_on().turn_on().turn_off()

my_tv.turn_on().raise_volume().raise_volume()

print(my_tv.volume)

print(Television.approver) # More proper way to access a class variable

print(my_tv.approver) # Another way to access a class variable - not recommended
print(grays_monitor.approver)

# NOT recommended below
# my_tv.approver = "Another organization"
# print(Television.approver)
# print(my_tv.approver)
# print(grays_monitor.approver)

# Proper way to change a class variable
Television.approver = "New FCC"
print(Television.approver)
print(my_tv.approver)
print(grays_monitor.approver)
