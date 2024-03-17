
from .base import *

DEBUG = False

ADMIN = (
    ('Chisom', 'marcusjobng@gmail.com'),
    ('Admin', 'info@ommcsl.loan')
)

ALLOWED_HOSTS = ['*']

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'ommscl$ommcslmain',
        'USER' : 'ommscl',
        'PASSWORD' : 'Newdata12@',
        'HOST' : 'ommscl.mysql.pythonanywhere-services.com',
        'OPTIONS' : {
            'sql_mode' : 'traditional'
            }
    }
}