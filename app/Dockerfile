FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive
# prevent 404 in apt-get update 
# ref: https://stackoverflow.com/questions/37706635/in-docker-apt-get-install-fails-with-failed-to-fetch-http-archive-ubuntu-com#answer-37708927
RUN sed -i'' 's/archive\.ubuntu\.com/us\.archive\.ubuntu\.com/' /etc/apt/sources.list
RUN rm -rf /var/lib/apt/lists/*

RUN  apt update
RUN apt install -y software-properties-common 
RUN add-apt-repository ppa:deadsnakes/ppa 
RUN apt-get update
RUN apt-get install -y locales curl\
  && locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8'
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
# https://github.com/librosa/librosa/issues/757#issuecomment-412095512
# RUN apt-get install -y libatlas-base-dev
RUN apt-get install -y llvm-10
RUN ln -s /usr/bin/llvm-config-10 /usr/bin/llvm-config
ENV LLVM_CONFIG=/usr/bin/llvm-config

RUN apt-get install -y python3.9 python3.9-distutils libsndfile1
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.9 get-pip.py 
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt