#!/bin/bash
set -e

echo "Waiting for postgres..."
while ! pg_isready -h db -p 5432 -U test; do
  sleep 1
done

echo "PostgreSQL is up"

alembic upgrade head

exec uvicorn app.main:app --host 0.0.0.0 --port 8000
