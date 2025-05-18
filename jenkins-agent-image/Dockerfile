FROM maven:3.8.6-openjdk-17-slim

USER root

RUN apt-get update && \
    apt-get install -y docker.io && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN useradd -ms /bin/bash jenkins
USER jenkins

