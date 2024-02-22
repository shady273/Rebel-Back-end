# Volunteering Site Backend and Admin Panel

## Project Overview

This project represents the backend part and admin panel for a volunteering website.

## Running the Project

### Using HTTPS Protocol

To run the project on the HTTPS protocol, start by generating a certificate:

```bash
# Generate a certificate
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout key.pem -out cert.pem
```
## Nginx Configuration

Nginx is used to configure routing and serve static files. Below is an example of an nginx configuration file:

```bash
server {
    listen 80;
    server_name localhost;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name localhost;
    ssl_certificate /sslcert/cert.pem;
    ssl_certificate_key /sslcert/key.pem;

    location / {
        proxy_pass http://django:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_set_header X-CSRFToken $cookie_csrf_token;
        proxy_pass_request_headers on;
        proxy_set_header X-Forwarded-Method $request_method;
        proxy_set_header X-Forwarded-Ssl on;
    }

    location /static/ {
        alias /static/;
    }
}
```

## Running with Docker Compose
To create containers and run them, use the following command:
```commandline
docker-compose up --build
```

## Accessing the Admin Panel
After a successful launch, the admin panel will be accessible at:

For HTTPS protocol: https://127.0.0.1:8080/admin

For HTTP protocol: http://127.0.0.1:8000/admin