from flask import Flask

app = Flask(__name__)

from app.controllers import default
from app.config import Config
