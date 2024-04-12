from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Memo
from forms import MemoForm
from flask_login import login_required, current_user

memo_bp = Blueprint('memo', __name__, url_prefix='/memo')


@memo_bp.route('/')
@login_required
def index():
    memos = Memo.query.filter_by(user_id=current_user.id).all()
    return render_template('memo/index.html', memos=memos)


@memo_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = MemoForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        memo = Memo(title=title, content=content, user_id=current_user.id)
        db.session.add(memo)
        db.session.commit()
        flash('登録しました')
        return redirect(url_for('memo.index'))

    return render_template('memo/create_form.html', form=form)


@memo_bp.route('/update/<int:memo_id>', methods=['GET', 'POST'])
@login_required
def update(memo_id):
    target_data = Memo.query.filter_by(id=memo_id, user_id=current_user.id).first_or_404()

    form = MemoForm(obj=target_data)
    form.edit_id.data = target_data.id

    if form.validate_on_submit():
        target_data.title = form.title.data
        target_data.content = form.content.data
        db.session.merge(target_data)
        db.session.commit()
        flash('変更しました')
        return redirect(url_for('memo.index'))

    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{field}: {error}")

    return render_template('memo/update_form.html', form=form, edit_id=target_data.id)


@memo_bp.route('/delete/<int:memo_id>')
@login_required
def delete(memo_id):
    memo = Memo.query.filter_by(id=memo_id, user_id=current_user.id).first_or_404()
    db.session.delete(memo)
    db.session.commit()
    flash('削除しました')
    return redirect(url_for('memo.index'))


@memo_bp.route('/create_from_search', methods=['POST'])
@login_required
def create_from_search():
    title = request.form['title']
    content = request.form['content']
    new_memo = Memo(title=title, content=content, user_id=current_user.id)
    db.session.add(new_memo)
    db.session.commit()
    flash('wikiからデータ登録しました')
    return redirect(url_for('memo.index'))
