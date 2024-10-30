# db.py
from flask_mongoengine import MongoEngine
from mongomock import MongoClient as MockMongoClient

db = MongoEngine()


def init_db(app):
    if app.config['MONGODB_SETTINGS']['host'].startswith('mongomock://'):
        app.config['MONGODB_SETTINGS']['client_class'] = MockMongoClient
    db.init_app(app)