from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase

from bookings.models import Booking, Table

User = get_user_model()


class TableModelTest(TestCase):
    """Tests for the Table model's string output and default field values."""

    def setUp(self):
        self.table = Table.objects.create(
            table_number=1,
            capacity=4,
            location=Table.LOCATION_INDOOR,
        )

    def test_table_str_returns_expected_string(self):
        """__str__ should include table number, capacity and location label."""
        self.assertEqual(str(self.table), "Table 1 (seats 4, Indoor)")

    def test_table_is_available_by_default(self):
        """
        A newly created table should be marked as available
        without setting it manually.
        """
        self.assertTrue(self.table.is_available)


class BookingModelTest(TestCase):
    """
    Tests for the Booking model's string output,
    defaults and constraints.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )
        self.table = Table.objects.create(
            table_number=1,
            capacity=4,
            location=Table.LOCATION_INDOOR,
        )
        self.booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            date=date.today() + timedelta(days=7),
            time_slot="19:00",
            guest_count=2,
            status=Booking.STATUS_PENDING,
        )

    def test_booking_str_contains_username_and_table_number(self):
        """__str__ should include the guest username and the table number."""
        result = str(self.booking)
        self.assertIn("testuser", result)
        self.assertIn("1", result)

    def test_new_booking_defaults_to_pending_status(self):
        """
        A booking created without an explicit status
        should default to pending.
        """
        new_booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            date=date.today() + timedelta(days=14),
            time_slot="20:00",
            guest_count=2,
        )
        self.assertEqual(new_booking.status, Booking.STATUS_PENDING)

    def test_double_booking_same_slot_raises_integrity_error(self):
        """
        The unique constraint should prevent two bookings
        for the same table, date and slot.
        """
        with self.assertRaises(IntegrityError):
            Booking.objects.create(
                user=self.user,
                table=self.table,
                date=self.booking.date,
                time_slot=self.booking.time_slot,
                guest_count=2,
            )
