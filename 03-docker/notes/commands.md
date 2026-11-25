## Docker commands

- Show docker version
```bash
docker version
```
- Show docker daemon (container counts, runtimes, storage and engne information)
```bash
docker info
```
- Pull the lightweight nginx image from registry to local image store
```bash
docker pull nginx:alpine

# alpine is a lightwight linux distribution
```

- List docker images 
```bash
docker images

#images are templates, containers are instances created from them
```

- Run NGINX in the background as web and map port 8080 to 80.
```bash
docker run -d --name web -p 8080:80 nginx:alpine

#  -d = run in background and show the terminal
#  --name web = give the container name "web"
#  -p 8080:80 = map host port to container port

```

- List running containers 
```bash
docker ps
#  Shows which services a re currently running
# -a flag shows the running and stopped processes
```

- Show logs from web container 
```bash
docker logs web
```

- Start/Stop web container 
```bash
docker start web
docker stop web
```

- Show the web container hostname
```bash
docker exec web hostname
# executes the hostname command inside the web container's terminal
```

- Inspect all metadata for web container
```bash
docker inspect web
# inspect exposes the id(conatiner hostname), the state, mounts, networking, environment variables and port bindings
```

- Build image form docker file and give a tag
```bash
docker build -t devops-api:1.0 .
# devops-api is the name of the image
# -t flag for the tag in this case it is 1.0
# . copies all files from the from the local current directory to the container with the instruction "COPY" in tbe dockerfile
```

- Create a docker volume 
```bash
docker volume create pgdata
# a volume is where containers data is stored even if the container is deleted 
#pgdata is the vulume name
```

- Create a briged network
```bash
docker network create appnet
# the bridged network lets containers to communicate with each other on the same computer using their name rather ther thei ip addresses 
#appnet is the network name
```

- Connecte a container to a network
```bash
docker connect create appnet nginx
# appnet is the network name , nginx is the container which we connect
```

- Run PostgreSQL 16 in the background as a container named db, on appnet, with the pgdata volume at /var/lib/postgresql/data and POSTGRES_PASSWORD set to secret.
```bash
docker run -d --name db --network appnet -v pgdata:/var/lib/postgresql/data -e POSTGRES_PASSWORD=secret postgres:16-alpine

# -d flag run the process in background(detached)
# --name flag is the container name(db)
# --network flag attaches the conatainer(bd) to the the network(appnet)
# -v = flag mounts the named volume so the data survives container removal.Other containers on appnet can connect to db:5432 without publishing the port to the host.
```
- List docker network
```bash
docker network ls
```

- create and start containersDocker compose 
```bash
docker compose up -d
# if the container's config ave image has change , this command recreates it
```