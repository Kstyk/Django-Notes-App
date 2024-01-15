from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from notes.views import home

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home_path"),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
