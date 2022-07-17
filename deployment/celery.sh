export DJANGO_SETTINGS_MODULE=config.settings.prod


sleep 10

cd /home/avia_api/GogSkyApi/project


redis-cli FLUSHALL

python3 -m celery -A config worker --loglevel=info --detach

