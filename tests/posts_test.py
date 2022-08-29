import pytest


class TestPosts:
    def test_get_post_by_pk_1(self, test_post_dao):
        post = test_post_dao.get_post_by_pk(1)
        assert post.pk == 1, 'Вернулся не тот пост, что был запрошен'

    def test_get_comments_no_comments(self, test_post_dao):
        with pytest.raises(ValueError):
            test_post_dao.get_comments_by_post_id(8)

    def test_get_comments_post_not_exist(self, test_post_dao):
        with pytest.raises(ValueError):
            test_post_dao.get_comments_by_post_id(9)
            