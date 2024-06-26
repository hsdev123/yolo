from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("data.urls")),
    path('api/', include('rest_framework.urls')),
    path("admin/", admin.site.urls),
]
