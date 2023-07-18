FROM node:16.20.0

WORKDIR /app

COPY package.json .

RUN yarn

COPY . .

CMD ["yarn", "start", "3004"]
