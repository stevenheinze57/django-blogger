
set -e

echo "-----> Loading Blogger UI fixture data into database "
cd /opt/blogger_ui/src/app/
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata /mnt/env-files/blogger.fixture.json

echo "-----> Blogger UI bootstrap complete "
