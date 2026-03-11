import dj_database_url
from newportfolio.settings.base import *

# Override base.py settings here
DEBUG = False
env = os.environ.copy()

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}

DATABASES['default'].update(dj_database_url.config(conn_max_age=500, ssl_require=True))

# try:
#     from newportfolio.settings.local import *
# except:
#     pass