from django.contrib import admin
from django.urls import path, include
from kach_static_pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home-page"),
    path('api/', include('kach_api_endpoints.urls')),
    path('backend/', include('kach_backend_endpoints.urls')),
]
