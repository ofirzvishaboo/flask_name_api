#!/bin/bash

until curl -s http://db:3306 &> /dev/null; do
  >&2 echo "Waiting for MySQL to start..."
  sleep 1
done

exec docker-entrypoint.sh devops-rest
