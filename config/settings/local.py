from ..base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'root',
        'USER': '29494*',
        'HOST': 'localhost',  # set in docker-compose.yml
        'PORT': 3306  # default postgres port
    }
}