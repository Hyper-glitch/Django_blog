FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_blog
WORKDIR /django_blog
COPY requirements.txt /django_blog/
RUN pip install -r requirements.txt
COPY . /django_blog/