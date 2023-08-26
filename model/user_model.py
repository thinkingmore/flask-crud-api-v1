import mysql.connector

class user_model():
    def __init__(self):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="12345", database="flask_crud_api")
            print("Connection established")
        except:
            print("Error: unable to connect to MySQL server")
    def user_getall_model(self):
        # connection to database
        #Query executiion code
        return "This is user sign_up model"