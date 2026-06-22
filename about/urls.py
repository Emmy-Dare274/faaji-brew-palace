# URL patterns for the about app.
# The homepage is served at the root URL.

from django.urls import path
from . import views

app_name = "about"

urlpatterns = [
    path("", views.index, name="index"),
]
