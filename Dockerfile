FROM python:3.8-slim-buster

WORKDIR D:\Flask\location

RUN mkdir -p /opt/flask/location/send_location

COPY ./send_location /opt/flask/location/send_location

RUN pip3 install -r /opt/flask/location/send_location/requirement.txt

CMD [ "python3", "/opt/flask/location/send_location/app.py" ]