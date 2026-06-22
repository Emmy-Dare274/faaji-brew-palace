"""
Models for the Faaji & Brew Palace booking system.

Three models work together:
  Restaurant  -- stores the restaurant's public profile (name, hours, contact info)
  Table       -- represents each physical table on the floor
  Booking     -- records a user reservation tied to a table on a specific date and time
"""

from cloudinary.models import CloudinaryField
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

#  Restaurant models
class Restaurant(models.Model):
    """
    Stores the restaurant's public profile.
    A single record is expected in production and is managed from the admin panel.
    Staff can update the description, contact details, and hero image without
    touching any code.
    """

    name = models.CharField(max_length=100)
    description = models.TextField(
        help_text="A short summary shown on the About page"
    )
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    opening_time = models.TimeField(
        help_text="Daily opening time, for example 12:00"
    )
    closing_time = models.TimeField(
        help_text="Daily closing time, for example 22:00"
    )
    # Hero image is stored in Cloudinary and served via CDN
    image = CloudinaryField("image", blank=True, null=True)

    def __str__(self):
        return self.name

#  Table models
class Table(models.Model):
    """
    Represents a physical table inside the restaurant.

    capacity sets the hard limit on guest_count at booking time.
    is_available is toggled by staff to mark a table out of service
    without deleting its booking history.
    """

    LOCATION_INDOOR = "indoor"
    LOCATION_OUTDOOR = "outdoor"
    LOCATION_PRIVATE = "private"
    LOCATION_BAR = "bar"

    LOCATION_CHOICES = [
        (LOCATION_INDOOR, "Indoor"),
        (LOCATION_OUTDOOR, "Outdoor"),
        (LOCATION_PRIVATE, "Private Dining Room"),
        (LOCATION_BAR, "Bar Area"),
    ]

    table_number = models.PositiveIntegerField(
        unique=True,
        help_text="Unique number identifying this table on the floor plan",
    )
    capacity = models.PositiveIntegerField(
        help_text="Maximum number of guests this table can seat",
    )
    location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        default=LOCATION_INDOOR,
    )
    # Staff can take a table offline for maintenance without removing it
    is_available = models.BooleanField(
        default=True,
        help_text="Uncheck to temporarily remove this table from the booking flow",
    )

    class Meta:
        ordering = ["table_number"]

    def __str__(self):
        return (
            f"Table {self.table_number} "
            f"(seats {self.capacity}, {self.get_location_display()})"
        )

