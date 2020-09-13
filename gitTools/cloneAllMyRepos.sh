#!/bin/bash
# Clone all github.com repos for my user

echo Insert your github username or organization name:
read userName

echo
echo About to start cloning all your repos to this dir...
echo

for repo in `curl -s https://api.github.com/users/$userName/repos?per_page=1000 |grep git_url |awk '{print $2}'| sed 's/"\(.*\)",/\1/'`;do
git clone $repo;
done;

echo
echo All your repos are cloned, task finished!
echo
