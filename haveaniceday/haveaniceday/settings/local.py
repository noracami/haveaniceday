from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd^qxcml3(^-h3)m@2^!95ct5((vvu&hkv62mgrj%yn0&amg&8!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
