FROM python:3.10.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app
COPY Pipfile Pipfile.lock ./


RUN apt-get update
RUN apt-get -y install python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0
RUN python -m pip install --upgrade pip

RUN python -m pip install pipenv
RUN pipenv install --deploy --system
RUN python -m pip install gunicorn
RUN python -m pip install whitenoise

COPY . ./

EXPOSE 8000

ENTRYPOINT ["sh", "./entrypoint.sh"]
