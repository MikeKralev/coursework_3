import logging

from flask import Flask, render_template

from app.main.views import main_blueprint
from app.posts.views import posts_blueprint
from app.search.views import search_blueprint
from app.users.views import users_blueprint
from app.api.views import api_blueprint
from app.tag.views import tag_blueprint
from app.bookmarks.views import bookmarks_blueprint

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config['app.json.ensure_ascii'] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(posts_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(tag_blueprint)
app.register_blueprint(bookmarks_blueprint)


@app.errorhandler(404)
def not_found_error(error):
    return 'Ошибка 404', 404


@app.errorhandler(500)
def not_found_error(error):
    return 'Ошибка 500', 500


if __name__ == '__main__':
    app.run()
