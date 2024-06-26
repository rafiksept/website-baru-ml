# Gunakan image Python resmi sebagai base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Buat direktori untuk source code app
WORKDIR /app

# Install dependencies system
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Install pipenv dan dependencies proyek
# COPY Pipfile Pipfile.lock /app/
# RUN pip install pipenv && pipenv install --deploy --ignore-pipfile


# Install any needed packages specified in requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
RUN gdown https://drive.google.com/uc?id=1jc-4IpojaRaBuR_VQxcJUH3W5qnmOQ3o
# Salin source code proyek
COPY . /app/

# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate
# Expose port untuk Django
EXPOSE 8000

# Jalankan entrypoint script
CMD ["./entrypoint.sh"]
