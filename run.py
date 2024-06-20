<<<<<<< HEAD
from app import app, config
import os

=======
from app import app
import os

from app.controllers import config

>>>>>>> 5b6e02677efb2eb2d84964daff6ebf6d266cef28
app.config.from_object(config.Config)

if not os.path.exists(config.Config.UPLOAD_IMAGES):
    os.makedirs(config.Config.UPLOAD_IMAGES)
if not os.path.exists(config.Config.UPLOAD_MUSICS):
    os.makedirs(config.Config.UPLOAD_MUSICS)

if __name__ == "__main__":
    app.run(debug=True)
<<<<<<< HEAD

=======
>>>>>>> 5b6e02677efb2eb2d84964daff6ebf6d266cef28
