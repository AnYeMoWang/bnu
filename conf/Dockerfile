FROM ubuntu:14.04

MAINTAINER root

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ADD ./sources.list /etc/apt/
run apt-get update
run apt-get install -y build-essential git
run apt-get install -y python python-dev python-setuptools
run apt-get install -y nginx supervisor
run apt-get install -y libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms1-dev libwebp-dev
run easy_install pip

# ADD CODE
ADD ./bnu/ /tmp/bnu/

# run pip install
run pip install -r /tmp/bnu/requirements.pip


ADD ./duoshuo /tmp/duoshuo
run cd /tmp/duoshuo && python setup.py install

# set up all config
run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
run ln -s /tmp/bnu/conf/bnu_nginx.conf /etc/nginx/sites-enabled/
run ln -s /tmp/bnu/conf/bnu_supervisor.conf /etc/supervisor/conf.d/

expose 8080
cmd ["supervisord", "-n"]
