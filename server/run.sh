#!/bin/bash

echo "Running all required API services..."

#echo "Check Docker Containers"
#
#docker container ls -a
#
#echo "Sleeping for 10s, if Postgres and Redis are not running please quit and start them."
#sleep 10

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

echo $SCRIPT_DIR

SCRIPT_PREFIX="cd ${SCRIPT_DIR} && source venv/bin/activate &&"

start_celery_worker="${SCRIPT_PREFIX} python -m celery -A commutr worker -l info -E"
start_celery_beat="${SCRIPT_PREFIX} python -m celery -A commutr beat -l info"
start_commutr="${SCRIPT_PREFIX} python manage.py runserver"

osascript -e "tell application \"Terminal\" to do script \"${start_celery_worker}\""
sleep 5
osascript -e "tell application \"Terminal\" to do script \"${start_celery_beat}\""

if [[ "$#" -ge 1 && "$*" == *"--run-migrations"* ]]; then
  source venv/bin/activate
  python manage.py makemigrations
  python manage.py migrate
fi

if [[ "$#" -ge 1 && "$*" == *"--no-commutr"* ]]; then
  echo "Not running with Commutr. Exiting..."
  exit 1
fi

sleep 5
osascript -e "tell application \"Terminal\" to do script \"${start_commutr}\""