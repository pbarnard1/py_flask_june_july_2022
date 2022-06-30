from flask_app import app
from flask import render_template, request, redirect, session


# Visible routes
@app.route("/") # Root route that displays the welcome page
def home_page():
    return render_template("welcome_page.html")

@app.route("/attractions")
def tourist_page():
    if "name" not in session: # If someone didn't enter their name, send them back
        return redirect("/")
    if "attractions" not in session: # If no attractions saved, create a new, empty list
        session["attractions"] = []
    print(session["attractions"])
    return render_template("attractions_page.html")

# Invisible (hidden) routes
# Route for allowing someone to enter or "log in" (more formal discussion on logging in will be in Week 6)
@app.route('/enter', methods=["POST"])
def enter():
    session["name"] = request.form["name"] # Save the name in session
    return redirect("/attractions")

# Leave the attractions page and reset session
@app.route("/exit")
def exit():
    session.clear()
    return redirect("/") # Go back to route that shows welcome page

@app.route("/add_attraction", methods=["POST"])
def add_attraction_to_session():
    # Unfortunately, you can't directly edit a list from session unless you do the following:
    # session.modified = True # NEEDED since lists will not be changed unless this flag's value is set to True
    # So a workaround is to save the original list in a new variable, then use that variable to add to the list,
    # then save the list in session
    old_attractions = session["attractions"]
    old_attractions.append(f"{request.form['attraction']} in {request.form['city']}")
    session["attractions"] = old_attractions
    return redirect("/attractions")

# Clear the attractions saved in session - but NOT the name of the person
@app.route("/reset_attractions")
def clear_attractions():
    session.pop("attractions")
    return redirect("/attractions")