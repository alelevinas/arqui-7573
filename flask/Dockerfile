FROM python:3.4-alpine

ADD ./static/. /home/www/arqui/static/

ADD ./flask/. /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
