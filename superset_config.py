from superset.security import SupersetSecurityManager
from flask_appbuilder.security.manager import AUTH_OAUTH
import os

# Superset specific config
ROW_LIMIT = 5000

# Flask App Builder configuration
# Your App secret key will be used for securely signing the session cookie
# and encrypting sensitive information on the database
# Make sure you are changing this key for your deployment with a strong key.
# Alternatively you can set it with `SUPERSET_SECRET_KEY` environment variable.
# You MUST set this for production environments or the server will refuse
# to start and you will see an error in the logs accordingly.
SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY')

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
# The check_same_thread=false property ensures the sqlite client does not attempt
# to enforce single-threaded access, which may be problematic in some edge cases
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SUPERSET_DATABASE_URI_OVERRIDE",
    "sqlite:////app/superset_home/superset.db?check_same_thread=false"
)


# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''

CUSTOM_SECURITY_MANAGER = SupersetSecurityManager

OAUTH_PROVIDERS = [{
    'name': 'google',
    'token_key': 'access_token',
    'icon': 'fa-google',
    'remote_app': {
        'client_id': os.getenv('GOOGLE_CLIENT_ID'),
        'client_secret': os.getenv('GOOGLE_CLIENT_SECRET'),
        'client_kwargs': {
            'scope': 'email profile'
        },
        'access_token_url': 'https://accounts.google.com/o/oauth2/token',
        'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
        'authorize_params': None,
        'access_token_params': None,
        'jwks_uri': 'https://www.googleapis.com/oauth2/v3/certs',
        'userinfo_endpoint': 'https://www.googleapis.com/oauth2/v3/userinfo',
        'client_kwargs': {
            'scope': 'openid email profile'
        },
    }
}]

#AUTH_TYPE = AUTH_OAUTH