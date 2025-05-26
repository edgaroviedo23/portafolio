from pathlib import Path
import os
import dj_database_url
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

# Email settings - usa variables de entorno para que Railway funcione correctamente
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config("EMAIL_HOST", default='smtp.gmail.com')
EMAIL_PORT = config("EMAIL_PORT", cast=int, default=587)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool, default=True)
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default=EMAIL_HOST_USER)

print("EMAIL_HOST_USER:", EMAIL_HOST_USER)  # Solo para debug, quita luego
print("EMAIL_HOST_PASSWORD seteada?:", EMAIL_HOST_PASSWORD is not None)

SECRET_KEY = 'django-insecure-*k#f_z^*3q8$$pq4qe9tgg06u12*j$mk=d5&1^d-vm+ec$xzmp'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'rest_framework',
    'django_filters',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'miportafolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'miportafolio.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL', default=''))
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_COOKIE_AGE = 60 * 60 * 24 * 14
SESSION_SAVE_EVERY_REQUEST = False
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:8000']

CSRF_TRUSTED_ORIGINS = ["https://*.railway.app"]
