#!/bin/bash

commands=("python3" "flutter" "docker" "psql" "xcode-select")

for cmd in "${commands[@]}"; do
    if command -v "$cmd" >/dev/null 2>&1; then
        echo ""
    else
        echo "$cmd is not installed. Please install all pre-requisites before running this script."
    fi
done

echo "All required commands have been installed. Moving on..."

echo "Installing virtualenv and setting up environment"
{
  pip3 install virtualenv
  python3 -m venv venv
  echo "export commutr_postgres_password=wnGhxi9ZaFN42G" | tee -a venv/bin/activate
  source venv/bin/activate
} &> /dev/null
echo "-- Done"

echo "Installing pip requirements"
{
  pip install -r requirements.txt
} &> /dev/null
echo "-- Done"

echo "Pulling Docker images"
{
  docker pull postgres:latest
  docker pull redis/redis-stack:latest
} &> /dev/null
echo "-- Done"

echo "Starting PostgreSQL and Redis"
{
  docker run --name commutr-db -e POSTGRES_PASSWORD=$commutr_postgres_password -d -p 5432:5432 postgres
  docker run -p 6379:6379 -d redis/redis-stack:latest
} &> /dev/null
echo "-- Done"

echo "Setting up database"
echo "-- Make Migrations"
{
  python manage.py makemigrations
} &> /dev/null
echo "---- Done"

echo "-- Do Migrations"
{
  python manage.py migrate
} &> /dev/null
echo "---- Done"

echo "Installation has completed. Try running the API with './run.sh'"