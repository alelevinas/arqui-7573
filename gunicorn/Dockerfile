FROM python:3.4-alpine

ADD ./static/. /home/www/arqui/static/

ADD ./gunicorn/. /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:8080 app:app
