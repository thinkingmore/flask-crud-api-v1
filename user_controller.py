from app import app
@app.route("/users/signup")
def signup():
    return "This is the signup route"