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
# Get started

1. git clone https://github.com/ImranRahimov1995/E-Commerce-Mele.git
2. python3 -m venv venv || source venv/bin/activate

All commands must starting from project/
pip3 install -r requirements.txt

# This is your local settings export your local settings for ENVOIRMENT and run some commands:

open project/config/settings

run this command:
. ./local_env.sh