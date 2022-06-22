FROM python:3.8-slim-buster as prod
ENV POETRY_VERSION=1.1.13
RUN pip install "poetry==$POETRY_VERSION" && poetry config virtualenvs.create false
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_NO_CACHE_DIR=off
ENV PYTHONDONTWRITEBYTECODE=on
ENV PYTHONFAULTHANDLER=on
ENV PYTHONUNBUFFERED=on
ENV ENV=development
RUN apt-get update && apt-get install -y --no-install-recommends \
 build-essential nano telnet curl \
 && rm -rf /var/lib/apt/lists/*
# Dependencies

COPY . /home
WORKDIR /home
RUN poetry install --no-interaction --no-ansi -vvv
# Application

RUN chmod +x /home/docker/api/startup.sh
ENTRYPOINT /home/docker/api/startup.sh