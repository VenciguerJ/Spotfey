from flask import Flask

app = Flask(__name__)

from app.controllers import default
<<<<<<< HEAD
from app.config import Config
=======
from app.controllers.config import Config
>>>>>>> 5b6e02677efb2eb2d84964daff6ebf6d266cef28
