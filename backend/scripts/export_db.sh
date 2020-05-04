#!/bin/bash

DB_DUMP_PATH=./docker-entrypoint-initdb.d
DB_DUMP_NAME=dump.sql
PROJECT_ENV_PATH=./.env-dev
DATABASE_DOCKER_SERVICE='postgres'

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

cd ..
echo '0-> Clean database dump...'
[[ -f "$DB_DUMP_PATH/$DB_DUMP_NAME" ]] && rm "$DB_DUMP_PATH/$DB_DUMP_NAME"

echo '1-> Getting DB name & pass'
source $PROJECT_ENV_PATH
echo "[DB  PASSWORD]====> "
echo $POSTGRES_USER
echo "[ CONTENAIRE ]====> $DB_CONTENAIRE"
wait_user_validation

echo '1-> Dumping database...'
docker-compose exec $DATABASE_DOCKER_SERVICE sh -c 'exec pg_dump -U $POSTGRES_USER $POSTGRES_DB' > $DB_DUMP_PATH/$DB_DUMP_NAME
echo "===> There should be your file here now: "
ls -lh $DB_DUMP_PATH
wait_user_validation