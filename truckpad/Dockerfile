# pull official base image
FROM python:3.8.2-slim

# set work directory
WORKDIR /usr/src/truckpad

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y libffi-dev libpq-dev gcc python3-dev musl-dev netcat\
    && apt-get install -y --no-install-recommends binutils libproj-dev gdal-bin \
    && pip install -U pip setuptools \
    && pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "/usr/src/truckpad/"]

RUN pipenv install

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/truckpad/entrypoint.sh

# copy projectgit
COPY . /usr/src/truckpad/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/truckpad/entrypoint.sh"]