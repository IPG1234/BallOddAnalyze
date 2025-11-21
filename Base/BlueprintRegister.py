from App.Odd_500 import Odd500_Interface
from Base import app

app.register_blueprint(Odd500_Interface.bp)