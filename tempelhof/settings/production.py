from .base import *

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

try:
    from .local import *
except ImportError:
    pass
