FROM ubuntu:trusty
RUN apt-get update; apt-get install -y python-pip python-dev libssl-dev libffi-dev build-essential
RUN pip install --upgrade pip urllib3[secure] ndg-httpsclient pyasn1 pyopenssl
