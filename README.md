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

<ul>
  <li>Download docker_project_sn.tar file</li>

  <li>Load image</li>
  `` 
  docker load --input docker_project_sn.tar
  ``
  <li>Check images</li>
  `` 
  docker images
  ``
  <li>Run container image</li>
  `` 
  docker run docker_project3
  ``
</ul>
