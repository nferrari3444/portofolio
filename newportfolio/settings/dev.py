from newportfolio.settings.base import *

# Override base.py settings here
DEBUG=True


ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE':  'django.db.backends.postgresql' ,#  'django.db.backends.sqlite3',
        'NAME':  'portfoliodb',
        'USER': 'postgres',
        'PASSWORD': 'alfabeta1984',
        'HOST': 'localhost',
        'PORT': '5432'                                           #BASE_DIR / 'db.sqlite3',
    }
}

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')





STATIC_URL= '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'uploads'

# if DEBUG:
#          STATICFILES_DIRS = [
#              os.path.join(BASE_DIR, 'static')
#         ]
# else:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATICFILES_DIRS = [
# BASE_DIR / "static" ,
# "/var/www/static/"
# # "C:/Users/Nicolas/Desktop/newportfolio-project/jobs/static/"
    
# ]


try:
    from newportfolio.settings.local import *
except:
    pass