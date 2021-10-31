export DJANGO_SETTINGS_MODULE=config.settings.local


cd ..

source ./venv/bin/activate
cd project

python3 manage.py runserver 0.0.0.0:8000
