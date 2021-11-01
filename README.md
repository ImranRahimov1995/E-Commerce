# E-Commerce-Mele

This is E-Commerce project my lesson-project which i learned from  book 

# What's inside ?

1. Base products with categories
2. Cart - based on sessions
3. Orders / Orders in PDF / Sending successful paid order in PDF
4. Payment system integrated https://www.braintreepayments.com/sandbox
5. In admin-panel export orders in csv
6. Coupon-discount system , you are create coupon in admin-panel and people uses your discount code when code is active state.
7. System of recommendations. which tracks user popup. 
   Sorts by rating the number of purchases along with another product and suggests to users


# What's i used ?

1. Django MVT
2. Celery
3. Redis
4. Postgres

# #library
You can see all installed library and relations in project/requirements.txt

_________________________________________________________________________________
# Get started for local settings

1. git clone https://github.com/ImranRahimov1995/E-Commerce-Mele.git
_________________________________________________________________________________

# All commands must starting from project/

1. Run this command for installing modules and activate venv:
. ./smart-command/install.sh

2. If you want load fixtures in your db
. ./smart-command/fixtures.sh

3. Open new terminal , go to project/
. ./smart-command/run-redis.sh

4. Open new terminal , go to project/
. ./smart-command/run-celery.sh

5 You need to create project/config/settings/pro.py (for right working all systems)

#EXAMPLE 

BRAINTREE_MERCHANT_ID = ' '     # ID SELLER. \
BRAINTREE_PUBLIC_KEY = ' '      # PUBLIC KEY. \
BRAINTREE_PRIVATE_KEY = ' '     # PRIVATE KEY. 

#### You can get this from https://www.braintreepayments.com/sandbox

_________________________________________________________________________________
# For testing in docker with nginx / gunicorn / postgres / -with loaded fixtures


1. git clone https://github.com/ImranRahimov1995/E-Commerce-Mele.git
2. git checkout dockerize

_________________________________________________________________________________
# Now you need to create 2 files

#### E-commerce/docker/postgres/init.sql:


CREATE USER username WITH PASSWORD 'devpass'; \
CREATE DATABASE app_db; \
GRANT ALL PRIVILEGES ON DATABASE app_db TO admin;

________________________________________________________
#### E-commerce/project/config/settings/pro.py:


from .base import *
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = { \
    'default': { \
        'ENGINE': 'django.db.backends.postgresql_psycopg2', \
        'NAME': 'app_db', \
        'USER': 'admin', \
        'PASSWORD': 'devpass', \
        'HOST': "postgresdb", \
        'PORT': 5432, \
    } \
} 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_USE_TLS = True \
EMAIL_HOST = 'smtp.gmail.com' \
EMAIL_PORT = 587 \
EMAIL_HOST_USER = 'YOUR_GMAIL_ADDRESS' \
EMAIL_HOST_PASSWORD = 'PASSWORD'


CELERY_BROKER_URL = "redis://redis:6379/0" \
CELERY_RESULT_BACKEND = "redis://redis:6379/0" 


BRAINTREE_MERCHANT_ID = ' '     # ID SELLER. \
BRAINTREE_PUBLIC_KEY = ' '      # PUBLIC KEY. \
BRAINTREE_PRIVATE_KEY = ' '     # PRIVATE KEY. 

##### You can get this from https://www.braintreepayments.com/sandbox



from braintree import Configuration, Environment

Configuration.configure( \
        Environment.Sandbox, \
            BRAINTREE_MERCHANT_ID, \
            BRAINTREE_PUBLIC_KEY, \
            BRAINTREE_PRIVATE_KEY \
    ) 


REDIS_HOST = 'redis' \
REDIS_PORT = 6379 \
REDIS_DB = 1 

________________________________________________________
Now you can build your app and test it in real case

cd E-Commerce/

docker-compose build \
docker-compose up 

### Admin credentials:
login : admin \
password: 123
