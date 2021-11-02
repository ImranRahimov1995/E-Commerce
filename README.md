# E-Commerce-Mele

This is E-Commerce project my lesson-project which i learned from  book 
http://139.162.178.110/
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
. ./smart-commands/install.sh

2. If you want load fixtures in your db \
. ./smart-commands/fixtures.sh

4. Open new terminal , go to project/
. ./smart-commands/run-celery.sh \
_________________________________________________________________________________
# For testing in docker with nginx / gunicorn / postgres / -with loaded fixtures


1. git clone https://github.com/ImranRahimov1995/E-Commerce-Mele.git
2. git checkout dockerize

_________________________________________________________________________________

## For send emails 
enter your mail in docker-compose.yaml
  web:
    restart: always
    environment:
      - MY_EMAIL=''
      - MY_EMAIL_PASSWORD=''
________________________________________________________
Now you can build your app and test it in real case

cd E-Commerce/

docker-compose build \
docker-compose up 

### Admin credentials:
login : admin \
password: 123

-----------------
# FOR PAYMENT :

cart : 5555 5555 5555 4444 \
CVV : 123 \
Expire Date : 02\24  

## FOR Coupon- discount:

input "DISCOUNT"  

-----------------
