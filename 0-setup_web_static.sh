#!/usr/bin/env bash
# Bash script that sets up your web servers for
# the deployment of web_static
# Install Nginx if it not already installed
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create the folder
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "<!DOCTYPE html>
<html>
  <head>
	<meta charset='UTF-8'>
	<title>My Nginx</title>
  </head>
  <body>
    <p>Hello Nginx</p>
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
