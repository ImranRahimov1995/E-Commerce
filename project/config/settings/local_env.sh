#This file need to run from /project/config/settings


#select config
export DJANGO_SETTINGS_MODULE=config.settings.local

cd ..
cd ..

#make migrate in right db
python3 manage.py migrate --settings=config.settings.local
