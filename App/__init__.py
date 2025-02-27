from flask import Flask
from run import app

app = Flask(__name__)

if app.name == __name__:
    app.run(debug=True)



