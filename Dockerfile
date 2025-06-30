FROM apache/airflow:2.9.1-python3.10

USER root

RUN apt-get update && apt-get install -y sudo \
  && echo 'airflow ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER airflow
