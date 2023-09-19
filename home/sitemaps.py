from django.contrib.sitemaps import Sitemap
from posts.models import Post


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = 'http'

    def items(self):
        return Post.objects.filter(display_post=True)

    def lastmod(self, obj):
        return obj.updated
