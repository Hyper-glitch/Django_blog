FROM python:3.9-alpine
RUN mkdir /django_blog
WORKDIR /django_blog
ADD requirements.txt .
RUN apk add gcc python3-dev musl-dev jpeg-dev zlib-dev && pip install -r requirements.txt
ADD . .
ENTRYPOINT ["python", "manage.py", "migrate"]
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
