
#!/bin/bash

# Clone all github.com repositories for your user

for repo in `curl -s https://api.github.com/users/<your_username>/repos?per_page=1000 |grep git_url |awk '{print $2}'| sed 's/"\(.*\)",/\1/'`;do
git clone $repo;
done;
