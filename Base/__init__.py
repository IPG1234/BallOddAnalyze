from flask import Flask
from Base.Browser import Browser

app = Flask(__name__)
browser = Browser()

def create_app():
    global app
    # with app.app_context():
    #     import Base.BlueprintRegister
    #     from DbManager import db
    #     db.create_all()
    return app