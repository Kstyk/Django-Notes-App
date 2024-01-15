from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from notes.views import home_view

urlpatterns = [
    path('/', home_view, name="home"),
    path('home/', home_view, name="home"),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
