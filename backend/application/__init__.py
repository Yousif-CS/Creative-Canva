from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
import gridfs
app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

db.createCollection("Users")
grid_fs = gridfs.GridFS(db)
db.createCollection("Photos")
from application import routes
