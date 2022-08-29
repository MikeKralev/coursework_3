from run import app


class TestAPI:
    def test_all_posts(self):
        response = app.test_client().get('/api/posts/', follow_redirects=True)
        assert type(response.json) is list, 'Возвращаемый тип не list'
        for post in response.json:
            assert post.get('poster_name') is not None, 'Ключ poster_name отсутствует'
            assert post.get('poster_avatar') is not None, 'Ключ poster_avatar отсутствует'
            assert post.get('pic') is not None, 'Ключ pic отсутствует'
            assert post.get('content') is not None, 'Ключ content отсутствует'
            assert post.get('views_count') is not None, 'Ключ views_count отсутствует'
            assert post.get('likes_count') is not None, 'Ключ likes_count отсутствует'
            assert post.get('pk') is not None, 'Ключ pk отсутствует'

    def test_one_post(self):
        response = app.test_client().get('/api/posts/1', follow_redirects=True)
        assert type(response.json) is dict, 'Возвращаемый тип не dict'
        assert response.json.get('poster_name') is not None, 'Ключ poster_name отсутствует'
        assert response.json.get('poster_avatar') is not None, 'Ключ poster_avatar отсутствует'
        assert response.json.get('pic') is not None, 'Ключ pic отсутствует'
        assert response.json.get('content') is not None, 'Ключ content отсутствует'
        assert response.json.get('views_count') is not None, 'Ключ views_count отсутствует'
        assert response.json.get('likes_count') is not None, 'Ключ likes_count отсутствует'
        assert response.json.get('pk') is not None, 'Ключ pk отсутствует'
