"""
Django settings for monsite project.

Usage:
  # Local (default)
  set DJANGO_ENV=local   # Windows CMD
  $env:DJANGO_ENV="local" # PowerShell
  export DJANGO_ENV=local # macOS/Linux

  # Production
  export DJANGO_ENV=prod
"""

from pathlib import Path
import os

# --------------------
# Base paths
# --------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------
# Environment
# --------------------
ENV = os.getenv("DJANGO_ENV", "local").lower()   # "local" (default) or "prod"
DEBUG = os.getenv("DJANGO_DEBUG", "1" if ENV != "prod" else "0") in ("1", "true", "True")
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "dev-only-secret-key-change-in-prod"
)

# --------------------
# Hosts & CSRF
# --------------------
if ENV == "prod":
    ALLOWED_HOSTS = ["youssef.bazzaoui.com"]
    CSRF_TRUSTED_ORIGINS = ["https://youssef.bazzaoui.com"]
else:
    # Local development: allow localhost + LAN IP (optional)
    ALLOWED_HOSTS = ["127.0.0.1", "localhost","192.168.11.117","youssef.bazzaoui.com"]
    # Add your LAN IP below if testing on phone, e.g. 192.168.1.12
    LAN_IP = os.getenv("LAN_IP")
    if LAN_IP:
        ALLOWED_HOSTS.append(LAN_IP)
    CSRF_TRUSTED_ORIGINS = [
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ] + ([f"http://{LAN_IP}:8000"] if LAN_IP else [])

# --------------------
# Installed apps / middleware
# --------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "base",
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

ROOT_URLCONF = "monsite.urls"

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

WSGI_APPLICATION = "monsite.wsgi.application"

# --------------------
# Database (SQLite by default)
# --------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --------------------
# Password validation
# --------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------
# I18N
# --------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --------------------
# Static & Media
# --------------------
STATIC_URL = "static/"

# Source static folders (used in dev; collected into STATIC_ROOT for prod)
STATICFILES_DIRS = []
candidate = BASE_DIR / "staticfiles"
if candidate.exists():
    STATICFILES_DIRS.append(candidate)

# Where collectstatic puts files (useful for deployment)
STATIC_ROOT = BASE_DIR / "staticfiles_collected"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# --------------------
# Default primary key
# --------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
