 
FROM python:3.8.16-slim-buster
RUN apt update -y && apt install awscli -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app