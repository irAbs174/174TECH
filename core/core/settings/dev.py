from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-l-^5l=mfc3qbp)5pg=&x%()-@oo6cswt2b9a!p^i%k3deaa5m!"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["8000-irabs174-174tech-mjztw4iznm2.ws-eu107.gitpod.io"]

CSRF_TRUSTED_ORIGINS = ["https://8000-irabs174-174tech-mjztw4iznm2.ws-eu107.gitpod.io"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
