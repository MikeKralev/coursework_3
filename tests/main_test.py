

class TestMain:
    def test_root_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код"""
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "Статус-код всех постов неверный"

    def test_get_post_all(self, test_main_dao):
        posts = test_main_dao.get_all()
        assert len(posts) > 0, "Возвращаемый список постов пуст"
        