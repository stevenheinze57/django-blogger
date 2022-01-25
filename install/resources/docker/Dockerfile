FROM ubuntu

RUN mkdir -p /opt/blogger_ui/src/ && \
    mkdir /opt/blogger_ui/scripts/ && \
    mkdir /opt/blogger_ui/logs/ && \
    mkdir /mnt/env-files/

RUN touch /opt/blogger_ui/logs/blogger_ui.log
ADD src/ /opt/blogger_ui/src/
ADD install/resources/docker/scripts/ /opt/blogger_ui/scripts/
ADD install/conf/local/files/ /mnt/env-files/

RUN chmod -R 755 /opt/blogger_ui/scripts/*

ENV BLOGGER_CONFIG_FILE_PATH=/mnt/env-files/blogger_settings.ini

RUN apt-get update -y
RUN apt-get install python3 python3-pip libpq-dev python3-dev -y

EXPOSE 80

RUN pip3 install -r /opt/blogger_ui/src/requirements.txt

#RUN cd /opt/blogger_ui/src/app/ && \
#    python3 manage.py test

ENTRYPOINT cd /opt/blogger_ui/src/app/ && \
    python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    python3 manage.py loaddata /mnt/env-files/blogger.fixture.json && \
    python3 manage.py test && \
    python3 manage.py runserver 0.0.0.0:80 >> /opt/blogger_ui/logs/blogger_ui.log 2>&1
