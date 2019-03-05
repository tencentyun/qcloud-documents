本文档旨在介绍如何通过 Docker Compose 搭建一个简单的 registry 环境，使用 DockerHub 官方镜像，registry 镜像版本 为`registry:2.5.0`， nginx 镜像版本为 `nginx:1.11.5`。这里主要介绍 registry 环境的搭建及使用，更详细的企业级 registry 服务器的搭建可参阅开源的 [Harbor](https://github.com/vmware/harbor "Harbor")。

## registry 概述
registry 是 Docker 的镜像存储服务，DockerHub 上的 registry 镜像见 [Registry 官方镜像](https://hub.docker.com/_/registry/ "Registry官方镜像")，更多详细信息请转至 [GitHub](https://github.com/docker/distribution "源码") 查看最新源码 。

## 搭建 registry
- 在服务器上执行如下命令安装 Docker，这里选择腾讯云（Ubuntu Server 14.04.1 LTS 64位）镜像来创建服务器。
```
curl -fsSL https://get.docker.com/ | sh
```
- 安装 Docker Compose
Docker Compose 是一个定义及运行多个 Docker 容器的工具。使用 Docker Compose 只需要在一个配置文件中定义多个 Docker 容器，再使用一条命令将多个容器启动，Docker Compose 会通过解析容器间的依赖关系，按先后顺序启动所定义的容器。有关 Docker Compose 详情请转至 [GitHub](https://github.com/docker/compose) 了解。
```
  curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-compose-$(uname -s)-$(uname -m) > /usr/local/bin/docker-compose
  chmod a+x /usr/local/bin/docker-compose
```    
- 启动 registry 服务，此例中包含 nginx 和 registry 两个容器，涉及的配置文件请参见附录。
```
docker-compose up -d
```
- 停止服务。
```
  docker-compose stop
```
- 重启服务。
```
  docker-compose restart
```
- 下线服务。
```
  docker-compose down
```

## 镜像基本操作
### 上传镜像
- 因为搭建的 registry 服务使用 HTTP 协议，所以 Docker 启动参数需要配置 `--insecure-registry localhost` 选项，修改 `/etc/default/docker` 文件如下：
```
DOCKER_OPTS="--insecure-registry localhost"
```
- 重启 Docker。
```
  service docker restart
```
- 拉取上传镜像 docker pull；docker tag；docker push ( tag 默认为 latest )。
```
  docker pull hello-world
  docker tag hello-world localhost/library/hello-world
  docker push localhost/library/hello-world
```
 
### 下载镜像
```
   docker pull localhost/library/hello-world
```

### 删除镜像
```
    docker rmi localhost/library/hello-world
```

## 获取镜像
### 获取镜像仓库列表
```
    # curl http://localhost/v2/_catalog
    {"repositories":["library/hello-world"]}
```
未上传镜像前的输出如下：
```
    # curl http://localhost/v2/_catalog
    {"repositories":[]}
```

### 获取镜像 tag 列表
```
    # curl -X GET http://localhost/v2/library/hello-world/tags/list
    {"name":"library/hello-world","tags":["latest"]}
```

### 获取镜像 manifests 信息
```
    # curl -H "Accept: application/vnd.docker.distribution.manifest.v2+json"  -X GET http://localhost/v2/library/hello-world/manifests/latest
    {
       "schemaVersion": 2,
       "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
       "config": {
          "mediaType": "application/vnd.docker.container.image.v1+json",
          "size": 1473,
          "digest": "sha256:c54a2cc56cbb2f04003c1cd4507e118af7c0d340fe7e2720f70976c4b75237dc"
       },
       "layers": [
          {
             "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
             "size": 974,
             "digest": "sha256:c04b14da8d1441880ed3fe6106fb2cc6fa1c9661846ac0266b8a5ec8edf37b7c"
          }
       ]
    }
```
其中 `c54a2cc56cbb2f04003c1cd4507e118af7c0d340fe7e2720f70976c4b75237dc` 即为执行 docker images 时显示的 IMAGE ID。
layers 表示了镜像的层次关系，可以通过 layers 中的 digest 来拉取 blob，详情见下面获取镜像 blob。

### 获取镜像 blob
在上面获取 hello-world:latest 镜像的 manifests 信息中只有一个 layer，以此为例来说明如何获取镜像 blob。拉取的结果显示获取的 blob 与文件 sha256 是一致的。**执行 docker pull 实际上就是先获取到镜像的 manifests 信息，再拉取 blob**。
```
    # curl -s -X GET http://localhost/v2/library/hello-world/blobs/sha256:c04b14da8d1441880ed3fe6106fb2cc6fa1c9661846ac0266b8a5ec8edf37b7c -o hello-world.blob
    # ls -l hello-world.blob 
    -rw-r--r-- 1 root root 974 Nov 23 09:56 hello-world.blob
    # sha256sum hello-world.blob 
    c04b14da8d1441880ed3fe6106fb2cc6fa1c9661846ac0266b8a5ec8edf37b7c  hello-world.blob  
```

## 删除镜像
### 删除镜像（ soft delete ）
首先通过 curl -i 参数获取到镜像的 `Docker-Content-Digest`，registry 2.3 版本及以后的版本必须在 header 中指定 `Accept: application/vnd.docker.distribution.manifest.v2+json`，否则默认返回的是 schema1 的 digest，与 schema2 的 digest 不同，使用不指定上述头信息返回的 digest 删除时会返回 404。
```
    # curl -i -H "Accept: application/vnd.docker.distribution.manifest.v2+json"  -X GET http://localhost/v2/library/hello-world/manifests/latest
    
    HTTP/1.1 200 OK
    Server: nginx/1.11.5
    Date: Wed, 23 Nov 2016 02:17:51 GMT
    Content-Type: application/vnd.docker.distribution.manifest.v2+json
    Content-Length: 524
    Connection: keep-alive
    Docker-Content-Digest: sha256:a18ed77532f6d6781500db650194e0f9396ba5f05f8b50d4046b294ae5f83aa4
    Docker-Distribution-Api-Version: registry/2.0
    Etag: "sha256:a18ed77532f6d6781500db650194e0f9396ba5f05f8b50d4046b294ae5f83aa4"
    
    {
       "schemaVersion": 2,
       "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
       "config": {
          "mediaType": "application/vnd.docker.container.image.v1+json",
          "size": 1473,
          "digest": "sha256:c54a2cc56cbb2f04003c1cd4507e118af7c0d340fe7e2720f70976c4b75237dc"
       },
       "layers": [
          {
             "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
             "size": 974,
             "digest": "sha256:c04b14da8d1441880ed3fe6106fb2cc6fa1c9661846ac0266b8a5ec8edf37b7c"
          }
       ]
    }
```
根据上一步返回的 `Docker-Content-Digest` 删除，返回 202 表示删除成功。
```
    # curl -k -v -s -X DELETE http://localhost/v2/library/hello-world/manifests/sha256:a18ed77532f6d6781500db650194e0f9396ba5f05f8b50d4046b294ae5f83aa4

    * Hostname was NOT found in DNS cache
    *   Trying 127.0.0.1...
    * Connected to localhost (127.0.0.1) port 80 (#0)
    > DELETE /v2/library/hello-world/manifests/sha256:a18ed77532f6d6781500db650194e0f9396ba5f05f8b50d4046b294ae5f83aa4 HTTP/1.1
    > User-Agent: curl/7.35.0
    > Host: localhost
    > Accept: */*
    > 
    < **HTTP/1.1 202 Accepted**
    * Server nginx/1.11.5 is not blacklisted
    < Server: nginx/1.11.5
    < Date: Wed, 23 Nov 2016 02:29:59 GMT
    < Content-Type: text/plain; charset=utf-8
    < Content-Length: 0
    < Connection: keep-alive
    < Docker-Distribution-Api-Version: registry/2.0
    < 
    * Connection #0 to host localhost left intact
```
确认结果：
```
    # curl -X GET http://localhost/v2/library/hello-world/tags/list
    {"name":"library/hello-world","tags":null}
```

### 删除镜像（ hard delete ）
在上一步中，只是删除了镜像的 manifests 信息，引用的 blob 还在占用磁盘空间，执行如下命令可以查看可以删除的 blob。 
```
  docker exec -it myregistry_registry_1 /bin/registry garbage-collect --dry-run /etc/registry/config.yml
```
要删除 blob，释放磁盘空间，需要执行下面的命令。
>**注意：**
>在执行下面的命令时 registry 必须是只读模式（只读模式可在 registry 配置文件中设置），否则可能会导致数据不一致。 
```
  docker exec -it myregistry_registry_1 /bin/registry garbage-collect /etc/registry/config.yml
```

## 附录
### 目录结构
    .
    |-- config
    |   |-- nginx
    |   |   `-- nginx.conf
    |   `-- registry
    |       `-- config.yml
    `-- docker-compose.yml
    
### nginx.conf
    worker_processes auto;
    
    events {
      worker_connections 1024;
      use epoll;
      multi_accept on;
    }
    
    http {
      tcp_nodelay on;
    
      # this is necessary for us to be able to disable request buffering in all cases
      proxy_http_version 1.1;
    
    
      upstream registry {
        server registry:5000;
      }
    
    
      server {
        listen 80;
    
        # disable any limits to avoid HTTP 413 for large image uploads
        client_max_body_size 0;
    
        location /v1/ {
          return 404;
        }
    
        location /v2/ {
          proxy_pass http://registry/v2/;
          proxy_set_header Host $http_host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          
          # When setting up Harbor behind other proxy, such as an Nginx instance, remove the below line if the proxy already has similar settings.
          proxy_set_header X-Forwarded-Proto $scheme;
          
          proxy_buffering off;
          proxy_request_buffering off;
    
        }
    
      }
    }

### config.yml
    version: 0.1
    log:
      level: debug
      fields:
        service: registry
    storage:
        cache:
            layerinfo: inmemory
        filesystem:
            rootdirectory: /var/lib/registry
        maintenance:
            uploadpurging:
                enabled: false
            readonly:
                enabled: false
        delete:
            enabled: true
    http:
        addr: :5000
        secret: yoursecret
    
### docker-comose.yaml
    version: '2'
    services:
      registry:
        image: library/registry:2.5.0
        restart: always
        volumes:
          - /data/registry:/var/lib/registry
          - ./config/registry/:/etc/registry/
        environment:
          - GODEBUG=netdns=cgo
        command:
          ["serve", "/etc/registry/config.yml"]
      proxy:
        image: library/nginx:1.11.5
        restart: always
        volumes:
          - ./config/nginx:/etc/nginx
        ports:
          - 80:80
          - 443:443
        depends_on:
          - registry

  [1]: https://cloud.tencent.com/
  [2]: https://github.com/docker/compose
