
#select config
export DJANGO_SETTINGS_MODULE=config.settings.pro
#migrate in right db
python3 manage.py migrate --settings=config.settings.pro