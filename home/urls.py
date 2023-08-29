from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap

app_name = 'home'
sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', views.HomePage.as_view(), name='home_page'),
    path('search/', views.SearchView.as_view(), name='search')

]
