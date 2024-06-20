from app import app
import os

from app.controllers import config

app.config.from_object(config.Config)

if not os.path.exists(config.Config.UPLOAD_IMAGES):
    os.makedirs(config.Config.UPLOAD_IMAGES)
if not os.path.exists(config.Config.UPLOAD_MUSICS):
    os.makedirs(config.Config.UPLOAD_MUSICS)

if __name__ == "__main__":
    app.run(debug=True)
