# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.4
FROM python:${PYTHON_VERSION}-slim as base

# Doesn't write .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# install dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

USER appuser

# copy project and entrypoint.sh
COPY . /app/
COPY entrypoint.sh /app/entrypoint.sh

# Exposes the port
EXPOSE 8089

# Run the entrypoint.sh bash file
ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]