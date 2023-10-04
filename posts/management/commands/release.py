import os

from django.core.management.base import BaseCommand

from posts.models import Post, StatusChoices
from django.utils import timezone


class Command(BaseCommand):
    help = "Release all scheduled posts"

    def handle(self, *args, **kwargs):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'A.settings')
        scheduled_posts = Post.objects.filter(publish_date__lte=timezone.now(), status=StatusChoices.SCHEDULED.value)
        scheduled_posts.update(status=StatusChoices.PUBLISHED.value)
