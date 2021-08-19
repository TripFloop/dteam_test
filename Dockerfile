FROM nginx/unit:1.23.0-python3.9

# set work directory
WORKDIR /web/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install postgresql-client -y && apt-get install -y binutils libproj-dev gettext libcairo2

RUN pip install --upgrade pip

COPY requirements.txt /web/app/requirements.txt

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . /web/app

RUN python manage.py collectstatic --noinput --clear
