from app import app
from model.user_model import user_model
obj = user_model()   

@app.route("/users/getall")
def signup():
    def user_getall_controller():
        return obj.user_getall_model()