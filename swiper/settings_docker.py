"""
Django settings for swiper project.

Generated by 'django-admin startproject' using Django 1.11.27.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5cx5#du3a8-^gskmp#zwz@6kc%h*@n9e+p-)+j0!*u*g5-x&q_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'user',
    'social',
    'vip'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'common.middleware.AuthMiddleware',
    'common.middleware.LogicErrMiddleware',
]

ROOT_URLCONF = 'swiper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'swiper.wsgi.application'

# Session 存储引擎
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Cache 配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://172.18.0.20:6379/6",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PICKLE_VERSION": -1,
        }
    }
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '172.18.0.30',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123',
        'NAME': 'swiper',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# 日志的配置
LOGGING = {
    'version': 1,

    # 打开或者关闭 Django 自带的日志 (NOTE: False 时可以查看Django生成的SQL语句)
    'disable_existing_loggers': True,

    # 格式配置
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(module)s.%(funcName)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'verbose': {
            'format': ('%(asctime)s %(levelname)s [%(process)d-%(threadName)s] '
                       '%(module)s.%(funcName)s line %(lineno)d: %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    # Handler 配置
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'info': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{BASE_DIR}/logs/info.log',  # 日志保存路径
            'when': 'midnight', # 每天凌晨零点切割日志
            'backupCount': 30,  # 日志保留 30 天
            'formatter': 'simple',
        },
        'error': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{BASE_DIR}/logs/error.log',  # 日志保存路径
            'when': 'W0',      # 每周一切割日志
            'backupCount': 4,  # 日志保留 4 周
            'formatter': 'verbose',
        }
    },
    # Logger 配置
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'ERROR'
        },
        'inf': {
            'handlers': ['info'],
            'propagate': True,
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
        'err': {
            'handlers': ['error'],
            'propagate': True,
            'level': 'DEBUG' if DEBUG else 'ERROR',
        }
    }
}
