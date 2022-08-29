import json

from app.main.dao.main_dao import MainDAO
from app.posts.dao.comment import Comment


class PostsDAO(MainDAO):

    def __init__(self, posts_path, comments_path):
        """ Путь к файлу с данными"""
        self.path = posts_path
        self.comments_path = comments_path

    def get_post_by_pk(self, pk):
        """Вернуть пост по его id(pk)"""
        posts = self.get_all()
        for post in posts:
            if pk == post.pk:
                break

        new_content = []
        content = post.content.split()
        for word in content:
            if word.startswith('#'):
                new_content.append(f'<a href="/tag/{word[1:]}">{word}</a>')
            else:
                new_content.append(word)
        post.content = ' '.join(new_content)
        return post

    def load_comment(self):
        """ Подгрузить все комменты из файла"""
        with open(self.comments_path, 'r', encoding='utf-8') as file:
            comments_data = json.load(file)
            comments = []

            for comment in comments_data:
                comments.append(Comment(
                    comment['post_id'],
                    comment['commenter_name'],
                    comment['comment'],
                    comment['pk'],
                ))
        return comments

    def get_comments_by_post_id(self, post_id):
        """ Подгрузить комменты к посту"""
        comments = self.load_comment()
        result = []
        for comment in comments:
            if post_id == comment.post_id:
                result.append(comment)
        if result:
            return result
        raise ValueError('Такого поста нет или пустой список постов, или у поста нет комментов')
