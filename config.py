import os
from postgresql import SQLALCHEMY_DATABASE_URI as DATABASE_URI


class Config(object):
    DEBUG = True
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres://",
    #                                                                  "postgresql://") or 'sqlite:///memodb.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
