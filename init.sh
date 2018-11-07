sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/hello.py hello:wsgi_application
sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application

