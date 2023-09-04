# Django imports
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
# local imports
from posts.models import Post


class HomePage(View):

    def get(self, request):
        posts = Post.objects.all()
        carousel_posts = posts[1:5]
        paginated = Paginator(posts, 10)
        page_number = request.GET.get('page')
        page = paginated.get_page(page_number)
        return render(request, 'home/index.html', {'posts': posts, 'page': page, 'carousel_posts': carousel_posts})


class SearchView(View):
    def get(self, request):
        search_query = request.GET.get('search')
        posts = Post.objects.filter(body__contains=search_query)
        return render(request, 'home/search.html', {'posts': posts, 'search_query': search_query})
