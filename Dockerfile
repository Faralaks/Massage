FROM python:3.9.0-alpine3.12


RUN apk update && apk upgrade


RUN pip3 install openpyxl && pip3 install flask && pip3 install pyTelegramBotAPI
WORKDIR /opt/massage/


COPY app.py .
COPY bot.py .
COPY config.py .
COPY templates ./templates
COPY static ./static

EXPOSE 80

CMD ["python3", "./app.py"]