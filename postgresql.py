SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'name': 'flaskapp'  # 事前に作成したデータベース名
})
