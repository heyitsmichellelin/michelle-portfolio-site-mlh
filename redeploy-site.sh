#!/bin/bash

cd portfolio-site-mlh/

git fetch && git reset origin/main --hard

echo "Pulled from GitHub"

docker compose -f docker-compose.prod.yml down

echo "just ran docker down"

docker compose -f docker-compose.prod.yml up -d --build

echo "just ran docker up"