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

You can get this from https://www.braintreepayments.com/sandbox

_________________________________________________________________________________




