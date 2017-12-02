FROM node:alpine

ADD ./node/. /code

WORKDIR /code

RUN npm install

ADD ./static/. /home/www/arqui/static

CMD ["npm", "start"]
