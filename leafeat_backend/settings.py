DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'leafeat',          # seu banco criado
        'USER': 'postgres',      # usuário do PostgreSQL
        'PASSWORD': '@Pgpghx63p',    # senha do PostgreSQL
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # aqui você pode colocar caminhos para seus templates personalizados
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

INSTALLED_APPS = [
    'corsheaders', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'usuarios',
    'restaurantes',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # Para permitir CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Vue
    "http://127.0.0.1:5173",
]

AUTH_USER_MODEL = 'usuarios.Usuario'
# Configuração do modelo de usuário personalizado

DEBUG = True

ALLOWED_HOSTS = ['*']

# Caminho base do projeto
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# URL para arquivos estáticos
STATIC_URL = '/static/'

# Opcional: pasta onde os arquivos estáticos serão coletados
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Pasta extra para arquivos estáticos do projeto
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
CORS_ALLOW_ALL_ORIGINS = True
# INSTALLED_APPS += ['rest_framework']
ROOT_URLCONF = 'leafeat_backend.urls'

SECRET_KEY = 'kb1jc@8l183d7cezs26(db!4usxiz5l66&4+r0c53)7d*6@3c!'

AUTHENTICATION_BACKENDS = [
    'usuarios.auth_backends.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]