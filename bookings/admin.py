"""
Admin configuration for the bookings app.

Booking, Table, and Restaurant are registered here with list views,
filters, search, and bulk actions that make daily management straightforward
for restaurant staff without requiring any code changes.
"""

from django.contrib import admin

from .models import Booking, Restaurant, Table


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """Admin view for the restaurant profile."""

    list_display = ("name", "phone", "email", "opening_time", "closing_time")


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    Admin view for managing tables.
    is_available can be toggled directly from the list without opening each record.
    """

    list_display = ("table_number", "capacity", "location", "is_available")
    list_filter = ("location", "is_available")
    list_editable = ("is_available",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin view for all reservations.

    Staff can search by guest name or email, filter by date or status,
    and use the bulk actions to confirm or cancel multiple bookings at once.
    """

    list_display = (
        "user",
        "table",
        "date",
        "time_slot",
        "guest_count",
        "status",
        "created_on",
    )
    list_filter = ("status", "date", "table__location")
    search_fields = ("user__username", "user__email")
    date_hierarchy = "date"
    ordering = ("-date", "time_slot")
    readonly_fields = ("created_on", "updated_on")
    actions = ["confirm_bookings", "cancel_bookings"]

    @admin.action(description="Mark selected bookings as Confirmed")
    def confirm_bookings(self, request, queryset):
        """Bulk action: confirm selected bookings."""
        count = queryset.update(status=Booking.STATUS_CONFIRMED)
        self.message_user(request, f"{count} booking(s) marked as confirmed.")

    @admin.action(description="Mark selected bookings as Cancelled")
    def cancel_bookings(self, request, queryset):
        """Bulk action: cancel selected bookings."""
        count = queryset.update(status=Booking.STATUS_CANCELLED)
        self.message_user(request, f"{count} booking(s) cancelled.")
        