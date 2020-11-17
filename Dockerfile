FROM python:3

WORKDIR /usr/src/app/
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY synapp ./synapp
WORKDIR /usr/src/app/synapp
RUN python manage.py migrate

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]