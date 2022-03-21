# pull official base image
FROM python:3.10-alpine

# Pull base image
FROM python:3.8-slim-buster

# Install psql so that "python manage.py dbshell" works
RUN apt-get update -qq && apt-get install -y postgresql-client

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt