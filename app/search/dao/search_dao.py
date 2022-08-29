from app.main.dao.main_dao import MainDAO


class SearchDAO(MainDAO):

    def search_for_post(self, query):
        """ Найти посты по ключевому слову"""
        result = []
        posts = self.get_all()
        query_lower = query.lower()
        for post in posts:
            if query_lower in post.content.lower():
                result.append(post)
        return result
