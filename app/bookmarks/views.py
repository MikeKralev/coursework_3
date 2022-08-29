from flask import Blueprint, redirect, render_template

from app.bookmarks.dao.bookmarks_dao import BookMarksDAO

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates', static_folder='static')

bookmarks_dao = BookMarksDAO('data/bookmarks.json', 'data/posts.json')


@bookmarks_blueprint.route("/bookmarks/add/<int:post_id>")
def add_bookmarks(post_id):
    """Добавить закладку"""
    bookmarks_dao.add_bookmark(post_id)
    return redirect('/', code=302)


@bookmarks_blueprint.route("/bookmarks/remove/<int:post_id>")
def remove_bookmarks(post_id):
    """Удалить закладку"""
    bookmarks_dao.remove_bookmark(post_id)
    return redirect('/', code=302)


@bookmarks_blueprint.route("/bookmarks/")
def show_all_bookmarks():
    """Страница для отображения всех постов по закладкам"""
    posts = bookmarks_dao.get_all_post_in_bookmarks()
    return render_template('bookmarks.html', posts=posts)
