from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('', include('pages.urls', namespace='pages')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
