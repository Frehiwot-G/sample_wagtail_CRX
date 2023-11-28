# FROM python:3.10
FROM arm64v8/python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . /app/

EXPOSE 8000

RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sample_website.wsgi:application"]

