from .base import *

ADMINS= [('admin','imash.odessahouse@gmail.com')]

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': os.getenv('DB_APP','app_db'),
         'USER': os.getenv('DB_USER','admin'),
         'PASSWORD': os.getenv('DB_PASSWORD','devpass'),
         'HOST': os.getenv("DB_HOST","127.0.0.1"),
         'PORT': os.getenv("DB_PORT","5432"),
     }
}



EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 25
EMAIL_HOST_USER = os.environ.get('MYEMAIL','smtp_sender@mail.ru')
EMAIL_HOST_PASSWORD = os.environ.get('MYPASS','v0hRbpS3bfB3PRhx2Zvi')
DEFAULT_FROM_EMAIL = 'smtp_sender@mail.ru'

# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = os.environ.get('MYEMAIL')
# EMAIL_HOST_PASSWORD = os.environ.get('MYPASS')

def check_env():
    if EMAIL_HOST_USER != '':
    	return 'django.core.mail.backends.smtp.EmailBackend'
    else:
    	return 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = check_env()




BRAINTREE_MERCHANT_ID = os.getenv('BRAINTREE_MERCHANT_ID','trhv67z232ntzz63') # Seller ID.
BRAINTREE_PUBLIC_KEY = os.getenv('BRAINTREE_PUBLIC_KEY','z6r3qcbkwwdhbk4q') # Public key.
BRAINTREE_PRIVATE_KEY = os.getenv('BRAINTREE_PRIVATE_KEY','2abd6474f8fe1ca37072b851aa949095') # Secret key

from braintree import Configuration, Environment

Configuration.configure(
        Environment.Sandbox,
        BRAINTREE_MERCHANT_ID,
        BRAINTREE_PUBLIC_KEY,
        BRAINTREE_PRIVATE_KEY
    )

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 1

CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"