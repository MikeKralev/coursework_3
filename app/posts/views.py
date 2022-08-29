from flask import Blueprint, render_template

from app.posts.dao.posts_dao import PostsDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates', static_folder='static')

posts_dao = PostsDAO('data/posts.json', 'data/comments.json')


@posts_blueprint.route('/posts/<int:post_id>')
def post_page(post_id):
    post = posts_dao.get_post_by_pk(post_id)
    comments = posts_dao.get_comments_by_post_id(post_id)
    return render_template('post.html', comments=comments, post=post)
