import os

class Config(object):
    DEBUG = True
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///memodb.db'
    SQLALCHEMY_ECHO = False
