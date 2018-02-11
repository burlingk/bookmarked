import os
from django.conf import settings





BASE_DIR=settings.BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['*']




# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
