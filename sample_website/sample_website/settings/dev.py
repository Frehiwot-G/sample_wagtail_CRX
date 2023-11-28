from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "@g-18o$qma#-xkgetq85ysiz=6d2$0!gndp_(@czey1t6@aqf*"

# ALLOWED_HOSTS = ["2two.uk", "65.21.144.205"]
ALLOWED_HOSTS = ["*"]


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WAGTAIL_CACHE = False

try:
    from .local import *  # noqa
except ImportError:
    pass
