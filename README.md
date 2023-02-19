# Simple-docker-image
Running a python script using docker

## Python script 
Reading two text files and displaying information such as word count and words with maximum occurrences in the file

## Dockerfile
Using an alpine base image
Installing python and creating required directories
Setting working directory 
Copying supported text files
Setting the command to run the python script

## Installation 

Make sure you have docker installed.

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
