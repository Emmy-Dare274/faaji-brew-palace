# Testing — Faaji & Brew Palace

## Contents

1. [Manual Testing](#manual-testing)
2. [Automated Testing](#automated-testing)
3. [Responsiveness Testing](#responsiveness-testing)
4. [Browser Compatibility](#browser-compatibility)
5. [Bugs Found and Fixed](#bugs-found-and-fixed)

---

## Manual Testing

All manual tests were carried out on the live Heroku deployment at
https://faaji-brew-palace-8fcdc34800ef.herokuapp.com/ and locally at
http://127.0.0.1:8000/ with DEBUG=False.

### Authentication

| ID | Feature | Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| A01 | User Registration | Visit /accounts/signup/, fill in username, email and password, click Create Account | Account created, redirected to My Bookings, success message shown | As expected | ✅ Pass |
| A02 | User Login | Visit /accounts/login/, enter credentials, click Sign In | Redirected to My Bookings, success message shown | As expected | ✅ Pass |
| A03 | User Logout | Click Logout in navbar, confirm on logout page | Redirected to homepage, info message shown, navbar shows Login and Register | As expected | ✅ Pass |
| A04 | Login Required — Booking Form | While logged out, visit /bookings/make-booking/ | Redirected to login page | As expected | ✅ Pass |
| A05 | Login Required — My Bookings | While logged out, visit /bookings/my-bookings/ | Redirected to login page | As expected | ✅ Pass |
| A06 | 403 Ownership Protection | Log in as User B and visit /bookings/edit/[User A booking ID]/ | Styled 403 Forbidden error page shown | As expected | ✅ Pass |

### Booking — Create

| ID | Feature | Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| C01 | Valid Booking Submission | Log in, visit Book a Table, fill all fields with valid data, click Confirm Reservation | Booking created, redirected to My Bookings, green success message shown | As expected | ✅ Pass |
| C02 | Past Date Rejected | In the booking form, type a date from yesterday, click Confirm Reservation | Form re-renders with date validation error message | As expected | ✅ Pass |
| C03 | Date Beyond 60 Days Rejected | Enter a date 61 days ahead, click Confirm Reservation | Form re-renders with date validation error message | As expected | ✅ Pass |
| C04 | Missing Time Slot | Leave time slot as Select time, click Confirm Reservation | Form re-renders with time slot error message | As expected | ✅ Pass |
| C05 | No Tables Available | Fill in a date and time where all tables are booked, click Confirm Reservation | Form re-renders with red error message explaining no availability | As expected | ✅ Pass |

### Booking — Read

| ID | Feature | Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| R01 | My Bookings Loads | Log in, click My Bookings in navbar | Page renders with all personal bookings listed | As expected | ✅ Pass |
| R02 | Data Isolation | Log in as User B, visit My Bookings | Only User B's own bookings are visible, not User A's | As expected | ✅ Pass |
| R03 | Empty State | Log in with a new account that has no bookings | Empty state message shown with a Book a Table button | As expected | ✅ Pass |
| R04 | Status Badges | Check My Bookings with pending, confirmed and cancelled bookings | Correct coloured badge shown for each status | As expected | ✅ Pass |

### Booking — Update

| ID | Feature | Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| U01 | Edit Form Pre-populated | Click Edit on a booking | Edit form opens with all existing values already filled in | As expected | ✅ Pass |
| U02 | Valid Edit Saves Changes | Change the date, click Save Changes | Booking updated, redirected to My Bookings, success message shown | As expected | ✅ Pass |
| U03 | Edit Cancelled Booking | Click Edit on a cancelled booking | Redirected to My Bookings with error message, no form shown | As expected | ✅ Pass |
| U04 | Cancel Changes Button | Open edit form, click Cancel Changes | Redirected back to My Bookings with no changes saved | As expected | ✅ Pass |

### Booking — Delete (Cancel)

| ID | Feature | Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| D01 | Cancel Modal Appears | Click Cancel on a booking in My Bookings | Styled dark confirmation modal appears, not a browser dialog | As expected | ✅ Pass |
| D02 | Keep My Booking Button | Click Cancel, then click Keep My Booking in modal | Modal closes, booking status unchanged | As expected | ✅ Pass |
| D03 | Confirm Cancel | Click Cancel, then click Yes Cancel It in modal | Booking status changes to Cancelled, card dims, success message shown | As expected | ✅ Pass |

### Error Pages

| ID | Feature | Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| E01 | 404 Page | Visit any non-existent URL on Heroku | Styled 404 page with Back to Home button shown | As expected | ✅ Pass |
| E02 | 403 Page | Visit another user's edit URL | Styled 403 page with Back to Home button shown | As expected | ✅ Pass |

### Navigation and UX

| ID | Feature | Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| N01 | Navbar — Logged Out | Visit the site while not logged in | Navbar shows Home, About, Book a Table, Register, Login | As expected | ✅ Pass |
| N02 | Navbar — Logged In | Log in | Navbar shows Home, About, Book a Table, My Bookings, Logout | As expected | ✅ Pass |
| N03 | Flash Message Auto-dismiss | Perform any action that triggers a message | Message appears and fades away automatically after 5 seconds | As expected | ✅ Pass |
| N04 | About Page Image | Visit /about/ on Heroku | Cloudinary restaurant image renders in the story section | As expected | ✅ Pass |

---

## Automated Testing

Automated tests were written using Django's built-in TestCase framework.
The test suite covers models, forms and views across 13 individual test cases.

### Running the Tests

```bash
python manage.py test bookings --verbosity=2
```

### Test Results
The form should pass validation when special requests is left empty. ... ok
test_booking_str_contains_username_and_table_number (bookings.tests.test_models.BookingModelTest.test_booking_str_contains_username_and_table_number)
__str__ should include the guest username and the table number. ... ok
test_double_booking_same_slot_raises_integrity_error (bookings.tests.test_models.BookingModelTest.test_double_booking_same_slot_raises_integrity_error)
The unique constraint should prevent two bookings for the same table, date and slot. ... ok
test_new_booking_defaults_to_pending_status (bookings.tests.test_models.BookingModelTest.test_new_booking_defaults_to_pending_status)
A booking created without an explicit status should default to pending. ... ok
test_table_is_available_by_default (bookings.tests.test_models.TableModelTest.test_table_is_available_by_default)
A newly created table should be marked as available without setting it manually. ... ok
test_table_str_returns_expected_string (bookings.tests.test_models.TableModelTest.test_table_str_returns_expected_string)
__str__ should include table number, capacity and location label. ... ok
test_cancel_booking_sets_status_to_cancelled (bookings.tests.test_views.BookingViewsTest.test_cancel_booking_sets_status_to_cancelled)
POSTing to cancel_booking should update the booking status to cancelled. ... C:\Users\Emmanuel Oluwadare\Desktop\project4\faaji-brew-palace\.venv\Lib\site-packages\django\core\handlers\base.py:62: UserWarning: No directory at: C:\Users\Emmanuel Oluwadare\Desktop\project4\faaji-brew-palace\staticfiles\
  mw_instance = middleware(adapted_handler)
ok
test_edit_booking_get_renders_prepopulated_form (bookings.tests.test_views.BookingViewsTest.test_edit_booking_get_renders_prepopulated_form)
GET to edit_booking should return the edit template for the booking owner. ... ok
test_make_booking_get_renders_form_for_logged_in_user (bookings.tests.test_views.BookingViewsTest.test_make_booking_get_renders_form_for_logged_in_user)
A logged-in GET request should render the booking form template. ... ok
test_make_booking_redirects_anonymous_user (bookings.tests.test_views.BookingViewsTest.test_make_booking_redirects_anonymous_user)
An anonymous visitor to the booking form should be sent to login. ... ok
test_my_bookings_only_returns_logged_in_users_bookings (bookings.tests.test_views.BookingViewsTest.test_my_bookings_only_returns_logged_in_users_bookings)
The My Bookings page must never show another user's reservations. ... ok
test_my_bookings_redirects_anonymous_user (bookings.tests.test_views.BookingViewsTest.test_my_bookings_redirects_anonymous_user)
An anonymous visitor to My Bookings should be sent to login. ... ok
test_other_user_cannot_cancel_another_users_booking (bookings.tests.test_views.BookingViewsTest.test_other_user_cannot_cancel_another_users_booking)
A cancel attempt on another user's booking should be blocked silently. ... ok
test_other_user_editing_booking_returns_403 (bookings.tests.test_views.BookingViewsTest.test_other_user_editing_booking_returns_403)
A user trying to edit someone else's booking should receive a 403. ... ok
test_valid_post_creates_booking_and_redirects_to_dashboard (bookings.tests.test_views.BookingViewsTest.test_valid_post_creates_booking_and_redirects_to_dashboard)
Valid POST data should create one booking and redirect to My Bookings. ... ok

----------------------------------------------------------------------


Ran 19 tests in 20.006s

OK
