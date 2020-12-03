from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('kach_api_endpoints.urls')),
    path('backend/', include('kach_backend_endpoints.urls'))
]
