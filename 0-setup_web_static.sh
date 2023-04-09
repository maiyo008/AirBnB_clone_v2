#!/usr/bin/env bash
# Set up web servers for the deployment of web-static

#Install Nginx if not installed
if command -v  nginx >/dev/null 2>&1; then
    echo "Nginx is installed"
else
    sudo apt-get update
    sudo apt-get install nginx
fi

#Create these folders if they do not exist
# /data/
# /data/web_static/
# /data/web_static/releases/
# /data/web_static/shared/
# /data/web_static/releases/test/

folder_name1="/data/"
folder_name2="/data/web_static/"
folder_name3="/data/web_static/releases/"
folder_name4="/data/web_static/shared/"
folder_name5="/data/web_static/releases/test/"

if [ ! -d "$folder_name1" ]; then
    echo "creating $folder_name1 ..."
    mkdir -p "$folder_name1"
else
    echo "$folder_name1 already exists"
fi

if [ ! -d "$folder_name2" ]; then
    echo "creating $folder_name2 ..."
    mkdir -p "$folder_name2"
else
    echo "$folder_name2 already exists"
fi

if [ ! -d "$folder_name3" ]; then
    echo "creating $folder_name3 ..."
    mkdir -p "$folder_name3"
else
    echo "$folder_name3 already exists"
fi

if [ ! -d "$folder_name4" ]; then
    echo "creating $folder_name4 ..."
    mkdir -p "$folder_name4"
else
    echo "$folder_name4 already exists"
fi

if [ ! -d "$folder_name5" ]; then
    echo "creating $folder_name5 ..."
    mkdir -p "$folder_name5"
else
    echo "$folder_name5 already exists"
fi

#writing random text to index.hmtl
sudo sh -c "cat > /data/web_static/releases/test/index.html"<<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

#Creating symbolic link
link_path="/data/web_static/current"
target_path="/data/web_static/releases/test/"
if [ -L "$link_path" ]; then
    echo "symbolic link exists. Removing it ..."
    rm "$link_path"
fi
echo "creating new symbolic link..."
ln -s "$target_path" "$link_path"
echo "Symbolic link created successfully"

#Change ownership recursively
echo "changing ownership of $folder_name1"
sudo chown -R ubuntu:ubuntu /data/

#Updating default nginx configuration file
sudo sh -c "cat > /etc/nginx/sites-available/default"<<EOF
server {
    listen 80;
    root /var/www/html;
    index index.html;
    

        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        error_page 404 /404.html;
        location = /404.html {
                root /var/www/html;
                internal;
        }
        location /hbnb_static {
            alias /data/web_static/current/;
            index index.html;
        }
        add_header X-Served-By \$hostname;

 }
EOF

#Test Nginx configuration file
sudo nginx -t

#Restart nginx
sudo service nginx restart
#Exit successfully
exit 0
