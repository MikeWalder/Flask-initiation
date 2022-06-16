# Variables globales utilisables sur tout le projet

import os
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

FB_API_ID = "986598165347670"

# Database initialization
basedir = os.path.abspath(os.path.dirname(__file__))
# basedir is the absolute path of the directory where the program resides.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
