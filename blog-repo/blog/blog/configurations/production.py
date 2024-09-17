from .base import *

DEBUG = False


ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'dominio-produccion.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_sqlite3',

        #POSTGRESQL
        #'ENGINE': 'django.db.backends.postgresql'

        #'NAME': os.getenv('DB_NAME'),
        #'USER': os.getenv('DB_USER'),
        #'PASSWORD': os.getenv('DB_PASSWORD'),
        #'HOST': os.getenv('DB_HOST'),
        #'PORT': os.getenv('DB_PORT'),

    }
}

os.environ['DJANGO_PORT'] = '1952' #8000 #8080