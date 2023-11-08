FROM python:3.10.12

RUN apt-get update
RUN apt-get -y install python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0 nginx

WORKDIR /app

RUN pip install pipenv

# Copiez le Pipfile et le Pipfile.lock dans le répertoire de travail
COPY Pipfile Pipfile.lock ./

# Installez les dépendances Python à l'aide de Pipenv
RUN pipenv install --deploy --ignore-pipfile

COPY . ./

ENTRYPOINT ["sh", "./entrypoint.sh"]
