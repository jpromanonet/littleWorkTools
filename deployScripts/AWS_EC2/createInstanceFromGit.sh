#!/bin/bash

sudo yum -y install httpd
sudo systemctl start httpd
sudo yum -y install git
sudo git clone https://amazon:Test-12345@gitlab.8amarketing.com/zendesk/showcase
sudo mkdir -p /var/www/html/livestreaming-20-08-20/
sudo cp -R ./showcase/* /var/www/html/livestreaming-20-08-20/
sudo chown -R ec2-user:ec2-user /var/www/html/
sudo echo $HOSTNAME > /var/www/html/index.html