FROM node:20-slim

WORKDIR /app

COPY --chown=node:node ./app/ .

RUN npm install

ENV NODE_ENV production

USER node 
 
CMD ["npm", "start"]