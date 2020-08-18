#!/bin/bash

sudo yum -y install httpd
sudo systemctl start httpd
sudo yum -y install git
sudo git clone https://user:password@repo
sudo cp -R ./<YOUR GIT DIR>/* /var/www/html/
sudo chown -R ec2-user:ec2-user /var/www/html/
sudo echo $HOSTNAME > /var/www/html/success.html
