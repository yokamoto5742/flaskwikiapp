from flask import Blueprint, render_template
from wikipediaapi import Wikipedia
from forms import WikiForm
from flask_login import login_required

wiki_bp = Blueprint('wiki', __name__, url_prefix='/wiki')

wiki_ja = Wikipedia(language='ja', user_agent="my_custom_user_agent")


@wiki_bp.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = WikiForm()
    if form.validate_on_submit():
        keyword = form.keyword.data
        page = wiki_ja.page(keyword)

        if page.exists():
            return render_template('wiki/wiki_search_result.html',
                                   keyword=keyword, summary=page.summary[:200],
                                   url=page.fullurl)
        else:
            return render_template('wiki/wiki_search_result.html',
                                   error='指定されたキーワードの結果は見つかりませんでした。')

    return render_template('wiki/wiki_search.html', form=form)
