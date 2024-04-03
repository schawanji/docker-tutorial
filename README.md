https://www.youtube.com/watch?v=6OxqiEeCvMI

docker network ls
docker network inspect host
docker rm fastapi-container 
docker run --name fastapi-container -p 80:80 --network=host fastapi-image
docker run --name fastapi-container -p 80:80 --network=host -d fastapi-image
docker logs fastapi-container

docker run --name fastapi-container -p 80:80 --network=host -d -v $(pwd):/code fastapi-image