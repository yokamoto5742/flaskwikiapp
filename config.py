class Config(object):
    DEBUG = True
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'postgres://u2k83758nrpbqs:p19597ac1773b6eb8280a7a1edac258551d90c73d8d19d36eb5ad4daa882578fb@c7gljno857ucsl.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dc47e1ohccf94l'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///memodb.db'
