FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["python", "admin_panel/manage.py", "runserver", "0.0.0.0:8000"]