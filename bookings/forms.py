from datetime import date, timedelta
from django import forms
from .models import Booking


class BookingForm(forms.Form):
    """
    Booking form shown to logged-in users at /bookings/make-booking/.

    seating_preference is not stored directly on the Booking model.
    The view uses it to filter available tables and assigns the best
    match automatically, so guests never have to pick a table number.
    """

    PARTY_SIZE_CHOICES = [
        (i, f"{i} guest{'s' if i > 1 else ''}") for i in range(1, 11)
    ]

    SEATING_CHOICES = [
        ("", "No preference"),
        ("indoor", "Indoor"),
        ("outdoor", "Outdoor"),
        ("private", "Private Dining Room"),
        ("bar", "Bar Area"),
    ]

    date = forms.DateField(
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control",
        }),
        error_messages={
            "required": "Please choose a date for your visit.",
        },
    )

    time_slot = forms.ChoiceField(
        choices=[("", "Select time")] + list(Booking.TIME_SLOT_CHOICES),
        widget=forms.Select(attrs={"class": "form-select"}),
        error_messages={
            "required": "Please select a time slot.",
        },
    )

    guest_count = forms.TypedChoiceField(
        choices=PARTY_SIZE_CHOICES,
        coerce=int,
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    seating_preference = forms.ChoiceField(
        choices=SEATING_CHOICES,
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    special_requests = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 4,
            "placeholder": (
                "Dietary requirements, anniversary setup, high chair needed..."
            ),
        }),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = date.today()
        max_date = today + timedelta(days=60)
        self.fields["date"].widget.attrs.update({
            "min": today.isoformat(),
            "max": max_date.isoformat(),
        })

    def clean_date(self):
        chosen = self.cleaned_data["date"]
        today = date.today()
        if chosen < today:
            raise forms.ValidationError(
                "Bookings cannot be made for a date that has already passed."
            )
        if chosen > today + timedelta(days=60):
            raise forms.ValidationError(
                "Bookings can only be made up to 60 days in advance."
            )
        return chosen

    def clean_time_slot(self):
        slot = self.cleaned_data.get("time_slot")
        if not slot:
            raise forms.ValidationError("Please select a time slot.")
        return slot
