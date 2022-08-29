import pytest


class TestUsers:
    def test_get_posts_by_user_leo(self, test_users_dao):
        posts = test_users_dao.get_posts_by_user('leo')
        for post in posts:
            assert 'leo' in post.poster_name, 'Поиск постов по имени вернул не те посты'

    def test_get_posts_by_user_non_exist_user(self, test_users_dao):
        with pytest.raises(ValueError):
            test_users_dao.get_posts_by_user('non_exist_user')
