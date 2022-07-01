Visible routes:
- "/" - shows the Welcome page where one can enter their name
- "/attractions" - shows the page where one can add tourist attractions

Invisible (hidden) routes:
- "/enter" - POST route that saves the name from the form in session, then sends the user to the attractions route
- "/exit" - clears session and sends the client back to the route that shows the welcome page ("/")
- "/add_attraction" - POST route that takes the attraction and city from the form and adds it to session
- "/reset_attractions" - clears the attractions from session