FROM python:3.9.0-alpine3.12


RUN apk update && apk upgrade


RUN pip3 install openpyxl && pip3 install flask
WORKDIR /opt/massage/


COPY app.py .
COPY config.py .
COPY templates ./templates

EXPOSE 5000

CMD ["python3", "./app.py"]