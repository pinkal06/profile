
"""
Django settings for portfolio_project project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file for local development
load_dotenv(BASE_DIR / ".env")

# Secret key
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-pinkal-rathod-portfolio-development-key-2025"
)

# Debug mode: False by default for production
DEBUG = os.getenv("DEBUG", "False").lower() in (
    "true", "1", "t", "yes"
)

# Allowed hosts
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "rathodpinkal-hnfgamc7z-pinkal06.vercel.app",
]

# Allow additional Vercel domains through environment variables
extra_hosts = os.getenv("ALLOWED_HOSTS", "")
for host in extra_hosts.split(","):
    host = host.strip()
    if host and host not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(host)

# Applications
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "portfolio",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "portfolio_project.urls"

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    "https://rathodpinkal-hnfgamc7z-pinkal06.vercel.app",
]

extra_origins = os.getenv("CSRF_TRUSTED_ORIGINS", "")
for origin in extra_origins.split(","):
    origin = origin.strip()
    if origin and origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(origin)

# Templates
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

WSGI_APPLICATION = "portfolio_project.wsgi.application"

# Database: SQLite
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise static files storage
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email configuration
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Production security
if not DEBUG:
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"

    SECURE_SSL_REDIRECT = (
        os.getenv("SECURE_SSL_REDIRECT", "False").lower()
        in ("true", "1", "t", "yes")
    )

    SESSION_COOKIE_SECURE = (
        os.getenv("SESSION_COOKIE_SECURE", "True").lower()
        in ("true", "1", "t", "yes")
    )

    CSRF_COOKIE_SECURE = (
        os.getenv("CSRF_COOKIE_SECURE", "True").lower()
        in ("true", "1", "t", "yes")
    )
