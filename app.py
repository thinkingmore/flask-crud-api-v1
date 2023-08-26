from flask import Flask
app = Flask(__name__)
from dotenv import load_dotenv

load_dotenv()

@app.route("/")
def welcome():
    return "Hello We changed the text!"

@app.route("/home")
def home():
    return "Welcome to Flask!"

@app.route("/about")
def about():
    return "This is about page"

@app.route("/contact")
def contact():
    return "This is changed"

if __name__ == '__main__':
    app.run(debug=True)

from controller import * 

