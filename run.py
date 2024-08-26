from app import app
from app.controllers import config
import os

if not os.path.exists(config.Config.UPLOAD_IMAGES):
    os.makedirs(config.Config.UPLOAD_IMAGES)
if not os.path.exists(config.Config.UPLOAD_MUSICS):
    os.makedirs(config.Config.UPLOAD_MUSICS)

if __name__ == "__main__":
    app.run(debug=True)

