"""
Settings
========
Module contains settings for this projects.

I try to keep this module as simple and minimal as possible
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY', 'password123')

#: Indicates if this project is running in developer mode
DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = []

CSRF_USE_SESSIONS = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'djoser',

    'money',
    'parser',
    'geo_data',
    'discount',
    'discount_tracker'
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

ROOT_URLCONF = 'bus_travel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'bus_travel', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bus_travel.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3')},
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
        ),
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

LANGUAGE_CODE = 'en-us'

#: This setting allows clean urls for static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'bus_travel', 'static'),
    # This is needed to serve svg icons for flags-css
    os.path.join(BASE_DIR, '..', 'node_modules', 'flag-icon-css', 'flags')
)
#: This tells Django that all static files should be awailable from
#: /static/ url
STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s [%(asctime)s] (%(name)s) %(message)s'
        },
        'simple': {'format': '%(levelname)s %(message)s'},
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'propagate': True,
        },
        'parser': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'service': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'geo_data': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

#: Custom setting object for storing access to Mapzen api serivce.
#: Mainly I use this api service as fallback alternative to Opencage
#: service, so when Opencage fails I can try get info from this guy.
# TODO: Need to cleanup this part, to not duplicate yourself
MAPZEN_API = {
    'name': 'Mapzen',
    'url': 'https://search.mapzen.com/v1/search/structured',
    'key': os.environ.get('MAPZEN_API_KEY'),
    'timeout': .5,
    'query_keyword': 'locality',
    'api_keyword': 'api_key',
    'extra': {},
}
#: Custom setting object for storing access to Opencage api serivce.
#: Important part here is ``extra`` object containing geo bounds
#: that allow forward geo seraching be more fast and specific
OPENCAGE_API = {
    'name': 'OpenCage',
    'url': 'https://api.opencagedata.com/geocode/v1/json',
    'key': os.environ.get('OPENCAGE_API_KEY'),
    'timeout': 1,
    'query_keyword': 'q',
    'api_keyword': 'key',
    'extra': {
        # We need only basic info
        'no_annotations': 1,
        'limit': 1,
        # Searching only Europe
        'bounds': '-10.546875,36.4919734706,42.1875,71.2302205238',
    }
}
