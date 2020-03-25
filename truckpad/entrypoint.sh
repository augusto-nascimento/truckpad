#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

pipenv run /usr/src/truckpad/manage.py flush --no-input
pipenv run /usr/src/truckpad/manage.py migrate

exec "$@"