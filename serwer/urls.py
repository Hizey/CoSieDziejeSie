from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("wydarzenia.urls")),
    path("tinymce/", include("tinymce.urls")),
]
