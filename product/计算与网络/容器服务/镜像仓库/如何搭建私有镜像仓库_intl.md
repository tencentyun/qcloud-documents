## Introduction
This document describes how to build a simple Registry environment through Docker Compose. Here, we use official DockerHub image. Registry image tag: `registry:2.5.0`; nginx image tag: `nginx:1.11.5`. This document focuses on how to build and use Registry environment. For more information on how to build an enterprise-level Registry server, please see open-source [Harbor](https://github.com/vmware/harbor "Harbor")。

## What is Registry?
Registry is a storage service for Docker images. Registry images on DockerHub can be found in [Official Registry Images](https://hub.docker.com/_/registry/ "Official Registry Images"). For more information, please [go to GitHub to see the latest source codes](https://github.com/docker/distribution "source codes").

## Build Registry

 - Install Docker by executing the following command on the CVM. Here, we choose [Tencent Cloud](https://cloud.tencent.com/ "Tencent Cloud") (Ubuntu Server 14.04.1 LTS 64-bit) image to create the CVM.
```
curl -fsSL https://get.docker.com/ | sh
```

 - Install Docker-compose
Docker Compose is a tool used to define and run multiple Docker containers. To use Docker Compose, simply define multiple Docker containers in a configuration file, and then launch the containers by executing a command. Docker Compose will launch the defined containers in sequential order by resolving the dependency between these containers.
[Go to GitHub for more information about Docker Compose >>](https://github.com/docker/compose)
```
  curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-compose-$(uname -s)-$(uname -m) > /usr/local/bin/docker-compose
  chmod a+x /usr/local/bin/docker-compose
```    
 - Launch Registry service. In this example, there are two containers: nginx and registry. Related configuration files can be found in Appendix.
```
docker-compose up -d
```
 - Stop the service.
```
  docker-compose stop
```

 - Restart the service.
```
  docker-compose restart
```

 - Deactivate the service.
```
  docker-compose down
```

## Upload Image

 - Since the Registry service we built is an HTTP service, you need to configure Docker launch parameters with `--insecure-registry localhost` option, and modify the `/etc/default/docker` file.
```
DOCKER_OPTS="--insecure-registry localhost"
```

 - Restart Docker.
```
  service docker restart
```

 - Pull and upload the image "docker pull;docker tag;docker push" (tag is "latest" by default).
```
  docker pull hello-world
  docker tag hello-world localhost/library/hello-world
  docker push localhost/library/hello-world
```
 
## Download Image

```
   docker pull localhost/library/hello-world
```

## Delete Image

```
    docker rmi localhost/library/hello-world
```

## Acquire Image Repository List

```
    # curl http://localhost/v2/_catalog
    {"repositories":["library/hello-world"]}
```

Before the image is uploaded, the output is as follows:
```
    # curl http://localhost/v2/_catalog
    {"repositories":[]}
```

## Acquire Image Tag List

```
    # curl -X GET http://localhost/v2/library/hello-world/tags/list
    {"name":"library/hello-world","tags":["latest"]}
```

## Acquire Image Manifests Information

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

`c54a2cc56cbb2f04003c1cd4507e118af7c0d340fe7e2720f70976c4b75237dc` is the IMAGE ID shown when you execute "docker images".
"layers" indicates the hierarchy of images. "blob" can be pulled through "digest" in "layers". For more information on how to acquire image blob, please see below.

## Acquire Image blob

There is only one "layer" in the "manifests" information of "hello-world:latest" image acquired above. We use this as an example to see how to acquire image blob. As shown in the pulling result, the blob we acquired is consistent with file's sha256. **Executing "docker pull" is actually a process to acquire the manifests information of the image, before pulling blob**.

```
    # curl -s -X GET http://localhost/v2/library/hello-world/blobs/sha256:c04b14da8d1441880ed3fe6106fb2cc6fa1c9661846ac0266b8a5ec8edf37b7c -o hello-world.blob
    # ls -l hello-world.blob 
    -rw-r--r-- 1 root root 974 Nov 23 09:56 hello-world.blob
    # sha256sum hello-world.blob 
    c04b14da8d1441880ed3fe6106fb2cc6fa1c9661846ac0266b8a5ec8edf37b7c  hello-world.blob  
```

    
## Delete Image (Soft Delete)

First, acquire `Docker-Content-Digest` of the image using parameter "curl -i". For Register 2.3 and future versions, you must specify `Accept:  application/vnd.docker.distribution.manifest.v2+json` in the header, otherwise the "digest" of "schema1" is returned by default, which is different from that of "schema2". If you delete using a "digest" that is not returned by specifying the header above, you will receive a 404 error.

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


 When deleting image using the `Docker-Content-Digest` returned in the previous step, you will receive the 202 code, indicating that the deletion is successful.
 
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

 Confirm result:
 
```
    # curl -X GET http://localhost/v2/library/hello-world/tags/list
    {"name":"library/hello-world","tags":null}
```

## Delete Image (Hard Delete)

In the previous step, you only deleted the manifests information of the image, while some disk space is still occupied by the referenced "blob". Execute the following command to see deletable "blob".
  
```
  docker exec -it myregistry_registry_1 /bin/registry garbage-collect --dry-run /etc/registry/config.yml
```

To free disk space, execute the following command to delete "blob". Note that **Registry must be set as read-only when you execute the command below (read-only mode can be set in the Registry configuration file)**, otherwise data inconsistency may occur.
  
```
  docker exec -it myregistry_registry_1 /bin/registry garbage-collect /etc/registry/config.yml
```


## Appendix

### Directory Structure
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
