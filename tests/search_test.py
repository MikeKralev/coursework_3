class TestSearch:
    def test_search_for_posts_by_кот(self, test_search_dao):
        posts = test_search_dao.search_for_post('кот')
        for post in posts:
            assert 'кот' in post.content.lower(), "Поиск по слову кот вернул не ты посты"
