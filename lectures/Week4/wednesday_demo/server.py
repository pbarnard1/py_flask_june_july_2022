from flask_app import app # Define the app
from flask_app.controllers import attractions # Define our routes by importing our controllers

# Run the app
if __name__=="__main__":
    app.run(debug=True)