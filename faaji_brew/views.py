"""
Custom error handlers for faaji_brew project.
"""

from django.shortcuts import render


def handler404(request, exception):
    """Handle 404 Page Not Found errors."""
    return render(request, "404.html", status=404)


def handler500(request):
    """Handle 500 Internal Server errors."""
    return render(request, "500.html", status=500)


def handler403(request, exception):
    """Handle 403 Forbidden errors raised by PermissionDenied."""
    return render(request, "403.html", status=403)
