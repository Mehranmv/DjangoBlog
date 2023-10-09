# Django imports
from django.shortcuts import render
from django.views import View
from django.contrib.postgres.search import TrigramWordSimilarity
# local imports
from posts.models import Post, StatusChoices
from .models import MenuItem
import utils
# python imports
from random import sample


class HomePage(View):

    def get(self, request):
        """
        show_filter and carousel_posts_filter are two manager for Post module
        """
        posts = Post.objects.show_filter()
        carousel_posts = Post.objects.carousel_posts_filter()
        menu_items = MenuItem.objects.all()
        if carousel_posts.exists():
            if carousel_posts.count() < 4 and carousel_posts.count() != 0:
                carousel_items = carousel_posts
            else:
                carousel_items = sample(list(carousel_posts), 4)
        else:
            carousel_items = sample(list(posts), 4)
        page_number = request.GET.get('page')
        page = utils.pagination(posts, page_number)
        context = {
            'posts': posts,
            'page': page,
            'carousel_items': carousel_items,
            'menu_items': menu_items,
        }
        return render(request, 'home/index.html', context)


class SearchView(View):
    """
    the search is using pg_trgm of Postgresql for similarity
    """
    def get(self, request):
        posts = Post.objects.all()
        search_query = request.GET.get('search')
        posts = posts.annotate(
            similarity=TrigramWordSimilarity(search_query, expression='title_fa')).filter(
            similarity__gt=0.3).order_by('-similarity')
        context = {
            'posts': posts,
            'search_query': search_query
        }
        return render(request, 'home/search.html', context)
