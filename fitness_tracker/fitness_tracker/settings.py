"""
Django settings for fitness_tracker project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e26cvpcl5%(m&22&qh)1(3g1v&xny8szb3kwwv+m*9!x(k0%)^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['fitwithme.onrender.com', 'http://localhost:3000/', '16.171.79.44:8000']

CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'clients',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Runs first
    'fitness_tracker.middleware.ImpersonateUserMiddleware',  # Runs after AuthenticationMiddleware
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'fitness_tracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Add this line
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
"""
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default backend
    'fitness_tracker.backends.ImpersonationAuthBackend',  # Your new backend
]
"""
WSGI_APPLICATION = 'fitness_tracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fitness_tracker',
        'USER': 'root',
        'PASSWORD': '225588',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
"""
"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fitwithmelis',
        'USER': 'fitwithmelis',
        'PASSWORD': '225588jds',
        'HOST': 'fitwithmelis.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
"""
"""
#local
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fitness_tracker',          # Database name
        'USER': 'fitwithmelis',             # Database user
        'PASSWORD': '225588db',             # Database password
        'HOST': 'localhost',                # Database host
        'PORT': '5432',                     # PostgreSQL default port
    }
}

#render
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fitness_tracker_uowk',          # Database name
        'USER': 'fitwithmelis',             # Database user
        'PASSWORD': 'VgWFQ9njfSyxaUwpUUVAiIKABtBKE417',             # Database password
        'HOST': 'dpg-cuk1l9qj1k6c73d3dfs0-a',                # Database host
        'PORT': '5432',                     # PostgreSQL default port
    }
}
"""
#AWS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fitwithmelisdb',          # Database name
        'USER': 'fitwithmelis',             # Database user
        'PASSWORD': '225588db',             # Database password
        'HOST': 'localhost',                # Database host
        'PORT': '',                     # PostgreSQL default port
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = 'static/'
STATIC_URL = '/static/'


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Create the static directory if it doesn't exist
STATIC_DIR = os.path.join(BASE_DIR, 'static')
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)

STATICFILES_DIRS = [STATIC_DIR]

SESSION_COOKIE_SECURE = True
# Static files (CSS, JavaScript, Images)

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




CORS_ALLOWED_ORIGINS = [
    'https://fitwithme.onrender.com', 'http://localhost:3000', 'http://16.171.79.44',
]

CSRF_TRUSTED_ORIGINS = [
    'https://fitwithme.onrender.com', 'http://localhost:3000', 'http://16.171.79.44',
]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'https://fitwithme.onrender.com', 'http://localhost:3000', 'http://16.171.79.44',  # Your React app URL
]

CORS_EXPOSE_HEADERS = ['Set-Cookie']
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'impersonate-user',
]



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

#CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins (for development only)


from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),  # Extend access token lifetime to 24 hours
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),   # Extend refresh token lifetime to 7 days
    'ROTATE_REFRESH_TOKENS': True,                # Allow refresh tokens to be rotated
    'BLACKLIST_AFTER_ROTATION': True,             # Blacklist old refresh tokens after rotation
}

