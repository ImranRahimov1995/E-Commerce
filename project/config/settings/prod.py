from .base import *

from braintree import Configuration, Environment

DEBUG = False

ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('MY_EMAIL', '')
EMAIL_HOST_PASSWORD = os.environ.get('MYPASS', '')


def check_env():
    if EMAIL_HOST_USER:
    	return 'django.core.mail.backends.smtp.EmailBackend'
    else:
    	return 'django.core.mail.backends.console.EmailBackend'



EMAIL_BACKEND = check_env()


BRAINTREE_MERCHANT_ID = os.getenv('BRAINTREE_MERCHANT_ID','trhv67z232ntzz63') # Seller ID.
BRAINTREE_PUBLIC_KEY = os.getenv('BRAINTREE_PUBLIC_KEY','z6r3qcbkwwdhbk4q') # Public key.
BRAINTREE_PRIVATE_KEY = os.getenv('BRAINTREE_PRIVATE_KEY','2abd6474f8fe1ca37072b851aa949095') # Secret key



Configuration.configure(
        Environment.Sandbox,
        BRAINTREE_MERCHANT_ID,
        BRAINTREE_PUBLIC_KEY,
        BRAINTREE_PRIVATE_KEY
    )

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1
