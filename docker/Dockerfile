FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev

# Копируем все файлы приложения в рабочую директорию в контейнере
COPY ./ /app

EXPOSE 8000