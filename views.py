from flask import render_template
from werkzeug.exceptions import NotFound
from app import app


@app.errorhandler(NotFound)
def show_404_page(error):
    msg = error.description
    print('エラー内容:', msg)
    return render_template('errors/404.html', msg=msg), 404
