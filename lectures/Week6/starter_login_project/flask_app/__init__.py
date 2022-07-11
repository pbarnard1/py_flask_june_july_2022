from flask import Flask
app = Flask(__name__)
app.secret_key = "its_a_secret_to_everybody" # For session and other stuff later