FROM ubuntu:20.04

RUN apt-get -yqq update
RUN apt-get -yqq upgrade
RUN apt  -yqq install python3-pip
RUN pip3 install openpyxl
RUN pip3 install flask

RUN mkdir /opt/massage/

# copy our application code
ADD app.py /opt/massage/
ADD db_creator.py /opt/massage/
ADD db.sqlite /opt/massage/
ADD templates /opt/massage/templates
WORKDIR /opt/massage/

#RUN python3 ./db_creator.py

EXPOSE 5000

# run the application
CMD ["python3", "./app.py"]