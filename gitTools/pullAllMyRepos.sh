#!/bin/bash
# pull all github.com repos

echo
echo About to start pulling updates from all your repos to this dir...
echo

find . -mindepth 1 -maxdepth 1 -type d -print -exec git -C {} pull \;
done;

echo
echo All your repos are updated, task finished!
echo
