from django.db import models


class CommentManager(models.Manager):
    def accepted(self, post):
        return self.filter(post=post, is_accepted=True)
