#!/bin/bash

git checkout master
git pull
git merge dev
NOW=`date`
git commit -m "[DEPLOY] $NOW"
git push
git checkout dev
