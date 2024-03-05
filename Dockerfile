FROM python:3.11.5-slim-bookworm
ARG YOUR_ENV

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.8.1

WORKDIR /code
EXPOSE 80
COPY poetry.lock pyproject.toml /code/
RUN pip3 install poetry && poetry install
COPY . /code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
