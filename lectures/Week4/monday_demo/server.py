from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # Equivalent to localhost:5000 or localhost:5000/
def index():
    name = "Adrian"
    return render_template("test_file.html", name = name, this_number = 40)

@app.route("/my_animals") # localhost:5000/my_animals
def animals_page(): # Route that goes through a list of animals
    animals = ["cat", "dog", "parrot", "hamster"]
    return render_template("my_animals.html", my_animals = animals)

@app.route("/<name>/<int:number>")
def name_page(name, number): # Notice the path variables being passed as parameters!
    return render_template("test_file.html",name = name, this_number = number)

# Run the app
if __name__=="__main__":
    app.run(debug=True)