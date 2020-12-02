import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '1_8pekirv-*n4%s@^8^_br!9yj08ztou@7=%il!-d03=1bthzj'

DEBUG = True

ALLOWED_HOST=[]

INSTALLED_APPS = [
    'forum',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'career.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'career.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

staticfile=os.path.join(BASE_DIR,'staticfiles')

STATICFILES_DIRS=[staticfile]

STATIC_ROOT='/home/insightlife/last/career/static'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

PAYTM_MERCHANT_ID = 'JEYLdX59445091837751'

PAYTM_SECRET_KEY = 'Ielms1FV!gmIm8Uv'

PAYTM_WEBSITE = 'WEBSTAGING'

PAYTM_CHANNEL_ID = 'WEB'

PAYTM_INDUSTRY_TYPE_ID = 'Retail'

EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_HOST_USER = 'sumanpatra260@gmail.com'

EMAIL_HOST_PASSWORD = 'jukyfzmfmkpcxbhb'

DEFAULT_FROM_EMAIL = 'sumanpatra260@gmail.com'

DEFAULT_TO_EMAIL = 'sumanpatra68@gmail.com'

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'
