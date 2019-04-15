from ..base import *

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'qcount',
#         'USER': 'root',
#         'PASSWORD': '29494*',
#         'HOST': 'localhost',  # set in docker-compose.yml
#         'PORT': 3306  # default postgres port
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database.sqlite'),
    }
}