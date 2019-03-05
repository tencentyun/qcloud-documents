## docker run Parameter Adaptation

  This document describes how to match parameters of docker run and Tencent Cloud container console when migrating a container that is debugged in the local docker to Tencent CCS platform. Here we take creating a simple gitlab service as an example.

### 1. Sample of gitlab Container Parameter
We can create a simple gitlab container using the following docker run commands:

```shell
docker run \
-d \
-p 20180:80 \
-p 20122:22 \
--restart always \
-v /data/gitlab/config:/etc/gitlab \
-v /data/var/log/gitlab:/var/log/gitlab \
-v /data/gitlab/data:/var/opt/gitlab \
--name gitlab \
gitlab/gitlab-ce:8.16.7-ce.0

```



`-d`: Container runs in the backend. You do not need to specify this parameter in the container console, because containers always run in the backend of the container platform.

`-p`: Specifies port mapping. Here we have two port mappings. The container ports are 80 and 22, and the exposed ports are 20180 and 20122. Correspondingly, we add two port mapping rules in the console, and enter the corresponding container port and service port. Since the gitlab need to be accessed from public network, **Via Internet** is selected as the access method.
![](https://mc.qcloudimg.com/static/img/cf73ee3d941a768491d52af56a386db4/image.png)

`--restart`: Specifies whether to restart the container when it exits. You do not need to specify this parameter in the container console, because all containers created in the container platform always restart when they exist.

`-v`: Specifies container volume. The above command specifies three volumes. Correspondingly, we need to add three **data volumes** in the container console, and then mount the three volumes into the container through**Advanced Settings**.

First, create three volumes:
![](https://mc.qcloudimg.com/static/img/c5b11b2c717c263aa68a2aab12234fad/volume.png)

Then, mount the three volumes into the container through**Advanced Settings**:
![](https://mc.qcloudimg.com/static/img/d4130bd91b37fd76b6de759c2f8a1075/mount.png)

Note: We select `Use Local Disk` as the data volume type, so the data generated during the running process of the container will be saved to all nodes of the container, and switching container to another node will result in data loss. We can select `Cloud Disk` as data volume type for the container data to be saved to cloud disk. In this way, container volume data will not be lost, even if the container is switched to another node.

`--name`: Name of the running container. In the container console, the parameter specifies service name. The container and the service can use the same name.

### 2. Other Parameters
Here describes other common parameters used for executing docker run:

`-i`: Interactive container execution. This parameter is not supported, for containers can only run in the backend of our container console.

`-t`: Not supported, same as "-i".


`-e`: Environment variable of the running container. For example, a user executes the following docker run command:
```
docker run -e FOO='foo' -e BAR='bar' --name=container_name container_image
```

Container environment variables can be added via "Advanced Settings" of the container when a service is created in the container console. Here, the user is going to add two environment variables for the container: Foo with a value of foo and Bar with a value of bar.

### 3. Command and Args
Sometimes we want to specify a command and parameter for docker run, for example:
```
docker run --name=kubedns gcr.io/google_containers/kubedns-amd64:1.7 /kube-dns --domain=cluster.local. --dns-port=10053 -v 2

```
Here, the following command is specified:  /kube-dns, and three specified parameters are `-domain=cluster.local.`, `--dns-port=10053`, and -`v 2`.
In the console, we can specify as follows:

![](https://mc.qcloudimg.com/static/img/cf991cd098b96c19b70b1da4e11507c5/image.png)
