from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from kach_static_pages import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('admin/', admin.site.urls),
    path('api/', include('kach_api_endpoints.urls')),
    path('backend/', include('kach_backend_endpoints.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
