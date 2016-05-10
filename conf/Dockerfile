FROM ubuntu:14.04

MAINTAINER root

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ADD ./sources.list /etc/apt/
run apt-get update
run apt-get install -y build-essential git
run apt-get install -y python python-dev python-setuptools
run apt-get install -y nginx supervisor
run easy_install pip

# install uwsgi now because it takes a little while
run pip install uwsgi

# install nginx
# run apt-get install -y python-software-properties
# run apt-get update
# run add-apt-repository -y ppa:nginx/stable

# add oracle env
COPY ./oracle/ /opt/oracle/

# add project code
ADD ./GMSOC/ /opt/GMSOC/

run apt-get install libaio1

ENV ORACLE_HOME /opt/oracle/instantclient_11_2
ENV LD_LIBRARY_PATH /opt/oracle/instantclient_11_2
ENV DYLD_LIBRARY_PATH /opt/oracle/instantclient_11_2

run env

# run pip install

run pip install -r /opt/GMSOC/requirements.txt


# set up all config
run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
run ln -s /opt/GMSOC/gm_nginx.conf /etc/nginx/sites-enabled/
run ln -s /opt/GMSOC/gm_supervisor.conf /etc/supervisor/conf.d/
run python /opt/GMSOC/create_config.py

expose 8080
cmd ["supervisord", "-n"]
