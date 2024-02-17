#!/bin/bash

until nc -z db 3306; do
  >&2 echo "Waiting for MySQL to start..."
  sleep 1
done

exec docker-entrypoint.sh python app.py
