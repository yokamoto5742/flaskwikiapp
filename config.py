class Config(object):
    DEBUG = True
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///memo.db'
    SQLALCHEMY_ECHO = True
