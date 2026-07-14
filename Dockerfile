FROM python:3.12-slim

ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir poetry


COPY pyproject.toml poetry.lock ./


RUN poetry config virtualenvs.create false \
    && poetry install --without lint --no-root --no-interaction


COPY . .


RUN chmod +x ./scripts/entrypoint.sh
CMD ["./scripts/entrypoint.sh"]
