## docker run 参数适配

  本文将介绍如何把在本地的docker中已经调试完毕的容器，在迁移到腾讯云容器服务平台中运行时，对于docker run中的参数如何跟腾讯云容器控制台的参数进行对应。这里我们以创建一个简单的gitlab服务为例。

### 一、gitlab容器的参数示例
我们使用以下的docker run命令可以创建出一个简单的gitlab容器：

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



`-d`:容器在后台运行。容器平台都是以后台的形式来运行容器，所以本参数不需要在容器控制台指定。

`-p`:指定端口映射。我们这里映射了两个端口，容器端口分别是80和22，对外暴露的端口分别是20180和20122，对应到控制台，我们添加两条端口映射规则，并填写对应的容器端口和服务端口。由于我们的gitlab需要提供外网访问，我们选择了**提供公网访问**访问方式。
![](https://mc.qcloudimg.com/static/img/cf73ee3d941a768491d52af56a386db4/image.png)

`--restart`:本参数用于指定在容器退出时，是否重启容器。容器平台创建的所有容器退出时，都会重启容器，所以本参数不需要在容器控制台指定。

`-v`:本参数用于指定容器卷。上面的命令指定了三个卷，对应到容器控制台，我们也需要添加三个**数据卷**，并在容器的**高级设置**里将这三个卷挂载到容器里。

首先我们创建三个卷：
![](https://mc.qcloudimg.com/static/img/c5b11b2c717c263aa68a2aab12234fad/volume.png)

接着我们在容器的高级设置里面，将三个卷分别挂载到容器里：
![](https://mc.qcloudimg.com/static/img/d4130bd91b37fd76b6de759c2f8a1075/mount.png)

这里要注意的是，我们的数据卷的类型选择的是`使用本地硬盘`，所以容器运行过程中，在容器中生产的数据会被保存到容器所在的节点上，如果容器被调度到其他的节点上，那么数据就丢失了。我们可以使用`云硬盘`类型数据卷，容器的数据会保存到云硬盘中，即使容器被调度到其他的节点，容器卷的数据也不会丢。

`--name`:容器运行的名字。这个参数，对应到容器控制台就是服务名，当然容器名也可以跟服务名用相同的名字。

### 二、其它参数
这里介绍我们执行docker run时，其它常见的参数：

`-i`:交互式执行容器。我们容器控制台只支持后台运行容器，所以本参数不支持。

`-t`:跟-i参数一样，本参数也不支持。


`-e`:容器运行的环境变量。比如用户执行以下的docker run命令：
```
docker run -e FOO='foo' -e BAR='bar' --name=container_name container_image
```

这里用户希望为容器添加两个环境变量，在我们的容器控制台创建服务时，在容器的高级设置里，可以添加容器的环境变量，在这里，变量名和变量值分别为 变量名:Foo,变量值:foo，以及变量名:BAR,变量值:bar。

### 三、Command和Args
有时候我们希望在docker run的时候，指定进程的命令和参数，比如：
```
docker run --name=kubedns gcr.io/google_containers/kubedns-amd64:1.7 /kube-dns --domain=cluster.local. --dns-port=10053 -v 2

```
这里我们指定了容器进程的命令为： /kube-dns，并指定了三个参数：`-domain=cluster.local.` `--dns-port=10053` 和-`v 2`。
在我们的控制台，我们可以这样指定：

![](https://mc.qcloudimg.com/static/img/cf991cd098b96c19b70b1da4e11507c5/image.png)