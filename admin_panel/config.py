from decouple import config

SECRET_KEY = config('SECRET_KEY')

DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')

ALLOWED_HOSTS = config('ALLOWED_HOSTS')

CORS_ALLOWED_ORIGINS_1 = config('CORS_ALLOWED_ORIGINS_1')
CORS_ALLOWED_ORIGINS_2 = config('CORS_ALLOWED_ORIGINS_2')

DEBUG = config('DEBUG')