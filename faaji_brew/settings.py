""" Settings for the Faaji & Brew Palace Django project.

# Sensitive values are read from environment variables via env.py locally
# and from Heroku Config Vars in production.
"""

import os
import dj_database_url
from pathlib import Path

# Import env.py only if it exists, for local development only
if os.path.isfile("env.py"):
    import env

# Root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key is stored in env.py locally and in Heroku Config Vars in production
SECRET_KEY = os.environ.get("SECRET_KEY")

# Set to True only during local development, always False in production
DEBUG = True

# Hosts allowed to serve this application
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".herokuapp.com",
]

# All installed apps including Django core, third party and local apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "cloudinary",
    "cloudinary_storage",
    "crispy_forms",
    "crispy_bootstrap5",
    "whitenoise.runserver_nostatic",
    "bookings",
    "about",
]

# Required by django-allauth
SITE_ID = 1

# Middleware runs on every request and response cycle
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "faaji_brew.urls"

# Template configuration points to the root level templates folder
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "faaji_brew.wsgi.application"

# Database configuration
# Uses PostgreSQL in production via DATABASE_URL environment variable
# Falls back to SQLite for local development if DATABASE_URL is not set
DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation rules for user accounts
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalisation settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files configuration
# STATICFILES_DIRS is where custom CSS and JS live during development
# STATIC_ROOT is where collectstatic gathers everything for production
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Cloudinary handles all uploaded media files in production
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")

# Default primary key type for all models
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Authentication backends allow both standard login and allauth login
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Where to redirect users after login and logout
LOGIN_REDIRECT_URL = "/bookings/my-bookings/"
LOGOUT_REDIRECT_URL = "/"

# Allauth account settings
# Email verification is disabled for development to keep things simple
# Allauth account settings for version 65+
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGIN_METHODS = {"username", "email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "username*", "password1*", "password2*"]


# Crispy forms uses Bootstrap 5 for all form rendering
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Map Django message levels to Bootstrap 5 alert classes
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}
