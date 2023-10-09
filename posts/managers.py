from django.db import models


class CommentManager(models.Manager):
    def accepted(self, post):
        return self.filter(post=post, is_accepted=True)


class PostManager(models.Manager):
    def show_filter(self):
        return self.filter(display_post=True, status='1')

    def carousel_posts_filter(self):
        return self.filter(display_post=True, is_carousel_item=True, status='1')
