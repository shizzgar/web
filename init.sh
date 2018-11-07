sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/hello.py hello:hello
sudo gunicorn -c /home/box/web/etc/django.py ask.wsgi:application

