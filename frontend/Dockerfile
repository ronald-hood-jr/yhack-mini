# Installs Node.js image
FROM node

# Make folder to put our files in
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/frontend

# Set working directory so that all
# subsequent command runs in this folder
WORKDIR /usr/src/app/frontend

# Copy package json and install dependencies
COPY package*.json ./
RUN yarn

# Copies everything in the src directory to WORKDIR/src
COPY . .

# Expose port to access server
EXPOSE 3000

# Command to run our app
CMD [ "yarn", "start" ]