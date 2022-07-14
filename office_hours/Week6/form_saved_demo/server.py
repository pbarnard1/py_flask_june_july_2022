from flask_app import app # So we can run the app
from flask_app.controllers import animals, zoos # VERY IMPORTANT: ALWAYS import ALL of your controller files!

if __name__=="__main__": # Run the app
    app.run(debug=True)