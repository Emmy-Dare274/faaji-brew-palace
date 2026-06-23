"""
URL configuration for faaji_brew project.
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("bookings/", include("bookings.urls")),
    path("", include("about.urls")),
]


handler404 = "faaji_brew.views.handler404"
handler500 = "faaji_brew.views.handler500"
handler403 = "faaji_brew.views.handler403"

