import os

# -----------------------------------------------------------------------------
# GENERAL FLASK CONFIGURATION
# -----------------------------------------------------------------------------
SECRET_KEY = os.environ['SECRET_KEY']
LOG_FILE = os.environ['LOG_FILE']
API_VERSION = "v1"

# -----------------------------------------------------------------------------
# JWT CONFIGURATIONS
# -----------------------------------------------------------------------------

# IF JWT ALGORITHM IS HS256 THEN USE SYMMETRIC CRYPTOGRAPHY
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']

# IF JWT ALGORITHM IS SET TO RS256 THEN ASYMMETRIC CRYPTO IS USED SO A
# VALID PEM FORMATTED PUBLIC KEY MUST BE PROVIDED.
# JWT_PUBLIC_KEY = os.environ['JWT_PUBLIC_KEY']
JWT_TOKEN_LOCATION = 'headers'
JWT_ALGORITHM = 'RS256'


# -----------------------------------------------------------------------------
# CELERY CONFIGURATION
# -----------------------------------------------------------------------------
# CELERY IS USED TO SUPPORT BACKGROUND PROCESSING
# CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
# CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']
task_serializer = 'json'
accept_content = ['json']
