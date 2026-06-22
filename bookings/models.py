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

#  Bookings models
class Booking(models.Model):
    """
    Records a table reservation made by a registered user.

    A booking links a User, a Table, a date, and a time slot.
    The UniqueConstraint on (table, date, time_slot) prevents two bookings
    from claiming the same table at the same time.
    """

    # Time slots covering lunch and dinner service at Faaji & Brew Palace
    TIME_SLOT_CHOICES = [
        ("12:00", "12:00 PM  —  Lunch"),
        ("13:00", "1:00 PM"),
        ("14:00", "2:00 PM"),
        ("18:00", "6:00 PM  —  Dinner"),
        ("19:00", "7:00 PM"),
        ("20:00", "8:00 PM"),
        ("21:00", "9:00 PM  —  Last Seating"),
    ]

    # Named constants make status comparisons readable throughout the code
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    date = models.DateField()
    time_slot = models.CharField(
        max_length=5,
        choices=TIME_SLOT_CHOICES,
    )
    guest_count = models.PositiveIntegerField(
        help_text="Total number of guests including the person booking",
    )
    special_requests = models.TextField(
        blank=True,
        default="",
        help_text="Dietary requirements, celebrations, or any other notes for the kitchen",
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    # Timestamps are set automatically and cannot be edited
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        # Most recent bookings appear first in any queryset
        ordering = ["-date", "time_slot"]
        constraints = [
            # One booking per table per date per time slot
            models.UniqueConstraint(
                fields=["table", "date", "time_slot"],
                name="unique_table_date_timeslot",
            )
        ]

    def clean(self):
        """
        Model-level validation called by full_clean().

        These checks run when saving through the admin panel as well as
        through the booking form, so data integrity is enforced at both layers.
        """
        today = timezone.now().date()

        # Reject bookings set in the past
        if self.date and self.date < today:
            raise ValidationError(
                {"date": "Bookings cannot be made for a date that has already passed."}
            )

        # Guest count must not exceed the physical capacity of the table
        if self.table_id and self.guest_count:
            if self.guest_count > self.table.capacity:
                raise ValidationError(
                    {
                        "guest_count": (
                            f"This table seats up to {self.table.capacity} guests. "
                            f"You requested {self.guest_count}. "
                            f"Please choose a larger table or reduce your party size."
                        )
                    }
                )

        # Block new bookings on a table that staff have taken offline
        if self.table_id and not self.table.is_available:
            raise ValidationError(
                {"table": "This table is currently out of service. Please choose another."}
            )

    def __str__(self):
        return (
            f"{self.user.username} — Table {self.table.table_number} "
            f"on {self.date} at {self.get_time_slot_display()}"
        )
        