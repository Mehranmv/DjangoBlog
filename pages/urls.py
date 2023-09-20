from django.urls import path, re_path
from . import views

app_name = 'pages'
urlpatterns = [
    path('aboutus/', views.AboutUsView.as_view(), name='aboutus'),
    path('contactus/', views.ContactUsView.as_view(), name='contactus'),
    path('rules/', views.RulesView.as_view(), name='rules'),
    path('questions/', views.QuestionsView.as_view(), name='question'),

]
