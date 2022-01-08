FROM python:3.9
RUN mkdir /django_blog
WORKDIR /django_blog
ADD . .
RUN pip install -r requirements.txt
VOLUME ["/django_blog/volume"]
ENTRYPOINT ["python", "manage.py", "migrate"]
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]