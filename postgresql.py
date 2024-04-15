SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'name': 'memodb.db'
})
