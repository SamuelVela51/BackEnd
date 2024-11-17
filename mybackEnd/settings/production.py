from .common import *
from .partials.util import get_secret

DEBUG = True
DEBUG_TOOLBAR = True

ALLOWED_HOSTS = ['*']
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

# ADMINS (For error notifications)
ADMINS = [
    ('Brayan', 'destroyergarzon@gamil.com'),
]



if get_secret('DATABASE_URL'):
    import dj_database_url

    DATABASES = {
        'default': dj_database_url.config()
    }
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'
else:
    POSTGRES_USER = get_secret('POSTGRES_USER')
    POSTGRES_PASSWORD = get_secret('POSTGRES_PASSWORD')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'goal-wear',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
    }


SPECTACULAR_SETTINGS['SERVERS'] = [{"url": "http://localhost:8000"}]

API_FIREBASE_KEY = os.environ.get('API_FIREBASE_KEY', '')



