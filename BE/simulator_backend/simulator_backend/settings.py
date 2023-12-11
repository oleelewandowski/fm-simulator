"""
Ustawienia Django dla projektu simulator_backend.

Wygenerowane przez 'django-admin startproject' używając Django 4.2.7.

Aby uzyskać więcej informacji na temat tego pliku, zobacz
https://docs.djangoproject.com/en/4.2/topics/settings/

Pełna lista ustawień i ich wartości znajduje się na
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from corsheaders.defaults import default_headers

# Budowanie ścieżek wewnątrz projektu, na przykład: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Szybkie ustawienia rozwojowe - nieodpowiednie dla produkcji
# Zobacz https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = 'django-insecure-atfh-g9+z%lnv5r-l-)2m_94jfbf#)8#n!t&om#l6ky1(o7^lg'

# OSTRZEŻENIE O BEZPIECZEŃSTWIE: nie uruchamiaj z włączonym debugowaniem w produkcji!
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ["*"]


# Definicja aplikacji

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # aplikacja fm_simulator
    'corsheaders',
    'fm_simulator'
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
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://fm-simulator-oleelewandowski.vercel.app"
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'contenttype',
]

ROOT_URLCONF = 'simulator_backend.urls'

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

WSGI_APPLICATION = 'simulator_backend.wsgi.application'


# Baza danych
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Walidacja haseł
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internacjonalizacja
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Pliki statyczne (CSS, JavaScript, Obrazy)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL='static/'
STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Domyślny typ głównego klucza
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
