from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookingForm
from .models import Booking, Table


@login_required
def make_booking(request):
    """
    Show the booking form and handle submission.

    On POST the view finds the best available table matching the
    guest count and seating preference, then creates the Booking.
    The user never has to choose a table number themselves.
    """
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            chosen_date = form.cleaned_data["date"]
            time_slot = form.cleaned_data["time_slot"]
            guest_count = form.cleaned_data["guest_count"]
            seating_pref = form.cleaned_data["seating_preference"]
            special_requests = form.cleaned_data["special_requests"]

            # Find tables already taken for this date and time slot
            taken_ids = Booking.objects.filter(
                date=chosen_date,
                time_slot=time_slot,
                status__in=[Booking.STATUS_PENDING, Booking.STATUS_CONFIRMED],
            ).values_list("table_id", flat=True)

            # Start with all available tables that fit the party
            available = Table.objects.filter(
                is_available=True,
                capacity__gte=guest_count,
            ).exclude(id__in=taken_ids)

            # Apply seating preference if one was given
            if seating_pref:
                preferred = available.filter(location=seating_pref)
                # Fall back to any available table if preference yields nothing
                available = preferred if preferred.exists() else available

            # Pick the smallest table that fits to leave larger ones free
            table = available.order_by("capacity").first()

            if not table:
                messages.error(
                    request,
                    "No tables are available for your chosen date, time, and party "
                    "size. Please try a different combination.",
                )
            else:
                Booking.objects.create(
                    user=request.user,
                    table=table,
                    date=chosen_date,
                    time_slot=time_slot,
                    guest_count=guest_count,
                    special_requests=special_requests,
                    status=Booking.STATUS_PENDING,
                )
                messages.success(
                    request,
                    "Your reservation has been received. We will confirm "
                    "within 2 hours. See you soon!",
                )
                return redirect("bookings:my_bookings")
    else:
        form = BookingForm()

    return render(request, "bookings/make_booking.html", {"form": form})


@login_required
def my_bookings(request):
    """
    Show all reservations belonging to the logged-in user,
    most recent date first.
    """
    user_bookings = Booking.objects.filter(
        user=request.user
    ).order_by("-date", "time_slot")

    return render(
        request,
        "bookings/my_bookings.html",
        {"bookings": user_bookings},
    )


@login_required
def cancel_booking(request, booking_id):
    """
    Mark a booking as cancelled. Only the owner can cancel their own booking.
    Accepts POST only to prevent accidental cancellation via a shared link.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        if booking.status != Booking.STATUS_CANCELLED:
            booking.status = Booking.STATUS_CANCELLED
            booking.save()
            messages.success(request, "Your booking has been cancelled.")
        else:
            messages.info(request, "This booking is already cancelled.")

    return redirect("bookings:my_bookings")
