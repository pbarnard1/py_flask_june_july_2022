from flask import Flask
app = Flask(__name__)
app.secret_key = "this_is_hush_a_secret" # For session and other stuff later