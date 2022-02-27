## Simple face detection with docker

There are two images that used here. The image for front-end hosting and image for the image processing. Both hosted with Flask.

Simply run 
```sh
docker-compose up
```
in the docker-compose.yml directory to run only one container each.

To run in swarm:
```sh
docker swarm init
```
then
```sh
docker stack deploy -c docker-compose.yml compose_name
```

Running front-end container can be acesses via localhost:5000, but the image processing API live in port 8080.


