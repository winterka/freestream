FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3 build-essential
RUN mkdir -p /usr/src/freestream
RUN mkdir -p /usr/src/freestream/backend
COPY . /usr/src/freestream/backend
WORKDIR /usr/src/freestream/backend
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
