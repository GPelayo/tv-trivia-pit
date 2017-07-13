import os

try:
    import local_settings
    OMDB_API_KEY = local_settings.OMDB_API_KEY
    FLASK_HOST_IP = local_settings.FLASK_HOST_IP
except ImportError:
    OMDB_API_KEY = os.environ.get('OMDB_API_KEY', None)
    FLASK_HOST_IP = '0.0.0.0'