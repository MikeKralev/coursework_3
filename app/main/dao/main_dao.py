import json

from app.main.dao.post import Post


class MainDAO:

    def __init__(self, path):
        """ Путь к файлу с данными"""
        self.path = path

    def load_data(self):
        """ Создает список объектов класс Post"""
        with open(self.path, 'r', encoding='utf-8') as file:
            posts_data = json.load(file)
            posts = []

            for post in posts_data:
                posts.append(Post(
                    post['poster_name'],
                    post['poster_avatar'],
                    post['pic'],
                    post['content'],
                    post['views_count'],
                    post['likes_count'],
                    post['pk']
                ))
        return posts

    def get_all(self):
        """ Возвращает все посты"""
        posts = self.load_data()
        return posts
