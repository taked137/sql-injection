FROM centos:latest
RUN dnf install -y python3
RUN dnf install -y sqlite 
RUN pip3 install tornado
RUN dnf install -y php
RUN dnf install -y php-pdo
#RUN apt install -y python3.8
#RUN apt install -y pip3
