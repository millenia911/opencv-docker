## Simple face detection with OpenCV in docker container

There are two Docker images that used here. The image for front-end hosting and image for the image processing. Both hosted with Flask.

To run in swarm, edit replicas number in .yml file, attach your desired volume, then initiate the swarm mode:
```sh
docker swarm init
```
then
```sh
docker stack deploy -c docker-compose.yml compose_name
```

Running front-end container can be acesses via localhost:5000, but the image processing API live in port 8080.

To pull images only without running:
```sh
docker-compose pull
```
