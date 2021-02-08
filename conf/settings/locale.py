import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'd2k%2rlr1r&y2d7_q6=jet9r7r9u+%ebdu9m2)f-_9@vob)b0k'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME', 'vitapc'),
        'USER': os.getenv('DB_USER', 'vitapc'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'vitapc'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

MEDIA_ROOT = (os.path.join(BASE_DIR, 'media'))
MEDIA_URL = "/media/"

STATIC_ROOT = Path(BASE_DIR).joinpath('static')

from conf.settings.base import *