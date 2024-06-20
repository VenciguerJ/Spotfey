from flask import Flask

app = Flask(__name__)

from app.controllers import default
from app.controllers.config import Config
