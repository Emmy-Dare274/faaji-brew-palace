from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from bookings.models import Booking, Table

User = get_user_model()


class BookingViewsTest(TestCase):
    """
    Tests for all booking views.

    setUp creates two users, one table and one booking so every test
    starts from a clean, realistic state without repeating boilerplate.
    """

    def setUp(self):
        # Primary user who owns the test booking
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )
        # Second user used only to verify ownership protection
        self.other_user = User.objects.create_user(
            username="otheruser",
            password="testpass123",
        )
        # A table the view can assign when processing a new booking
        self.table = Table.objects.create(
            table_number=1,
            capacity=4,
            location=Table.LOCATION_INDOOR,
            is_available=True,
        )
        # An existing booking owned by the primary user
        self.booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            date=date.today() + timedelta(days=7),
            time_slot="19:00",
            guest_count=2,
            status=Booking.STATUS_PENDING,
        )

    def test_make_booking_redirects_anonymous_user(self):
        """An anonymous visitor to the booking form should be sent to login."""
        response = self.client.get(reverse("bookings:make_booking"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response["Location"])

    def test_my_bookings_redirects_anonymous_user(self):
        """An anonymous visitor to My Bookings should be sent to login."""
        response = self.client.get(reverse("bookings:my_bookings"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response["Location"])

    def test_make_booking_get_renders_form_for_logged_in_user(self):
        """A logged-in GET request should render the booking form template."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("bookings:make_booking"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookings/make_booking.html")

    def test_valid_post_creates_booking_and_redirects_to_dashboard(self):
        """
        Valid POST data should create one booking
        and redirect to My Bookings.
        """
        self.client.login(username="testuser", password="testpass123")
        count_before = Booking.objects.filter(user=self.user).count()
        response = self.client.post(
            reverse("bookings:make_booking"),
            {
                "date": (date.today() + timedelta(days=10)).isoformat(),
                "time_slot": "20:00",
                "guest_count": 2,
                "seating_preference": "",
                "special_requests": "",
            },
        )
        self.assertRedirects(response, reverse("bookings:my_bookings"))
        self.assertEqual(
            Booking.objects.filter(user=self.user).count(), count_before + 1
        )

    def test_my_bookings_only_returns_logged_in_users_bookings(self):
        """The My Bookings page must never show another user's reservations."""
        Booking.objects.create(
            user=self.other_user,
            table=self.table,
            date=date.today() + timedelta(days=20),
            time_slot="18:00",
            guest_count=1,
        )
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("bookings:my_bookings"))
        self.assertEqual(response.status_code, 200)
        for booking in response.context["bookings"]:
            self.assertEqual(booking.user, self.user)

    def test_cancel_booking_sets_status_to_cancelled(self):
        """
        POSTing to cancel_booking should update
        the booking status to cancelled.
        """
        self.client.login(username="testuser", password="testpass123")
        self.client.post(
            reverse("bookings:cancel_booking", args=[self.booking.id])
        )
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, Booking.STATUS_CANCELLED)

    def test_other_user_editing_booking_returns_403(self):
        """
        A user trying to edit someone else's booking
        should receive a 403.
        """
        self.client.login(username="otheruser", password="testpass123")
        response = self.client.get(
            reverse("bookings:edit_booking", args=[self.booking.id])
        )
        self.assertEqual(response.status_code, 403)

    def test_other_user_cannot_cancel_another_users_booking(self):
        """
        A cancel attempt on another user's booking
        should be blocked silently.
        """
        self.client.login(username="otheruser", password="testpass123")
        self.client.post(
            reverse("bookings:cancel_booking", args=[self.booking.id])
        )
        self.booking.refresh_from_db()
        # Status must remain pending because the cancel was denied
        self.assertEqual(self.booking.status, Booking.STATUS_PENDING)

    def test_edit_booking_get_renders_prepopulated_form(self):
        """
        GET to edit_booking should return the edit template
        for the booking owner.
        """
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(
            reverse("bookings:edit_booking", args=[self.booking.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookings/edit_booking.html")
