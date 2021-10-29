
#select config
export DJANGO_SETTINGS_MODULE=config.settings.pro

cd ..
cd ..

python3 manage.py migrate --settings=config.settings.pro



