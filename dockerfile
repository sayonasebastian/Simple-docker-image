#Deriving the latest base image
FROM alpine:latest

LABEL Maintainer="nettiksn"
RUN apk --update add python3
RUN mkdir -p /home/data
RUN mkdir -p /home/output

WORKDIR /home

COPY words.py ./
COPY IF.txt /home/data
COPY Limerick.txt /home/data


CMD [ "python", "./words.py"]