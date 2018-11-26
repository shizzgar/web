sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/shizz/py/clearstep/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/shizz/py/clearstep/web/etc/hello.py hello:hello &
cd ask
gunicorn -c /home/shizz/py/clearstep/web/etc/django.py ask.wsgi:application &
