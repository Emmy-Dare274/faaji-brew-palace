# Faaji & Brew Palace 🍽️
I created this project in order to pass the Code Institute Portfolio Project 4: Full-Stack Django Restaurant Booking System.

**A full-stack restaurant booking system built with Django.**

A Portfolio Project 4 submission for the Level 6 Diploma in Full-Stack Software Development at Code Institute, Dublin.

---

## Project Overview

Faaji & Brew Palace is a full-stack web application that allows users to browse a 
restaurant, register an account, and make, view, edit and cancel table reservations. 
Site owners can manage all bookings via a secure admin panel.

**Live Site:** [Live View — deployed to Heroku](https://faaji-brew-palace-8fcdc34800ef.herokuapp.com/)  
**GitHub Repository:** https://github.com/Emmy-Dare274/faaji-brew-palace


## UX Design


### Wireframes

The following wireframes were created prior to development to define the page 
structure, user flow, and visual design of the application.


---

## Technologies Used


### Frontend
- **HTML5** — semantic page structure
- **CSS3** — custom styling and responsive layout
- **JavaScript** — DOM manipulation, flash message dismissal, delete confirmation modal
- **Bootstrap 5** — responsive grid, components and utility classes
- **Crispy Forms** — Django form rendering styled with Bootstrap 5

### Backend
- **Python 3** — primary programming language
- **Django 4** — full-stack web framework (MVT architecture)
- **Django Allauth** — user registration, login and logout
- **Gunicorn** — WSGI HTTP server for Heroku deployment
- **Whitenoise** — static file serving in production

### Database
- **PostgreSQL** — production relational database (hosted on Neon)
- **SQLite** — local development database
- **dj-database-url** — database URL configuration for Django

### Cloud and Deployment
- **Cloudinary** — cloud media storage for uploaded images
- **Heroku** — cloud platform for live deployment
- **Git and GitHub** — version control and repository hosting

---


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



## Testing

A full breakdown of manual test cases, automated test results, responsiveness
testing, browser compatibility and bugs found and fixed is documented separately.

<details>
<summary>Click to view the Testing document</summary>

The complete testing write-up is in [TESTING.md](TESTING.md).

It covers:
- 24 manual test cases across auth, CRUD, navigation and error pages
- 19 automated Django tests covering models, forms and views (all passing)
- Responsiveness tested at 375px, 768px and 1280px
- Browser compatibility on Chrome, Edge and Firefox
- 5 bugs found during development with their fixes documented

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

