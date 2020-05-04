#!/bin/bash

function wait_user_validation () {
  echo '----------------------'
  read -p "Everything went okay? [y,n]" doit
  case $doit in
    y|Y) echo 'Continue' ;;
    n|N) exit 1 ;;
    *) echo dont know ;;
  esac
  echo '----------------------'
}

echo 'Did you close Android Studio ?'
wait_user_validation
cordova platform rm android
npm run build
wait_user_validation
mkdir ../www/static/css/static
cp -r ../www/static/img ../www/static/css/static
cordova platform add android