Run

```
docker-compose build
```

Then 

```
docker-compose up
```

To get to page: 127.0.0.1:8007

To stop it from running: 

```
docker-compose down
```

To verify containers have been created: 
```
docker ps
```
Output should be: 
```
CONTAINER ID   IMAGE                COMMAND                  CREATED             STATUS             PORTS                    NAMES
d3d7fec3d2ba   flask-web            "python3 app.py"         About an hour ago   Up About an hour   0.0.0.0:8007->8007/tcp   flask-web-1
c5be34a561a4   redislabs/redismod   "redis-server --load…"   15 hours ago        Up About an hour   0.0.0.0:6379->6379/tcp   flask-redis-1
```