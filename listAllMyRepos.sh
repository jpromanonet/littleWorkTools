#!/bin/bash

echo
echo Insert your github username or organization name to list all your repos
read userName
echo

curl -s https://api.github.com/users/$userName/repos?per_page=1000 |grep git_url |awk '{print $2}'| sed 's/"\(.*\)",/\1/'

echo
