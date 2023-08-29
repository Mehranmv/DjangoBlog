# Django imports
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
# local imports
from posts.models import Post


class HomePage(View):

    def get(self, request):
        postss = Post.objects.all()
        carousel_posts = postss[1:5]
        paginated = Paginator(postss, 10)
        page_number = request.GET.get('page')
        page = paginated.get_page(page_number)
        if request.GET.get('search'):
            page = postss.filter(body__contains=request.GET['search'])
        return render(request, 'home/index.html', {'postss': postss, 'page': page, 'carousel_posts': carousel_posts})


class SearchView(View):
    def get(self, request):
        search_query = request.GET.get('search')
        posts = Post.objects.filter(body__contains=search_query)
        return render(request, 'home/search.html', {'posts': posts, 'search_query': search_query})
