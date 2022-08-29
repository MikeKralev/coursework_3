import pytest
import run
from app.main.dao.main_dao import MainDAO
from app.posts.dao.posts_dao import PostsDAO
from app.search.dao.search_dao import SearchDAO
from app.users.dao.users_dao import UsersDAO
posts_path = 'data/posts.json'
comments_path = 'data/comments.json'


@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()


@pytest.fixture()
def test_main_dao():
    main_dao = MainDAO(posts_path)
    return main_dao


@pytest.fixture()
def test_post_dao():
    posts_dao = PostsDAO(posts_path, comments_path)
    return posts_dao


@pytest.fixture()
def test_search_dao():
    search_dao = SearchDAO(posts_path)
    return search_dao


@pytest.fixture()
def test_users_dao():
    users_dao = UsersDAO(posts_path)
    return users_dao
