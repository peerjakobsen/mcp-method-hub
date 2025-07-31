from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

# Use SQLite for local testing (when PostgreSQL is not available)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Simple cache for local testing
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

# Email backend for development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
