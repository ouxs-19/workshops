# Source image
FROM ubuntu:latest

# Update
RUN apt update

# Install dependencies
RUN apt install -y apache2 inetutils-ping 
ARG DEBIAN_FRONTEND=noninteractive
RUN apt install -y php

# Cleanup
RUN rm -rf /var/www/html

# Copy challenge files
COPY html /var/www/html

# Just to show case the bug 
RUN chmod -R 777 /var/www/html

# Expose challenge's port
EXPOSE 80

# Launch web server
ENTRYPOINT service apache2 start && tail -f /dev/null
