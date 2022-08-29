import logging

from flask import Blueprint, jsonify

from app.posts.dao.posts_dao import PostsDAO

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/api.log')
formatter_logger = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler.setFormatter(formatter_logger)
logger.addHandler(file_handler)


api_blueprint = Blueprint('api_blueprint', __name__)

api_dao = PostsDAO('data/posts.json', 'data/comments.json')


@api_blueprint.route('/api/posts/')
def api_posts():
    """API для всех постов"""
    posts = api_dao.get_all()
    logger.info('Запрос /api/posts/')
    return jsonify([post.__dict__ for post in posts])


@api_blueprint.route('/api/posts/<int:post_id>')
def api_get_post(post_id):
    """API для конкретного поста"""
    post = api_dao.get_post_by_pk(post_id)
    logger.info(f'Запрос /api/posts/{post_id}')
    return jsonify(post.__dict__)
