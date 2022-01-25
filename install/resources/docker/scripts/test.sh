
set -e

echo "-----> Running Blogger UI unit tests "
cd /opt/blogger_ui/src/app/
python3 manage.py test

echo "-----> Blogger UI test complete "
