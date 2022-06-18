class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.author = data["author"]
        self.pages = data["pages"]

my_data = [
    {
        "id": 1,
        "title": "The Old Man and the Sea",
        "author": "Ernest Hemingway",
        "pages": 200
    },
    {
        "id": 2,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "pages": 300
    }
]

# Loop that creates a list of Books (objects):
my_book_objects = []
for this_book_dictionary in my_data: # Loop through a list
    new_book_object = Book(this_book_dictionary) # Creating the Book instance (object)
    my_book_objects.append(new_book_object) # Add this Book object (instance) to the list

# Display each book's title with this list of Books
for this_book_object in my_book_objects:
    print(this_book_object.title)
