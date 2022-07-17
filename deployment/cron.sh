
crontab -l > mycron


@reboot /home/django_user/E-Commerce/deployment/celery.sh >/home/django_user/ecomcelery.txt 2>&1



crontab mycron
rm mycron