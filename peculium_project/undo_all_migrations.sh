#!/bin/sh
echo "Starting ... "


echo ">> Deleting all DATA BASE"
find . -path "*/db.sqlite3"  -delete

#python manage.py flush
#python manage.py migrate --fake
echo ">> Deleting old migrations"
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

echo ">> Running manage.py makemigrations"
python manage.py makemigrations

echo ">> Running manage.py migrate"
python manage.py migrate

echo ">> load DB"
#./manage.py dumpdata > db.json
./manage.py loaddata db.json
#echo ">> create super user"

#soteqapp@gmail.com
# python manage.py createsuperuser

#echo "from apps.accounts.models import Member; Member.objects.create_superuser('wafa.yahyaoui@ensi-uma.tn','wafa0000')" | python manage.py shell


# echo "from django.contrib.auth.models import User; User.objects.create_superuser('hoffa', 'soteqapp@gmail.com', 'hoffa0000')" | python manage.py shell
# echo "from django.contrib.auth.models import User; User.objects.filter(email='soteqapp@gmail.com').delete(); User.objects.create_superuser('hoffa', 'soteqapp@gmail.com', 'hoffa0000')" | python manage.py shell

echo ">> Done"
