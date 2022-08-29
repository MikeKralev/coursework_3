from flask import Blueprint, render_template

from app.main.dao.main_dao import MainDAO
from app.bookmarks.dao.bookmarks_dao import BookMarksDAO

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', static_folder='static')

main_dao = MainDAO('data/posts.json')
bookmarks_dao = BookMarksDAO('data/bookmarks.json', 'data/posts.json')


@main_blueprint.route('/')
def main_page():
    """ Главная страница"""
    posts = main_dao.get_all()
    bookmarks_count = len(bookmarks_dao.get_bookmarks())
    return render_template('index.html', posts=posts, bookmarks_count=bookmarks_count)
