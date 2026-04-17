from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("account.urls")),
    path("api/", include("property.urls")),
    path("api/", include("member.urls")),
    path("api/", include("contract.urls")),
]
