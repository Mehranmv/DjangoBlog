# django imports
from django.urls import path, re_path
from django.contrib.sitemaps.views import sitemap
# local imports
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('search/', views.SearchView.as_view(), name='search'),

]
