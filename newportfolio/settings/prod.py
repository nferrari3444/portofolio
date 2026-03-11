from newportfolio.settings.base import *

# Override base.py settings here
DEBUG = False
env = os.environ.copy()

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



DATABASES = {
    'default': {
        'ENGINE':  'django.db.backends.postgresql' ,#  'django.db.backends.sqlite3',
        'URL': os.getenv('DATABASE_URL'),
        'NAME':  os.getenv("DATABASE"),
        'USER': os.getenv("USER"),
        'PASSWORD': os.getenv("PASSWORD"),
        'HOST': os.getenv("HOST"),
        'PORT': os.getenv("PORT")                                        #BASE_DIR / 'db.sqlite3',
    }
}

# try:
#     from newportfolio.settings.local import *
# except:
#     pass