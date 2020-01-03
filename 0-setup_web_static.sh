#!/usr/bin/env bash
# This script installs nginx if is not already installed and prepare the server
if [ $(dpkg-query -W -f='${Status}' $1 2> /dev/null | grep -c "ok installed") -eq 0 ];
then
    apt-get -y update
    apt-get -y install nginx
    printf "Ceci n'est pas une page\n" > /usr/share/nginx/html/404.html
    sed -i "/server_name _;/ a\\\tadd_header X-Served-By $HOSTNAME;\n\n\trewrite ^/redirect_me http://www.youtube.com permanent;\n\terror_page 404 /404.html;\n\n\tlocation = /404.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t}" /etc/nginx/sites-available/default
fi
mkdir -p /data/; mkdir -p /data/web_static/; mkdir -p /data/web_static/releases/; mkdir -p /data/web_static/shared/; mkdir -p /data/web_static/releases/test/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i "/^\tlocation \/ {/ i\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t\n}" /etc/nginx/sites-available/default
service nginx restart
