# Ejecutar
- Ejecución del contenedor
  - **--name** cambiar el nombre
  - **-i** modo iterativo
  - **-t** abrir consola
  - **-d** ejecuta en segundo plano
  - **-p** indica el puerto donde el servicio del contenedor se expondra. 8080:80  <puerto del anfitrion>:<puerto de contenedor>
```
$ docker run <Image>
$ docker run <Image>:<tag>
```
- Ejecución iterativa
```
$ docker run -it <Image>
``` 
- Ejecutar comando interno en el contenedor. Mientras la tarea se ejecute, el contenedor no puede finalizar
```
$ docker run -d <Image> <Comando> 
```
- Ejecutar comando interno en el contenedor que está detenido, el contenedor no puede finalizar
```
$ docker exec -it <Image> <Comando>
$ docker exec -it <Image> bash
```
# Inspeccionar
- Descripción del contenedor
```
 $ docker inspect <name of Image>  
```

# Detener
- Detener un contenedor
```
$ docker stop <id o name>
```

# Listar
- Listado de ejecución o detenidos
  - **-a** muestra todos los contenedores, los que están detenidos
```
$ docker ps
```

# ELiminar
- ELiminar el contenedor 
```
$ docker rm <id_contenedor>
```
- Eliminar todos los contenedores detenidos
```
$ docker container prune
```

# Logs
- Visualizar logs
  - **-f** permite ver cada log a medida que va llegando.
  - **--tail  <un numero>** seguir las 10 ultimas entradas del log
```
$ docker logs proxy
```

# Bind mounts (Monturas de enlace)(Problemas de seguridad)
```
$ docker run -d --name <name of Image> -v <path anfitrion disco>:<path docker> <Image>
```
# Volumnenes
- **ls** listar volumenes
```
$ docker volume ls
```
- **create** crear volumenes
```
$ docker volume create dbdata
```
- Montar el volumen a un contenedor
  - **mount** volumen   
  - **src** define la fuente del volumen
  - **dst** define el destino del volumen 
```
crea el volumen
1. $ docker volume create dbdata
Indica el volumen creado y el directorio del contenedor. En caso de no estar docker crea el volumen
2. $ docker run -d --name <name of Image>  --mount src=dbdata,dst=/data/db mongo
Inspeccione Mounts
3. $ docker inspect <name of Image>  

```

## Copy
- **cp** permite copiar
- No hace falta que el contenedor se este ejecutando
```
$ docker cp <file of copy> <name of Image>:<path inside in image docker>/<new name of file copy>       - anfitrion ha contenedor
$ docker cp <name of Image>:<path inside in image docker>       - contenedor hacia anfitrion    

```

# History
- Permite visualizar el historial de comandos que se utilizaron por capas en la imagen
```
$ docker history <id_contenedor name_images>
```




# Imagens
- Cuando se crea un archivo Dockerfile
  - **t** tags
```
$ docker build -t <base_image>:<tag_image> <path Dockerfile context> o $ docker build -t <base_image> <path Dockerfile context>

$ docker build -t myapp .

```
- Cargar un contenedor de la nueva imagen
```
$ docker run -it <name_images>:<tag>   -Carga el contenedor con la imagen creada
```
- Desplieque de una mini app
```
$ docker run -d --rm -p 3000:3000 myapp
```
# Redes
- Listar redes
```
$ docker network ls
```
- Crear una nueva red
```
$ docker network create --attachable <name network>
```
- Inspeccionar
```
$ docker network inspect <name network>
```
- Conectar el contenedor a la red
```
$ docker network connect <name network> <name container>
```
