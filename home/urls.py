# django imports
from django.urls import path, re_path
from django.contrib.sitemaps.views import sitemap
# local imports
from . import views
from .sitemaps import PostSitemap

app_name = 'home'
sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', views.HomePage.as_view(), name='home_page'),
    path('search/', views.SearchView.as_view(), name='search'),
    #re_path(r'menu/(?P<menu_slug>[-\w]+)/', views.HomePage.as_view(), name='category'),

]
