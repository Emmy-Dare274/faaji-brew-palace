from datetime import date, timedelta

from django.test import TestCase

from bookings.forms import BookingForm


class BookingFormValidationTest(TestCase):
    """Tests for BookingForm field-level validation rules."""

    def get_valid_data(self):
        """Return a minimal set of valid form data to reuse across tests."""
        return {
            "date": (date.today() + timedelta(days=3)).isoformat(),
            "time_slot": "19:00",
            "guest_count": 2,
            "seating_preference": "",
            "special_requests": "",
        }

    def test_form_passes_with_correct_data(self):
        """A form with all required fields filled correctly should be valid."""
        form = BookingForm(data=self.get_valid_data())
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_past_date_is_rejected(self):
        """Choosing a date in the past should fail validation."""
        data = self.get_valid_data()
        data["date"] = (date.today() - timedelta(days=1)).isoformat()
        form = BookingForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("date", form.errors)

    def test_date_beyond_60_days_is_rejected(self):
        """A date more than 60 days ahead should fail validation."""
        data = self.get_valid_data()
        data["date"] = (date.today() + timedelta(days=61)).isoformat()
        form = BookingForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("date", form.errors)

    def test_missing_time_slot_is_rejected(self):
        """Submitting the form without choosing a time slot should be rejected."""
        data = self.get_valid_data()
        data["time_slot"] = ""
        form = BookingForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("time_slot", form.errors)

    def test_special_requests_field_is_optional(self):
        """The form should pass validation when special requests is left empty."""
        data = self.get_valid_data()
        data["special_requests"] = ""
        form = BookingForm(data=data)
        self.assertTrue(form.is_valid(), msg=form.errors)
        