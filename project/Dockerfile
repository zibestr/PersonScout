FROM python:3.12

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# to run poetry directly as soon as it's installed
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /app
RUN mkdir -p /staticfiles
RUN mkdir -p /mediafiles


COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-ansi

COPY entrypoint.sh /app/entrypoint.sh
COPY . /app/

ENTRYPOINT ["/app/entrypoint.sh"]
