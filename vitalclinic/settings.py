# vitalclinic/settings.py
from pathlib import Path

# -----------------------------
# BASE DIRECTORY
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# SECRET KEY (obligatorio)
# -----------------------------
SECRET_KEY = 'django-insecure-4z$k&2v8t9y!m^1#q7a@p5s+f0w*e(3l)b&j2h6u1y0g^#x!'  # para desarrollo

# -----------------------------
# DEBUG / HOSTS
# -----------------------------
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# -----------------------------
# INSTALLED APPS
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Terceros
    'rest_framework',
    'rest_framework_simplejwt',

    # Tus apps
    'appointments',
    'patients',
    'professionals',
    'pqrs',
]

# -----------------------------
# MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',            # obligatorio
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',         # obligatorio
    'django.contrib.messages.middleware.MessageMiddleware',            # obligatorio
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------
# ROOT URLCONF
# -----------------------------
ROOT_URLCONF = 'vitalclinic.urls'

# -----------------------------
# TEMPLATES
# -----------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'appointments' / 'templates'],  # templates dentro de appointments
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

# -----------------------------
# WSGI
# -----------------------------
WSGI_APPLICATION = 'vitalclinic.wsgi.application'

# -----------------------------
# DATABASE (SQLite para desarrollo)
# -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------
# PASSWORD VALIDATORS
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# -----------------------------
# INTERNACIONALIZACIÓN
# -----------------------------
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -----------------------------
# STATIC FILES
# -----------------------------
STATIC_URL = '/static/'

# -----------------------------
# REST FRAMEWORK
# -----------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
