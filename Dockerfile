FROM python:3.8

RUN apt update -y && apt install aswcli -y 
WORKDIR /app 


COPY . /app 
RUN pip install -r requirements.txt

CMD ['python3' , 'app.py']