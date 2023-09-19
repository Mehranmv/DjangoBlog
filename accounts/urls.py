from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path("history/", views.HistoryView.as_view(), name='history'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('bookmark_posts/', views.BookmarkView.as_view(), name='user_bookmark'),
    path('vip/', views.VipView.as_view(), name='vip'),
    path('membership/buy/<int:id>/', views.BuyMembershipView.as_view(), name='buy_vip'),
    path('membership/payment-callback/', views.PaymentCallbackView.as_view(), name='membership-payment-callback'),
]
