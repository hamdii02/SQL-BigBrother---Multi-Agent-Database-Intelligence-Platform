FROM node:20-alpine

WORKDIR /frontend

COPY package*.json ./

# RUN npm install -g npm@latest

RUN npm install

COPY . .

# RUN npm run build 

# RUN npm install -g serve

EXPOSE 5173

# CMD ["serve", "-s", "dist", "-l", "5173"]
CMD ["npm", "run", "dev"]