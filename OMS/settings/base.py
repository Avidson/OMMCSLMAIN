"""
Django settings for OMS project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/

"""
#from dotenv import load_dotenv
from pathlib import Path
import os
#from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(os.path.join(__file__, os.pardir)).resolve().parent.parent

#load_dotenv()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'django-secure-=nnf0109&^0rnk9wgvy!=ky8-(1ca0s(c(z5x8gw&9lh9*&8un'
#SECRET_KEY = config('SECRET_KEY')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'api',
    'main',
    'Membership',
    'payment',
    'Loan_Request',
    'Loan_Approval',
    'Share',
    'Monthly_due',
    'inAppDonations',
    'branches',
    'ads',
    'feedback',
    'ecommerce',
    'cart',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'widget_tweaks',
    'weasyprint',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'OMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS = (

    'django.core.context_processors.request',
    'cart.context_processors.cart',
)

WSGI_APPLICATION = 'OMS.wsgi.application'


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/")
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

#session for each task and transaction performed
SESSION_EXPIRE_AT_BROWSER_CLOSE: False
SESSION_COOKIE_AGE = 5*60
SESSION_SAVE_EVERY_REQUEST = True

#Sess
CART_SESSION_ID = 'cart'

#PAYSTACK PAYMENT DETAILS
PAYSTACK_SECRETE_KEY = 'sk_live_2c1dfd180392538dd795a79c46b1429392885113'
PAYSTACK_PUBLIC_KEY = 'pk_live_15fe3dca92002ca013afc08756003e61f0e17970'
PAYSTACK_INITIALIZE_PAYMENT_URL = 'https://api.paystack.co/transaction/initialize'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



DEFAULT_AUTHENTICATION_CLASSES = [
    'rest_framework.authentication.TokenAuthentication'
]


REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [
   'rest_framework.permissions.AllowAny',
]

}

USE_THOUSAND_SEPARATOR = True

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'csunny200@gmail.com'

EMAIL_HOST_PASSWAORD = 'Cityboy12@'

EMAIL_PORT = 587

EMAIL_USE_TLS = True


#sending mail via django's console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'