from django.contrib.sitemaps import Sitemap
from posts.models import Post


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_for_xml
