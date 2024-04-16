import os
from postgresql import SQLALCHEMY_DATABASE_URI as DATABASE_URI


class Config(object):
    DEBUG = True
    SECRET_KEY = 'secret_key'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres://",
                                                                     "postgresql://")
    # ローカル環境のPostgreSQL に接続する場合は、以下の行を有効にしてください
    # SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
