from .base import *
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key

DEBUG = False

ALLOWED_HOSTS = [os.getenv('PUBLIC_IP','0.0.0.0')]

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': os.getenv('DB_APP','app_db'),
         'USER': os.getenv('DB_USER','admin'),
         'PASSWORD': os.getenv('DB_PASSWORD','devpass'),
         'HOST': os.getenv("DB_HOST","postgresdb"),
         'PORT': os.getenv("DB_PORT","5432"),
     }
}




EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("MY_EMAIL",'')
EMAIL_HOST_PASSWORD = os.getenv("MY_EMAIL_PASSWORD",'')


def check_env():
    if EMAIL_HOST_USER:
    	return 'django.core.mail.backends.smtp.EmailBackend'
    else:
    	return 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = check_env()




BRAINTREE_MERCHANT_ID = os.getenv('BRAINTREE_MERCHANT_ID','trhv67z232ntzz63') # Seller ID.
BRAINTREE_PUBLIC_KEY = os.getenv('BRAINTREE_PUBLIC_KEY','z6r3qcbkwwdhbk4q') # Public key.
BRAINTREE_PRIVATE_KEY = os.getenv('BRAINTREE_PRIVATE_KEY','2abd6474f8fe1ca37072b851aa949095') # Secret key


REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 1
