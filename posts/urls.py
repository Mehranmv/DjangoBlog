from django.urls import re_path, path
from . import views

app_name = 'posts'
urlpatterns = [
    re_path(r'category/(?P<category_slug>[-\w]+)/', views.CategoryView.as_view(), name='category'),
    re_path(r'detail/(?P<post_slug>[-\w]+)/', views.PostDetailView.as_view(), name='post_detail'),
    re_path(r'reply/(?P<post_slug>[-\w]+)/(?P<comment_id>[-\w]+)', views.CommentReplyView.as_view(), name='comment_reply'),

]
