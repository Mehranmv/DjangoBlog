import os
import django
from django.utils import timezone
django.setup()
from posts.models import Post


def publish_scheduled_posts():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'A.settings')
    try:
        django.setup()
    except ModuleNotFoundError as e:
        print("Failed to setup Django: ", str(e))
        return

    scheduled_posts = Post.objects.filter(publish_date__lte=timezone.now(), status='scheduled')
    for post in scheduled_posts:
        post.status = Post.PUBLISHED
        post.save()


publish_scheduled_posts()
