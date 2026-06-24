# Faaji & Brew Palace 🍽️

> **West African Fine Dining — Table Reservation System**

A full-stack web application built with Django that allows guests to browse a restaurant, register an account, and make, view, edit and cancel table reservations. Restaurant staff manage all bookings through a secure admin panel.

**Portfolio Project 4 — Level 5 Diploma in Full-Stack Software Development**
**Code Institute, Dublin**

---

[![Live Site](https://img.shields.io/badge/Live%20Site-Heroku-purple)](https://faaji-brew-palace-8fcdc34800ef.herokuapp.com/)

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black)](https://github.com/Emmy-Dare274/faaji-brew-palace)

**Live Site:** https://faaji-brew-palace-8fcdc34800ef.herokuapp.com/
**GitHub Repository:** https://github.com/Emmy-Dare274/faaji-brew-palace

---

## Table of Contents

1. [About the Project](#about-the-project)
2. [UX Design](#ux-design)
   - [Strategy](#strategy)
   - [User Stories](#user-stories)
   - [Wireframes](#wireframes)
   - [Design System](#design-system)
3. [Features](#features)
   - [Existing Features](#existing-features)
   - [Future Features](#future-features)
4. [Data Model](#data-model)
5. [Agile Methodology](#agile-methodology)
6. [Technologies Used](#technologies-used)
7. [Testing](#testing)
8. [Validation](#validation)
9. [Deployment](#deployment)
   - [Local Development](#local-development)
   - [Heroku Deployment](#heroku-deployment)
10. [Credits](#credits)

---

## About the Project

Faaji & Brew Palace is a fictional West African fine dining restaurant based in Lagos and London. The project was developed as a Portfolio Project 4 submission for the Code Institute Level 5 Diploma in Full-Stack Software Development.

The word **Faaji** means joy and celebration in Yoruba. That meaning is the heartbeat of this application — every design decision, from the deep purple palette to the warm gold accents, was made to reflect the warmth and richness of West African hospitality.

The application provides:

- A public-facing website with a homepage, about page and contact information
- A full user authentication system (register, login, logout) powered by django-allauth
- A complete table reservation system with full CRUD functionality
- A restaurant admin panel for staff to confirm, edit and cancel bookings
- Cloudinary-hosted imagery served from a global CDN
- A PostgreSQL database in production hosted on Neon

---

## UX Design

### Strategy

**Target Audience**

- Diners looking to book a table at a West African fine dining restaurant
- Returning guests who want to manage existing reservations
- Restaurant staff who need to manage bookings through an admin panel

**Site Goals**

1. Allow guests to register, log in and make a table reservation in under two minutes
2. Give users full control of their bookings through a personal dashboard
3. Provide restaurant staff with a powerful admin interface to manage all reservations
4. Present the brand visually in a way that reflects West African culture and luxury dining
5. Be fully accessible and responsive across all screen sizes and devices

---

### User Stories

User stories were organised into five epics. Each issue on the Kanban board maps to one or more user stories below.

#### Epic 1 — User Authentication

| # | User Story | Acceptance Criteria |
|---|---|---|
| US-01 | As a **new visitor**, I can **register an account** with my username, email, and password so that **I can make and manage reservations** | Registration form accepts username, email and password. Account is created on submit. User is redirected to My Bookings. Success message is shown. |
| US-02 | As a **returning user**, I can **log in with my credentials** so that **I can access my booking history** | Login form accepts username or email and password. On success, user is redirected to My Bookings. Success message is shown. |
| US-03 | As a **logged-in user**, I can **log out** so that **my account stays secure on shared devices** | Clicking Logout shows a confirmation page. Confirming signs the user out and redirects to homepage. Info message is shown. |

#### Epic 2 — Restaurant Information

| # | User Story | Acceptance Criteria |
|---|---|---|
| US-04 | As a **visitor**, I can **view the homepage** so that **I can learn what Faaji & Brew Palace offers** | Homepage displays a hero section, features, today's specials and a call to action. Page is fully responsive. |
| US-05 | As a **visitor**, I can **view the About page** so that **I can learn the restaurant's story and values** | About page shows restaurant story, founding narrative, Cloudinary-hosted photo, and four values cards. |
| US-06 | As a **visitor**, I can **see contact information and opening hours** so that **I can plan my visit** | Info band below the hero displays address, hours, phone and email. |

#### Epic 3 — Booking System (Full CRUD)

| # | User Story | Acceptance Criteria |
|---|---|---|
| US-07 | As a **logged-in user**, I can **make a table reservation** so that **I can secure my place at the restaurant** | Booking form at /bookings/make-booking/ accepts date (up to 60 days ahead), time slot, party size, seating preference and special requests. System auto-assigns the best available table. Success message shown on completion. |
| US-08 | As a **logged-in user**, I can **view all my bookings** so that **I can keep track of upcoming reservations** | My Bookings dashboard at /bookings/my-bookings/ lists only the logged-in user's bookings with date, time, guests and status badge. |
| US-09 | As a **logged-in user**, I can **edit an existing booking** so that **I can change the date, time or party size if my plans change** | Edit form opens pre-filled with current booking data. Changes are validated. Success message confirms update. Booking status resets to pending. |
| US-10 | As a **logged-in user**, I can **cancel a booking** so that **I can free up the table if I can no longer attend** | Clicking Cancel opens a styled confirmation modal. Confirming changes the booking status to Cancelled. Success message is shown. Card dims to indicate cancelled state. |
| US-11 | As a **logged-in user**, I receive a **confirmation message after every action** so that **I always know the outcome** | Django messages appear at the top of the page for create, edit, cancel and auth events. Messages auto-dismiss after 5 seconds. |

#### Epic 4 — Site Owner / Admin

| # | User Story | Acceptance Criteria |
|---|---|---|
| US-12 | As a **site owner**, I can **log into the admin panel** so that **I can manage all bookings across the site** | Django admin is accessible at /admin/ with superuser credentials. All three models (Restaurant, Table, Booking) appear. |
| US-13 | As a **site owner**, I can **confirm or cancel bookings in bulk** so that **I can manage the reservation queue efficiently** | BookingAdmin has custom bulk actions: Mark as Confirmed and Mark as Cancelled. |
| US-14 | As a **site owner**, I can **add, edit and delete tables** so that **the booking system reflects the real floor plan** | TableAdmin supports inline toggling of is_available without opening each record. |
| US-15 | As a **site owner**, I can **upload restaurant images** so that **the About page shows current imagery** | RestaurantAdmin has an image field backed by Cloudinary. Images upload to the CDN and display via URL on the About page. |

#### Epic 5 — UX and Defensive Design

| # | User Story | Acceptance Criteria |
|---|---|---|
| US-16 | As a **user**, I see a **styled 404 page** if I navigate to a non-existent URL so that **I am not shown a blank browser error** | Custom 404.html renders the branded error page. Back to Home button returns the user to /. |
| US-17 | As a **user**, I see a **styled 403 page** if I try to access someone else's booking so that **I understand I am not authorised** | Visiting /bookings/edit/[another user's id]/ returns a 403 Forbidden page, not a 404 or stack trace. |
| US-18 | As a **user on any device**, I can **use the full site comfortably** so that **screen size never limits my experience** | All pages render correctly at 375px (mobile), 768px (tablet) and 1280px (desktop). Bootstrap grid collapses cards to single column on small screens. |

---

### Wireframes

All wireframes were created before development began to define the page structure, user flow, and visual design of the application.

#### Home Page
![Home Page Wireframe](docs/wireframes/01_homepage.jpeg)

#### About Page
![About Page Wireframe](docs/wireframes/02_aboutpage.jpeg)

#### Register Page
![Register Wireframe](docs/wireframes/03_registerpage.jpeg)

#### Login Page
![Login Wireframe](docs/wireframes/04_loginpage.jpeg)

#### Book a Table
![Book a Table Wireframe](docs/wireframes/05_booktablepage.jpeg)

#### My Bookings Dashboard
![My Bookings Wireframe](docs/wireframes/06_my_bookingpage.jpeg)

#### Edit Booking
![Edit Booking Wireframe](docs/wireframes/07_edit_bookingpage.jpeg)

#### 404 Page
![404 Page Wireframe](docs/wireframes/08_404_page.jpeg)

---

### Design System

#### Colour Palette

The colour palette was chosen to reflect the elegance and warmth of West African culture and fine dining.

| Role | Colour | Hex |
|---|---|---|
| Primary dark (navbar, footer, dark sections) | Deep Purple | `#312A44` |
| Brand accent (buttons, icons, headings) | Warm Gold | `#C9A96E` |
| Page background | Lavender White | `#F9F5FF` |
| Interactive buttons | Muted Purple | `#88708E` |
| Navbar link text | Soft Lavender | `#DAD4DF` |

#### Typography

| Role | Font | Source |
|---|---|---|
| All headings and display text | Cormorant Garamond (Serif) | Google Fonts |
| Body text, labels, buttons | Inter (Sans-serif) | Google Fonts |

Cormorant Garamond was chosen for its elegance and heritage feel. Inter was chosen for its clarity and readability at small sizes.

---

## Features

### Existing Features

#### Navigation Bar

The navbar is fully responsive using Bootstrap 5. It collapses to a hamburger menu on mobile. The links shown depend on login state:

- **Logged out:** Home, About, Book a Table (redirects to login), Register, Login
- **Logged in:** Home, About, Book a Table, My Bookings, Logout

The brand logo includes a utensils icon with "Faaji" in warm gold and "& Brew Palace" in a softer lavender weight, styled to reflect the restaurant identity.

#### Homepage

The homepage communicates the full brand experience in one scroll:

- **Hero section** — a full-viewport restaurant interior photograph with a deep purple gradient overlay, a fluid serif heading, subheading, and two CTA buttons
- **Info band** — a narrow medium-purple strip with address, opening hours, phone and email
- **Features section** — three dark cards on the brand-purple background, each with a real photograph, a labelled tag, and a Font Awesome icon before the card title
- **Chef's Selection** — four dish cards on a near-black background, three with food photography and one drink card for the Chapman Royale signature cocktail
- **CTA band** — a dark gradient section driving new visitors to register and book

#### About Page

The About page tells the restaurant's story:

- A dark hero header with the page title and brand tagline
- A two-column story section with a Cloudinary-hosted restaurant image on the left and the founding narrative on the right
- A "Reserve Your Place" CTA button
- Four value cards (Heritage First, Community, Excellence, Sustainability) on a lavender background

#### User Authentication

Powered by django-allauth, all three auth pages use fully custom templates matching the site's design:

- **Register** — "Reserve Your Place" heading, email/username/password fields rendered with Crispy Forms
- **Login** — "Welcome Back 👋" heading with a sign-in form
- **Logout** — a styled confirmation card to prevent accidental logout

#### Book a Table

The booking form at `/bookings/make-booking/` is accessible to logged-in users only:

- User's name is shown as a read-only field (taken from account)
- Date picker limited to today through 60 days ahead
- Seven time slot choices spanning lunch (12:00–14:00) and dinner (18:00–21:00)
- Party size dropdown (1–10 guests)
- Seating preference (Indoor, Outdoor, Private Dining Room, Bar Area or No preference)
- Special requests textarea (optional)
- The system auto-assigns the best available table matching the party size and seating preference, leaving larger tables free for bigger groups

#### My Bookings Dashboard

The My Bookings page at `/bookings/my-bookings/` shows only the logged-in user's own reservations:

- Each card shows a descriptive title (e.g. "Dinner for 2 — Indoor"), date, time, guest count and status badge
- Status badges: **Confirmed** (green), **Pending Confirmation** (amber), **Cancelled** (red, card dimmed)
- **Edit** button opens the pre-filled edit form
- **Cancel** button opens a styled Bootstrap confirmation modal — no browser alert dialogs
- A "+ New Booking" button links directly to the booking form
- Empty state with a Book a Table CTA is shown when no bookings exist

#### Edit Booking

The edit form at `/bookings/edit/<id>/` opens pre-filled with all existing booking values:

- Only the booking owner can access the form — any other user receives a 403 Forbidden page
- Cancelled bookings cannot be edited — the user is redirected with an error message
- The system re-runs the table assignment logic on save, excluding the current booking from the availability check so the same slot is not blocked against itself
- Booking status resets to Pending on save so staff can reconfirm the updated reservation

#### Cancel Booking

Cancellation uses a styled Bootstrap modal rather than a browser dialog:

- One shared modal handles all booking cards on the page
- JavaScript sets the correct form action URL before the modal opens
- Cancelled bookings appear dimmed on the dashboard and cannot be edited

#### Django Messages

Every user action triggers a Django flash message:

- Register, login, logout — handled by allauth
- Create booking success / no tables available
- Edit booking success / no tables available
- Cancel booking success / already cancelled
- Attempt to edit cancelled booking

All messages appear in a styled Bootstrap alert at the top of the page and auto-dismiss after 5 seconds via JavaScript.

#### Admin Panel

Three models are registered in the Django admin with custom configuration:

- **RestaurantAdmin** — list of name, contact, hours
- **TableAdmin** — list with inline toggling of `is_available` without opening each record
- **BookingAdmin** — searchable by username/email, filterable by status and date, with bulk actions to confirm or cancel multiple bookings at once

#### Custom Error Pages

Three fully styled error pages match the site's design:

- **403 Forbidden** — shown when a user tries to access another user's booking
- **404 Not Found** — shown for any non-existent URL, with a Back to Home button
- **500 Server Error** — shown for unexpected server-side failures

All three extend the base template so the full navbar and footer are present.

### Future Features

- **Email confirmation** — send booking confirmation emails via SendGrid or Mailjet
- **Menu page** — a dedicated page listing the full restaurant menu
- **Review system** — allow diners to leave a star rating and written review after their visit
- **Availability calendar** — a visual calendar showing available and full time slots
- **SMS reminders** — send booking reminders via Twilio 24 hours before the reservation

---

## Data Model

The application uses three custom models alongside Django's built-in User model. PostgreSQL is used in production (hosted on Neon). SQLite is used locally during development.

### Entity Relationship Diagram

```
+--------------------+          +--------------------+
|       User         |          |    Restaurant      |
|  (Django built-in) |          | (site profile)     |
+--------------------+          +--------------------+
| id (PK)            |          | id (PK)            |
| username           |          | name               |
| email              |          | description        |
| password           |          | address            |
+--------------------+          | phone              |
         |                      | email              |
         | 1                    | opening_time       |
         |                      | closing_time       |
         | M                    | image (Cloudinary) |
         |                      +--------------------+
+--------------------+
|      Booking       |          +--------------------+
+--------------------+          |      Table         |
| id (PK)            |  M    1  +--------------------+
| user (FK → User)   |----------| id (PK)            |
| table (FK → Table) |          | table_number       |
| date               |          | capacity           |
| time_slot          |          | location           |
| guest_count        |          | is_available       |
| special_requests   |          +--------------------+
| status             |
| created_on         |
| updated_on         |
+--------------------+
```

### Model Details

#### Restaurant

Stores the restaurant's public profile. Only one record is expected in production and it is managed via the admin panel. The `image` field is a CloudinaryField that stores the public ID of an uploaded image; the full CDN URL is generated on request via `.url`.

#### Table

Represents a physical table on the restaurant floor. The `capacity` field is used during booking to find a table that can seat the requested party size. The `is_available` boolean allows staff to take a table offline for maintenance without deleting it or its booking history.

#### Booking

The core model that records a user's reservation. Key design decisions:

- `time_slot` uses `CharField` with choices instead of a `TimeField`, making the user experience a dropdown of named time slots rather than a time input
- A `UniqueConstraint` on `(table, date, time_slot)` enforces no double bookings at the database level
- A `clean()` method adds model-level validation for past dates, capacity breaches, and out-of-service tables — this runs in both the admin and on the front-end form
- Status uses named class constants (`STATUS_PENDING`, `STATUS_CONFIRMED`, `STATUS_CANCELLED`) so any comparison in views or templates is protected against typos

### Database

| Environment | Database | Details |
|---|---|---|
| Local development | SQLite | File-based database at `db.sqlite3`. Not committed to git. |
| Production (Heroku) | PostgreSQL | Hosted on [Neon](https://neon.tech/). Connected via `DATABASE_URL` environment variable. Managed with `dj-database-url`. |

---

## Agile Methodology

This project was planned and developed using Agile methodology with a GitHub Projects Kanban board.

**Kanban Board:** https://github.com/users/Emmy-Dare274/projects/3/views/1

The project was broken into 18 GitHub Issues, each representing a discrete piece of work. Issues were grouped into the following logical phases:

| Phase | Issues | Description |
|---|---|---|
| Setup | #1 – #4 | Project creation, settings, early Heroku deployment, allauth setup |
| Models | #5 | Restaurant, Table and Booking models with admin registration |
| Auth Templates | #6 | Custom login, signup and logout pages |
| Pages | #7 – #8 | Homepage and About page |
| Booking CRUD | #9 – #11 | Booking form, My Bookings dashboard, edit booking with 403 protection |
| JavaScript | #12 | Auto-dismiss messages and cancel confirmation modal |
| Error Pages | #13 | Custom 403, 404 and 500 error pages |
| UX Polish | #14 – #15 | Django messages, manual and automated testing |
| Validation | #16 | PEP8, W3C HTML/CSS, JSHint, Lighthouse |
| Deployment | #17 | Final Heroku deployment with all checks |
| Documentation | #18 | README |

Each issue was written with a User Story and a list of Acceptance Criteria. Issues were moved from **To Do** → **In Progress** → **Done** on the Kanban board as work progressed.

---

## Technologies Used

### Frontend
- **HTML5** — semantic page structure using `<section>`, `<article>`, `<nav>`, `<main>` and `<footer>` elements
- **CSS3** — custom styling and responsive layout with the BEM-influenced class naming
- **JavaScript (ES6)** — auto-dismiss flash messages, Bootstrap modal interaction, form action injection
- **Bootstrap 5.0.1** — responsive grid system, components (modals, alerts, dropdowns) and utility classes
- **Crispy Forms + crispy-bootstrap5** — Django form rendering styled with Bootstrap 5
- **Font Awesome 6.5.1** — icon library for UI icons throughout the site
- **Google Fonts** — Cormorant Garamond (headings) and Inter (body text)

### Backend
- **Python 3.12** — primary programming language
- **Django 6.0.6** — full-stack web framework using the MVT (Model-View-Template) pattern
- **Django Allauth 65.18** — user registration, login, logout and account management
- **Gunicorn 26.0** — WSGI HTTP server for production deployment on Heroku
- **WhiteNoise 6.12** — static file serving in production with cache headers and compression

### Database
- **PostgreSQL** — production relational database hosted on [Neon](https://neon.tech/)
- **SQLite** — local development file-based database (not committed to git)
- **dj-database-url 0.5** — parses the `DATABASE_URL` environment variable into Django's `DATABASES` setting
- **psycopg2 2.9.11** — PostgreSQL adapter for Python

### Cloud and Storage
- **Cloudinary** — cloud media storage for the restaurant profile image, served via global CDN
- **django-cloudinary-storage** — integrates Cloudinary as Django's default file storage backend

### Deployment and Version Control
- **Heroku** — cloud platform hosting the live application on the Heroku-24 stack
- **Git** — version control with descriptive commit messages referencing issue numbers
- **GitHub** — remote repository and project Kanban board hosting

### Development Tools
- **VS Code** — primary code editor
- **Chrome DevTools** — responsive design testing, Lighthouse audits, JavaScript debugging
- **CI Python Linter** — PEP8 compliance checking at https://pep8ci.herokuapp.com/
- **W3C Nu HTML Checker** — HTML validation at https://validator.w3.org/nu/
- **W3C Jigsaw CSS Validator** — CSS validation at https://jigsaw.w3.org/css-validator/
- **JSHint** — JavaScript quality checking at https://jshint.com/

---

## Testing

A full breakdown of manual test cases, automated test results, responsiveness testing, browser compatibility and bugs found and fixed is documented separately.

<details>
<summary>Click to view the Testing document</summary>

The complete testing write-up is in [TESTING.md](TESTING.md).

It covers:
- 24 manual test cases across auth, CRUD, navigation and error pages
- 19 automated Django tests covering models, forms and views (all passing in 15–20 seconds)
- Responsiveness tested at 375px, 768px and 1280px
- Browser compatibility on Chrome, Edge and Firefox
- 5 bugs found during development with their root causes and fixes documented

</details>

---

## Validation

### Python — PEP8 (CI Python Linter)

All Python files were checked using the [Code Institute Python Linter](https://pep8ci.herokuapp.com/) and returned zero errors.

| File | Result |
|---|---|
| bookings/models.py | ![models](docs/validation/py/CI-PythonLinter-bookings-model-result.jpg) |
| bookings/views.py | ![views](docs/validation/py/CI-PythonLinter-bookings-view-result.jpg) |
| bookings/forms.py | ![forms](docs/validation/py/CI-PythonLinter-bookings-forms-result.jpg) |
| bookings/admin.py | ![admin](docs/validation/py/CI-PythonLinter-bookings-admin-result.jpg) |
| bookings/urls.py | ![urls](docs/validation/py/CI-PythonLinter-bookings-urls-result.jpg) |
| bookings/tests/test_models.py | ![test models](docs/validation/py/CI-PythonLinter-bookings-tests-test_models-result.jpg) |
| bookings/tests/test_forms.py | ![test forms](docs/validation/py/CI-PythonLinter-bookings-tests-test_forms-result.jpg) |
| bookings/tests/test_views.py | ![test views](docs/validation/py/CI-PythonLinter-bookings-tests-test_views-result.jpg) |
| faaji_brew/settings.py | ![settings](docs/validation/py/CI-PythonLinter-faaji_brew-settings-result.jpg) |
| faaji_brew/urls.py | ![faaji urls](docs/validation/py/CI-PythonLinter-faaji_brew-urls-result.jpg) |
| faaji_brew/views.py | ![faaji views](docs/validation/py/CI-PythonLinter-faaji_brew-views-result.jpg) |
| about/views.py | ![about views](docs/validation/py/CI-PythonLinter-about-views-result.jpg) |
| about/urls.py | ![about urls](docs/validation/py/CI-PythonLinter-about-urls-result.jpg) |

---

### HTML — W3C Validator

All pages were validated using the [W3C Nu HTML Checker](https://validator.w3.org/nu/).

| Page | Result |
|---|---|
| Homepage | ![home](docs/validation/w3c/W3Chtml-validation-home.jpg) |
| About | ![about](docs/validation/w3c/W3Chtml-validation-about.jpg) |
| Login | ![login](docs/validation/w3c/W3Chtml-validation-account-login.jpg) |
| Logout | ![logout](docs/validation/w3c/W3Chtml-validation-account-logout.jpg) |
| Sign Up | ![signup](docs/validation/w3c/W3Chtml-validation-account-signup.jpg) |
| Book a Table | ![booking form](docs/validation/w3c/W3Chtml-validation-bookings-makebooking.jpg) |
| My Bookings | ![my bookings](docs/validation/w3c/W3Chtml-validation-mybookings-bookings.jpg) |

---

### CSS — W3C Jigsaw Validator

![CSS Validation](docs/validation/w3c/W3C-CSS-Validator-full-result.jpg)

---

### JavaScript — JSHint

![JSHint Result](docs/validation/w3c/JSHint-JavaScript-Code-result.jpg)

---

### Lighthouse

Lighthouse audits were run on the deployed Heroku site using Chrome DevTools.

| Page | Result |
|---|---|
| Homepage | ![lighthouse home](docs/validation/lighthouse/lighthouse-home.png) |
| About | ![lighthouse about](docs/validation/lighthouse/lighthouse-about.png) |
| Book a Table | ![lighthouse booking](docs/validation/lighthouse/lighthouse-booking.png) |

---

### Responsive Design

Tested across multiple screen sizes using Chrome DevTools Device Toolbar.

![Desktop](docs/validation/responsive/Faaji-Brew-Palace-desktop-view.jpg)
![iPad](docs/validation/responsive/Faaji-Brew-Palace-ipad-view.jpg)
![iPhone](docs/validation/responsive/Faaji-Brew-Palace-iphones-view.jpg)
![Other phones](docs/validation/responsive/Faaji-Brew-Palace-otherphones-view.jpg)

---

## Deployment

### Local Development

To run this project locally, follow these steps.

**Prerequisites:** Python 3.12, Git, a Cloudinary account

**1. Clone the repository**

```bash
git clone https://github.com/Emmy-Dare274/faaji-brew-palace.git
cd faaji-brew-palace
```

**2. Create and activate a virtual environment**

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac / Linux
python -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Create `env.py` in the project root**

This file stores sensitive credentials and must never be committed to git.
It is already listed in `.gitignore`.

```python
import os

os.environ["SECRET_KEY"] = "your-django-secret-key"
os.environ["CLOUDINARY_URL"] = "cloudinary://api_key:api_secret@cloud_name"
# DATABASE_URL is not needed locally — the app falls back to SQLite
```

**5. Run database migrations**

```bash
python manage.py migrate
```

**6. Create a superuser for the admin panel**

```bash
python manage.py createsuperuser
```

**7. Start the development server**

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

---

### Heroku Deployment

The live site was deployed to Heroku using the Heroku Dashboard. These steps reproduce that deployment from scratch.

**1. Create a Heroku app**

Log in to [heroku.com](https://heroku.com), create a new app, and choose a region.

**2. Provision a PostgreSQL database**

This project uses [Neon](https://neon.tech/) for PostgreSQL. Create a free Neon project, copy the connection string, and add it as a Heroku Config Var named `DATABASE_URL`.

Alternatively, the Heroku Postgres add-on can be used instead.

**3. Set Config Vars**

In the Heroku Dashboard under **Settings → Config Vars**, add the following:

| Key | Value |
|---|---|
| `SECRET_KEY` | A long, random secret key |
| `DATABASE_URL` | PostgreSQL connection string (from Neon or Heroku Postgres) |
| `CLOUDINARY_URL` | Cloudinary connection URL from your Cloudinary dashboard |
| `PORT` | `8000` |

**4. Connect to GitHub**

In the **Deploy** tab, choose **GitHub** as the deployment method. Search for the repository and connect it. Enable **Automatic Deploys** from the `main` branch.

**5. Deploy**

Click **Deploy Branch** to trigger the first build. Heroku will:
- Detect Python
- Install dependencies from `requirements.txt`
- Run `python manage.py collectstatic --noinput` (WhiteNoise collects static files)
- Start Gunicorn via the Procfile

**6. Run migrations on Heroku**

Use the Heroku Dashboard console (**More → Run console**):

```bash
python manage.py migrate
```

**7. Create a superuser on Heroku**

```bash
python manage.py createsuperuser
```

**8. Add initial data via the admin**

Visit `https://your-app.herokuapp.com/admin/` and add:
- At least one **Restaurant** record (with name, hours, and a Cloudinary image)
- At least one **Table** record (with table number, capacity and location)

The booking system will not work without at least one available table in the database.

---

### Environment Variables Reference

| Variable | Description | Required |
|---|---|---|
| `SECRET_KEY` | Django secret key for cryptographic signing | Yes |
| `DATABASE_URL` | PostgreSQL connection string | Yes (production) |
| `CLOUDINARY_URL` | Cloudinary API URL for media uploads | Yes |
| `PORT` | Port for Gunicorn (Heroku sets this automatically) | Optional |

---

## Credits

### Code and Learning Resources

- **[John Elder — Codemy.com](https://codemy.com/)** — John's Django and Python courses provided invaluable guidance for me throughout this project. His teaching style made Django's MVT pattern, authentication flows, and database design approachable and practical. The depth of his Full-Stack Django course content shaped how this project was structured and built.

- **[Code Institute](https://codeinstitute.net/)** — The LMS course material, walkthrough projects (especially CodeStar Blog), and the structured curriculum for Portfolio Project 4 provided me with the foundation for this build.

- **[Code Institute Full-Stack Discord Community](https://discord.gg/codeinstitute)** — The peer support and collaboration from the Code Institute Full-Stack channel was invaluable. Community members helped debug code, provided feedback, and kept the motivation high throughout the project. Special thanks to everyone who responded to me on time during stuck moments.

- **[Django Documentation](https://docs.djangoproject.com/)** — The official Django 6.x documentation was referenced throughout for models, views, forms, authentication, and deployment.

- **[Django Allauth Documentation](https://docs.allauth.org/)** — Used for implementing the full authentication system with allauth 65.x syntax.

- **[Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.0/)** — Referenced for the grid system, components and utility classes used throughout the frontend.

- **[WhiteNoise Documentation](https://whitenoise.readthedocs.io/)** — Used for configuring static file serving in production.

### Media

All photography used on the Faaji & Brew Palace website was sourced from **[Unsplash](https://unsplash.com/)**, a platform offering high-quality, freely usable images under the [Unsplash License](https://unsplash.com/license).

| Image | Usage |
|---|---|
| Restaurant interior (hero photo) | Homepage hero background |
| West African egusi dish | Cuisine feature card |
| Live brass band performance | Live Music feature card |
| Elegant dining room | Private Dining feature card |
| Jollof rice plating | Chef's Selection special |
| Beef suya skewers | Chef's Selection special |
| Puff puff dough balls | Chef's Selection special |
| Red hibiscus drink | Chapman Royale special |

The restaurant image on the About page was uploaded directly by the site owner via the Cloudinary-backed admin panel.

### Icons

- **[Font Awesome 6.5.1](https://fontawesome.com/)** — All icons used throughout the site (utensils, calendar, clock, users, etc.)

### Fonts

- **[Google Fonts](https://fonts.google.com/)** — Cormorant Garamond (serif, headings) and Inter (sans-serif, body text)

### Tools

- **[BGJar](https://bgjar.com/colored-shapes)** — Explored for the geometric shapes background concept used in early wireframe planning
- **[Neon](https://neon.tech/)** — PostgreSQL database hosting in production
- **[Heroku](https://heroku.com/)** — Cloud deployment platform

### Acknowledgements

This project was completed as part of my **Level British 5 Diploma in Full-Stack Software Development** at **Code Institute, Dublin**. The support of the Code Institute tutors, mentors, account department, and student community throughout this diploma has been outstanding.

---

*Faaji & Brew Palace — Where Every Meal Is a Faaji*

*by: Emmanuel Oluwadare — Code Institute Portfolio Project 4 — 2026*
