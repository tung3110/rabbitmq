#!/bin/sh
#docker rmi  tungnh2022/apihello:latest
docker container stop $(docker container ls -q --filter ancestor=tungnh2022/apihello:latest)
docker pull tungnh2022/apihello:latest
docker run -d -p 3000:3000 tungnh2022/apihello:latest
