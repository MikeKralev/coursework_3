from flask import Blueprint, request, render_template

from app.users.dao.users_dao import UsersDAO

users_blueprint = Blueprint('user_blueprint', __name__, template_folder='templates', static_folder='static')

users_dao = UsersDAO('data/posts.json')


@users_blueprint.route('/users/<name>')
def users_page(name):
    """Все посты одного пользователя"""
    posts = users_dao.get_posts_by_user(name)
    return render_template('user-feed.html', posts=posts, name=name)
