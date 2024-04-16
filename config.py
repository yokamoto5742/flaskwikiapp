import os
from postgresql import SQLALCHEMY_DATABASE_URI as DATABASE_URI
from flask import Flask
from flask_session import Session
import redis

app = Flask(__name__)

IS_HEROKU_APP = "DYNO" in os.environ and "CI" not in os.environ

DEBUG = IS_HEROKU_APP or not IS_HEROKU_APP

ALLOWED_HOSTS = ["*"] if IS_HEROKU_APP else []


class Config(object):
    DEBUG = True
    SECRET_KEY = 'secret_key'

    if IS_HEROKU_APP:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres://",
                                                                         "postgresql://")
    else:
        SQLALCHEMY_DATABASE_URI = DATABASE_URI
        app.config['SESSION_TYPE'] = 'redis'
        app.config['SESSION_REDIS'] = redis.from_url(os.environ.get("REDIS_URL", "redis://127.0.0.1:6379/1"))
        app.config['SESSION_USE_SIGNER'] = True
        app.config['SESSION_PERMANENT'] = False
        app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30分（秒単位）

        Session(app)

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
