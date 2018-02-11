DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookmarked_db',
                'USER': 'bookmarked_user',
                'PASSWORD': 'PASSWORD',     #Replace DATABASE_PASSWORD with the password you set when you create the database.
                'HOST': 'localhost',
    },
}

ALLOWED_HOSTS = ['bookmarked.site']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
