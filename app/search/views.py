from flask import Blueprint, request, render_template

from app.search.dao.search_dao import SearchDAO

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates', static_folder='static')

search_dao = SearchDAO('data/posts.json')


@search_blueprint.route('/search/')
def search_page():
    """ Найденные посты"""
    query = request.args.get('s')
    posts = search_dao.search_for_post(query)[:10]
    return render_template('search.html', posts=posts)
