import json

from app.main.dao.main_dao import MainDAO


class BookMarksDAO(MainDAO):

    def __init__(self, bookmarks_path, path):
        super().__init__(path)
        self.bookmarks_path = bookmarks_path

    def get_bookmarks(self):
        """Получить список закладок"""
        with open(self.bookmarks_path, 'r', encoding='utf-8') as file:
            bookmarks_list = json.load(file)
        return bookmarks_list

    def get_all_post_in_bookmarks(self):
        """Получить все посты по закладкам"""
        bookmarks_list = self.get_bookmarks()
        posts = self.get_all()

        result = []
        for post in posts:
            if post.pk in bookmarks_list:
                result.append(post)
        return result

    def add_bookmark(self, post_id):
        """Добавить закладку"""
        bookmarks_list = self.get_bookmarks()
        if post_id not in bookmarks_list:
            bookmarks_list.append(post_id)

            with open(self.bookmarks_path, 'w', encoding='utf-8') as file:
                json.dump(bookmarks_list, file)

    def remove_bookmark(self, post_id):
        """Удалить закладку"""
        bookmarks_list = self.get_bookmarks()
        bookmarks_list.remove(post_id)
        with open(self.bookmarks_path, 'w', encoding='utf-8') as file:
            json.dump(bookmarks_list, file)
