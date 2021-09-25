FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . ./app
RUN /bin/bash -c "source app/venv/bin/activate && pip install -r app/requirements.txt && python3 app/manage.py makemigrations token_authentication && python3 app/manage.py migrate"
ENTRYPOINT /bin/bash -c "python3 app/manage.py runserver localhost:8000"
EXPOSE 8000 8000 
