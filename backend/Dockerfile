# Installs Node.js image
FROM node

# Make folder to put our files in
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/backend

# sets the working directory for any RUN, CMD, COPY command
# all files we put in the Docker container running the server will be in /usr/src/app (e.g. /usr/src/app/package.json)
WORKDIR /usr/src/app/backend

# Copies package.json, package-lock.json, tsconfig.json, .env to the root of WORKDIR
COPY package*.json ./

RUN yarn

# Copies everything in the src directory to WORKDIR/src
COPY . .


EXPOSE ${PORT}

# Installs all packages
RUN yarn

# Runs the dev npm script to build & start the server
CMD ["yarn", "dev"]
