from app.posts.dao.posts_dao import MainDAO


class TagDAO(MainDAO):

    def search_by_tag(self, tag_name):
        """ Искать посты по хэш тегу"""
        tag = f"#{tag_name}"
        result = []

        posts = self.get_all()

        for post in posts:
            if tag in post.content:
                result.append(post)
        if result:
            return result
