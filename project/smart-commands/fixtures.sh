mkdir media media/products/ media/products/2021 media/products/2021/10 media/products/2021/10/31 

cp fixtures/images/* media/products/2021/10/31/

python3 manage.py loaddata fixtures/dump.json
python3 manage.py loaddata fixtures/admin-dump.json
python3 manage.py loaddata fixtures/coupon-dump.json

