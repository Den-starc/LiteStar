FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/apt/lists/*

COPY pyproject.toml poetry.lock* ./

RUN pip install poetry==2.1.3 && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . /app

ENV PYTHONUNBUFFERED=1

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
