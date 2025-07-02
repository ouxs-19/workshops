FROM php:7.0-apache
COPY app /var/www/html
WORKDIR /var/www/html
RUN php setup.php && rm -f setup.php
