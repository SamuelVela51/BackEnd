#!/bin/sh

# Set default values if environment variables are not set
POSTGRES_USER=${POSTGRES_USER:-postgres}
POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-postgres}
POSTGRES_DB=${POSTGRES_DB:-goal-wear}

echo "Using database settings:"
echo "POSTGRES_USER: $POSTGRES_USER"
echo "POSTGRES_DB: $POSTGRES_DB"
echo "POSTGRES_PASSWORD: [hidden]"

echo "Waiting for PostgreSQL to be ready..."
until PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U "$POSTGRES_USER" -c '\q' 2>/dev/null; do
  >&2 echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

echo "PostgreSQL is ready"

# Check if the database exists, if not create it
if PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U "$POSTGRES_USER" -lqt | cut -d \| -f 1 | grep -qw "$POSTGRES_DB"; then
    echo "Database $POSTGRES_DB already exists"
else
    echo "Database $POSTGRES_DB does not exist. Creating..."
    PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U "$POSTGRES_USER" -c "CREATE DATABASE \"$POSTGRES_DB\";"
    echo "Database $POSTGRES_DB created"
fi

# Connect to the specific database
until PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q' 2>/dev/null; do
  >&2 echo "Waiting for database $POSTGRES_DB to be ready"
  sleep 1
done

echo "Database $POSTGRES_DB is ready!"