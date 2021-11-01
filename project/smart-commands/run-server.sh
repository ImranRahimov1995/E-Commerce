export DJANGO_SETTINGS_MODULE=config.settings.local


cd ..

source ./venv/bin/activate
cd project


docker run -p 6379:6379 --name some-redis --rm -d redis
python3 manage.py runserver 0.0.0.0:8000
docker stop some-redis