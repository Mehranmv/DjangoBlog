# Django imports
from django.shortcuts import render
from django.views import View
from django.contrib.postgres.search import TrigramWordSimilarity
# local imports
from posts.models import Post
from .models import MenuItem
import utils
# python imports
from random import sample


class HomePage(View):

    def get(self, request):
        posts = Post.objects.filter(display_post=True, status='published')
        carousel_posts = posts.filter(is_carousel_item=True, status='published')
        menu_items = MenuItem.objects.all()
        if carousel_posts.exists():
            if carousel_posts.count() < 4:
                carousel_items = carousel_posts
            else:
                carousel_items = sample(list(carousel_posts), 4)
        else:
            carousel_items = sample(list(posts), 1)
            # carousel_items = carousel_posts
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
    def get(self, request):
        posts = Post.objects.all()
        search_query = request.GET.get('search')
        posts = posts.annotate(similarity=TrigramWordSimilarity(search_query, 'title')).filter(
            similarity__gt=0.3).order_by('-similarity')
        context = {
            'posts': posts,
            'search_query': search_query
        }
        return render(request, 'home/search.html', context)
