#!/bin/bash
read -t 30 -p "input images name:" images
container = $(docker ps -a | awk '/$images/{print $1}')
docker stop $(docker ps -a | awk '/' $container'/{print $1}')
read -t 30 -p "yes or no delete the CONTAINER:" choice
if [ "$choice" = "y" -o "$choice" = "Y"];then
	docker rm $(docker ps -a | awk '/'$images'/{print $1}')