from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError
from models import Memo, User


class MemoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired('タイトルは必須入力です'),
                                             Length(max=10, message='タイトルは10文字以内で入力してください')])
    content = TextAreaField('内容:')
    submit = SubmitField('送信')

    def validate_title(self, title):
        memo = Memo.query.filter_by(title=title.data).first()
        if memo:
            raise ValidationError(f'タイトル「{title.data}」は既に登録されています。'
                                  f'別のタイトルを入力してください')


class LoginForm(FlaskForm):
    username = StringField('ユーザー名:',
                           validators=[DataRequired('ユーザー名は必須入力です')])
    password = PasswordField('パスワード:',
                             validators=[DataRequired('パスワードは必須入力です'),
                                         Length(4, 10,
                                                message='パスワードは4文字以上10文字以内で入力してください')])

    submit = SubmitField('ログイン')


class SignUpForm(LoginForm):
    submit = SubmitField('サインアップ')

    def validate_password(self, password):
        if not (any(c.isdigit() for c in password.data) and
                any(c.isalpha() for c in password.data) and
                any(c in '!@#$%^*()&' for c in password.data)):
            raise ValidationError('パスワードは英字と数字と記号 !@#$%^*()& を含めてください')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'ユーザー名「{username.data}」は既に登録されています。'
                                  f'別のユーザー名を入力してください')


class WikiForm(FlaskForm):
    keyword = StringField('検索ワード:', render_kw={'placeholder': '入力してください'})
    submit = SubmitField('Wiki検索')
