
set +e

echo "-----> Killing all 'runserver' processes "
ps -aux | grep runserver | awk '{print $2}' | xargs sudo kill -9
echo "---> Only one failing kill command is normal"

set -e

echo "-----> Recycling the blogger_ui.log file "
cat /dev/null > /opt/blogger_ui/logs/blogger_ui.log

echo "-----> Installing dependencies from requirements.txt "
cd /opt/blogger_ui/src/
pip3 install -r requirements.txt

echo "-----> Making database migrations "
cd /opt/blogger_ui/src/app/
python3 manage.py makemigrations
python3 manage.py migrate

echo "-----> Starting server "
nohup sudo python3 manage.py runserver 0.0.0.0:80 >> /opt/blogger_ui/logs/blogger_ui.log 2>&1 &

echo "-----> Blogger UI restart complete "
