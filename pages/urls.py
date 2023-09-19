from django.urls import path, re_path
from . import views

app_name = 'pages'
urlpatterns = [
    re_path(r'(?P<page_slug>[-\w]+)/', views.AboutUsView.as_view(), name='comment_reply'),

]
