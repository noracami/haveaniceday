from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8h11kg44!o2*tt%7oo0yvou0o&)3#$&11z8=9ia0)*z=d8y_%+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
