docker build -t docker_imagen_prueba .
docker run -d --name docker_contenedor_prueba -p 80:80 docker_imagen_prueba

pause

docker container stop docker_contenedor_prueba
docker container rm docker_contenedor_prueba
docker image rm -f docker_imagen_prueba