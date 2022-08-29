from flask import Blueprint, render_template

from app.tag.dao.tag_dao import TagDAO

tag_blueprint = Blueprint('tag_blueprint', __name__, template_folder='templates', static_folder='static')

tag_dao = TagDAO('data/posts.json')


@tag_blueprint.route('/tag/<tag_name>')
def tag_page(tag_name):
    """ Отображает список найденный по хэш тегу постов"""
    print(tag_name)
    posts = tag_dao.search_by_tag(tag_name)
    return render_template('tag.html', posts=posts, tag=tag_name)
