"""
Django settings for portfolio_project project.
Pinkal Rathod – Personal Portfolio Web Application.
Configured for both local development and production hosting (Vercel / Render / Gunicorn).
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project: BASE_DIR points to root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file for local development
load_dotenv(BASE_DIR / ".env")

# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================

# Secret key: reads from environment or falls back to development key
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-pinkal-rathod-portfolio-development-key-2025"
)

# Debug mode: False by default in production, True when DEBUG=True in local .env
DEBUG = os.getenv("DEBUG", "False").strip().lower() in ("true", "1", "t", "yes")

# Allowed hosts: base localhost + hosting domains + extra env hosts
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "testserver",
    ".vercel.app",
    "profile-drab-beta.vercel.app",
    "rathodpinkal-hnfgamc7z-pinkal06.vercel.app",
]

# Support Render external hostname if deployed on Render
RENDER_HOST = os.getenv("RENDER_EXTERNAL_HOSTNAME", "").strip()
if RENDER_HOST and RENDER_HOST not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(RENDER_HOST)

# Append any custom ALLOWED_HOSTS passed via .env
extra_hosts = os.getenv("ALLOWED_HOSTS", "").strip()
if extra_hosts:
    for host in extra_hosts.split(","):
        host = host.strip()
        if host and host not in ALLOWED_HOSTS:
            ALLOWED_HOSTS.append(host)

# CSRF Trusted Origins (required for POST forms on HTTPS domains like Vercel)
CSRF_TRUSTED_ORIGINS = [
    "https://*.vercel.app",
    "https://profile-drab-beta.vercel.app",
    "https://rathodpinkal-hnfgamc7z-pinkal06.vercel.app",
    "http://127.0.0.1",
    "http://localhost",
]

if RENDER_HOST:
    render_origin = f"https://{RENDER_HOST}"
    if render_origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(render_origin)

extra_csrf = os.getenv("CSRF_TRUSTED_ORIGINS", "").strip()
if extra_csrf:
    for origin in extra_csrf.split(","):
        origin = origin.strip()
        if origin and origin not in CSRF_TRUSTED_ORIGINS:
            CSRF_TRUSTED_ORIGINS.append(origin)

# Automatically add HTTPS origin for any domain in ALLOWED_HOSTS
for host in ALLOWED_HOSTS:
    if host and not host.startswith(".") and host not in ("localhost", "127.0.0.1", "0.0.0.0", "testserver"):
        origin = f"https://{host}"
        if origin not in CSRF_TRUSTED_ORIGINS:
            CSRF_TRUSTED_ORIGINS.append(origin)

# ==============================================================================
# APPLICATION DEFINITION
# ==============================================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Custom apps
    "portfolio",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Enable WhiteNoise middleware for static file serving when installed
try:
    import whitenoise
    MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
except ImportError:
    pass

ROOT_URLCONF = "portfolio_project.urls"

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
                "django.template.context_processors.media",
                "django.template.context_processors.static",
            ],
        },
    },
]

WSGI_APPLICATION = "portfolio_project.wsgi.application"

# ==============================================================================
# DATABASE
# ==============================================================================

# Stateless in-memory SQLite database configuration
# Ensures zero disk file access, avoiding OperationalError on serverless/read-only hosts like Vercel
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Decouple session and message storage from database tables to run purely stateless
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# ==============================================================================
# PASSWORD VALIDATION
# ==============================================================================

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

# ==============================================================================
# INTERNATIONALIZATION
# ==============================================================================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

# ==============================================================================
# STATIC & MEDIA FILES
# ==============================================================================

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Use WhiteNoise to serve compressed static files safely if installed
try:
    import whitenoise
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
        },
    }
except ImportError:
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==============================================================================
# EMAIL CONFIGURATION
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ==============================================================================
# PRODUCTION SECURITY HEADERS (Active when DEBUG is False)
# ==============================================================================

if not DEBUG:
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"

    SECURE_SSL_REDIRECT = (
        os.getenv("SECURE_SSL_REDIRECT", "False").strip().lower()
        in ("true", "1", "t", "yes")
    )

    SESSION_COOKIE_SECURE = (
        os.getenv("SESSION_COOKIE_SECURE", "True").strip().lower()
        in ("true", "1", "t", "yes")
    )

    CSRF_COOKIE_SECURE = (
        os.getenv("CSRF_COOKIE_SECURE", "True").strip().lower()
        in ("true", "1", "t", "yes")
    )
