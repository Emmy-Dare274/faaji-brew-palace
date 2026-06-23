from django.shortcuts import render
from bookings.models import Restaurant


def index(request):
    """Render the homepage."""
    return render(request, "index.html")


def about(request):
    """
    Render the About page.
    Fetches the first Restaurant record so the Cloudinary image,
    description, and contact details are driven from the database.
    """
    restaurant = Restaurant.objects.last()
    return render(request, "about.html", {"restaurant": restaurant})
