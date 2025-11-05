import os
from pathlib import Path

from django.conf import settings

# =========================
# BASE DO PROJETO
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# SEGURANÇA
# =========================
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'sua_chave_secreta_local')
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "leafeat-backend-1.onrender.com",  # produção
]

# =========================
# APPS INSTALADOS
# =========================
INSTALLED_APPS = [
    'corsheaders',  # CORS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # REST
    'rest_framework',

    # Apps do projeto
    'usuarios',
    'restaurantes',
]

# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # sempre primeiro
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =========================
# URLS & TEMPLATES
# =========================
ROOT_URLCONF = 'leafeat_backend.urls'

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

WSGI_APPLICATION = 'leafeat_backend.wsgi.application'

# =========================
# BANCO DE DADOS
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DB_NAME'),
        'USER': os.environ.get('DJANGO_DB_USER'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD'),
        'HOST': os.environ.get('DJANGO_DB_HOST'),
        'PORT': os.environ.get('DJANGO_DB_PORT'),
    }
}

# =========================
# AUTENTICAÇÃO
# =========================
AUTH_USER_MODEL = 'usuarios.Usuario'
AUTHENTICATION_BACKENDS = [
    'usuarios.auth_backends.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# =========================
# CORS
# =========================
if DEBUG:
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]
else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://leaf-eat\.vercel\.app$",
    ]

if not settings.DEBUG:
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://leaf-eat\.vercel\.app/?$",
    ]
    
CORS_ALLOW_ALL_ORIGINS = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# =========================
# VALIDADORES DE SENHA
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =========================
# INTERNACIONALIZAÇÃO
# =========================
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True
USE_TZ = True

# =========================
# STATIC FILES
# =========================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # para deploy
STATICFILES_DIRS = [BASE_DIR / 'static']  # pasta local

# =========================
# REST FRAMEWORK
# =========================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}

# =========================
# AUTO FIELD
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
