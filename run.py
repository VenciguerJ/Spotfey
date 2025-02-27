from flask import Flask

from App import main
app = Flask(__name__)


app.run(debug=True)