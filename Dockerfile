FROM python:3.8.10-alpine

WORKDIR /app
COPY . /app/
RUN pip install pipenv

# You will need this if you need PostgreSQL, otherwise just skip this
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
RUN pip install pipenv
RUN pipenv install --system --deploy

# Runner script here
CMD ["python", "bot.py"]