FROM python:3.9-alpine
RUN mkdir /django_blog
WORKDIR /django_blog
ADD requirements.txt .
RUN apk update && \
apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev && \
python -m pip install --upgrade pip && \
pip install -r requirements.txt
ADD . .