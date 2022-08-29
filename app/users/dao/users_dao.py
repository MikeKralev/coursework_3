from app.main.dao.main_dao import MainDAO


class UsersDAO(MainDAO):
    """ Найти посты по имени пользователя"""
    def get_posts_by_user(self, user_name):
        result = []
        posts = self.get_all()
        user_name_lower = user_name.lower()
        for post in posts:
            if user_name_lower in post.poster_name.lower():
                result.append(post)
        if result:
            return result
        raise ValueError('Такого пользователя нет или исходный список пуст, или у пользователя нет постов')
