import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME', os.getenv('DB_NAME')),
        'USER': os.getenv('DB_USER', os.getenv('DB_USER')),
        'PASSWORD': os.getenv('DB_PASSWORD', os.getenv('DB_PASSWORD')),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

MEDIA_ROOT = (os.path.join(BASE_DIR, 'media'))
MEDIA_URL = "/media/"

STATIC_ROOT = Path(BASE_DIR).joinpath('static')
