#!/bin/bash
set -e

# Функция для проверки подключения к PostgreSQL
postgres_ready() {
  python << END
import sys
import psycopg
import os
import time

database_url = os.environ.get('DATABASE_URL')
if not database_url:
    sys.stderr.write("DATABASE_URL не указан в переменных окружения\n")
    sys.exit(1)

retries = 10
while retries > 0:
    try:
        conn = psycopg.connect(database_url)
        conn.close()
        sys.exit(0)
    except Exception as e:
        retries -= 1
        sys.stderr.write(f"Ожидание доступности базы данных... {e}\n")
        time.sleep(2)

sys.stderr.write("Не удалось подключиться к PostgreSQL после нескольких попыток\n")
sys.exit(1)
END
}

echo "Ожидание доступности PostgreSQL..."
postgres_ready

echo "PostgreSQL доступен. Запуск приложения..."
exec "$@"
