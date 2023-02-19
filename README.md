# Simple-docker-image
Running a python script using docker

## Python script 
Reading 2 text files and displaying information such as word count and words maximun word count

## Dockerfile
Using alpine base image
Installing python and creating required directories
Setting working directory 
Copying supported text files
Setting command to run python script

## Installation 

Make sure you have docker installed

Download docker_project_sn.tar file

Load image

```
$ docker  load --input docker_project_sn.tar
```
Check images
```
$ docker  images
```
Run container image
```
$ docker  run docker_project3
```
