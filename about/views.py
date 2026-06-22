from django.shortcuts import render

# Create your views here.

def index(request):
    """Render the homepage."""
    return render(request, "index.html")
