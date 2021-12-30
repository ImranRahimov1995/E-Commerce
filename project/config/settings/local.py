from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"




#PAYMENT ID_PASS
#You need have 3 constant in pro.py 
#https://www.braintreepayments.com/sandbox

production_env_path = os.path.join(BASE_DIR / 'config/settings/pro.py')
check_production_env = os.path.exists(production_env_path)


if check_production_env:
    try: 
        from .prod import BRAINTREE_MERCHANT_ID,\
                        BRAINTREE_PUBLIC_KEY,\
                        BRAINTREE_PRIVATE_KEY

    except ImportError:

            BRAINTREE_MERCHANT_ID = ""
            BRAINTREE_PUBLIC_KEY = ""
            BRAINTREE_PRIVATE_KEY = ""

    from braintree import Configuration, Environment

    Configuration.configure(
            Environment.Sandbox,
            BRAINTREE_MERCHANT_ID,
            BRAINTREE_PUBLIC_KEY,
            BRAINTREE_PRIVATE_KEY
        )

REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 1
