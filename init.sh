sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/etc/nginx.conf   /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
