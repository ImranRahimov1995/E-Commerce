export DJANGO_SETTINGS_MODULE=config.settings.local

cd ..
source ./venv/bin/activate
cd project

celery -A config  worker --loglevel=info
