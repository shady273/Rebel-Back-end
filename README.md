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
Modify the CMD in your Dockerfile as follows:

```
CMD ["python", "admin_panel/manage.py", "runserver_plus", "0.0.0.0:8080", "--cert-file", "cert.pem", "--key-file", "key.pem"]
```

Using HTTP Protocol
If you are using HTTP, certificates are not required. Change the CMD in your Dockerfile to:
```commandline
CMD ["python", "admin_panel/manage.py", "runserver", "0.0.0.0:8000"]
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