git add 1
git status – to check the file status
git commit -m “commit message” (files available in local repository)
git log – it shows commit history
git log --oneline – shows commit history in single line.
1 FROM
Purpose: Specifies the base image for the container.
Syntax:
FROM <image>:<tag>
Example:
FROM node:18
This sets the base image as Node.js version 18.
2  MAINTAINER (Deprecated)
Purpose: Used to specify the author/maintainer of the image (deprecated in favor of LABEL).
Syntax:
MAINTAINER Name <email@example.com>
Example:

MAINTAINER John Doe <john@example.com>
Instead, use LABEL:
LABEL maintainer="John Doe <john@example.com>"
Docker Network
===============
Bridge
The bridge driver creates an internal network within a single Docker host containers placed within this network can communicate with each other but are isolated from containers, not on the internal network, bridge is the default driver when running single containers or when using docker-compose.

Host
When using the host driver, the container shares the network stack of the Docker host appearing as if the container is the host itself, from a networking perspective.

None
The none driver simply disables networking for a container, making it isolated from other containers.

sudo hostnamectl set-hostname <required name>
sudo apt install net-tools -y
ifconfig
sudo docker network ls
sudo docker run -itd --name <container name> -p <Container port:host port> <image name>
sudo docker run -itd --name <container name> --net host <image name>
sudo docker run -itd --name <container name> --net none <image name>
