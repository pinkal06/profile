# SECURITY SETTINGS

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-pinkal-rathod-portfolio-development-key-2025"
)

DEBUG = os.getenv("DEBUG", "False").strip().lower() in (
    "true", "1", "t", "yes"
)

# Allowed hosts: Localhost + Hosting domain
ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        "ALLOWED_HOSTS",
        "127.0.0.1,localhost"
    ).split(",")
    if host.strip()
]

# Automatically allow the Render domain, if deployed on Render
RENDER_HOST = os.getenv("RENDER_EXTERNAL_HOSTNAME", "").strip()

if RENDER_HOST and RENDER_HOST not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(RENDER_HOST)

# CSRF trusted origins for forms and login
CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
]

if RENDER_HOST:
    render_origin = f"https://{RENDER_HOST}"
    if render_origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(render_origin)
