本文将介绍如何把在本地的 docker 中已经调试完毕的容器，在迁移到腾讯云容器服务平台中运行时，对于 docker run 中的参数如何跟腾讯云容器控制台的参数进行对应。这里我们以创建一个简单的 gitlab 服务为例。

### gitlab 容器的参数示例
您可以使用以下的 docker run 命令可以创建出一个简单的 gitlab 容器：
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



`-d`：容器在后台运行。容器平台都是以后台的形式来运行容器，所以本参数不需要在容器控制台指定。
`-p`：指定端口映射。这里映射了两个端口，容器端口分别是80和22，对外暴露的端口分别是20180和20122，对应到控制台，添加两条端口映射规则，并填写对应的容器端口和服务端口。由于 gitlab 需要提供外网访问，采用了**提供公网访问**访问方式。如下图所示：
![](https://mc.qcloudimg.com/static/img/cf73ee3d941a768491d52af56a386db4/image.png)

`--restart`：本参数用于指定在容器退出时，是否重启容器。容器平台创建的所有容器退出时，都会重启容器，所以本参数不需要在容器控制台指定。
`-v`：本参数用于指定容器卷。上面的命令指定了三个卷，对应到容器控制台，我们也需要添加三个**数据卷**，并在**实例内容器**里将这三个卷挂载到容器里。
首先我们创建三个卷。如下图所示：
![](https://main.qcloudimg.com/raw/8ab22b95db8157570bf587f528b47587.png)

在实例内容器里面，将三个卷分别挂载到容器里。如下图所示：
![](https://main.qcloudimg.com/raw/d827222268fb5411ca40e8eafc7cfc8d.png)

这里要注意的是，数据卷类型选择的是`使用主机路径`，所以容器运行过程中，在容器中生产的数据会被保存到容器所在的节点上，如果容器被调度到其他的节点上，那么数据就丢失了。您可以使用`云硬盘`类型数据卷，容器的数据会保存到云硬盘中，即使容器被调度到其他的节点，容器卷的数据也不会丢。
`--name`：容器运行的名字。这个参数，对应到容器控制台就是服务名，当然容器名也可以跟服务名用相同的名字。

### 其它参数
以下为执行 docker run 时，其它常见的参数：
`-i`：交互式执行容器。容器控制台只支持后台运行容器，所以本参数不支持。
`-t`：跟 -i 参数一样，本参数也不支持。
`-e`：容器运行的环境变量。例如用户执行以下的 docker run 命令：
```
docker run -e FOO='foo' -e BAR='bar' --name=container_name container_image
```
这里用户希望为容器添加两个环境变量，在容器控制台创建服务时，容器的高级设置里可添加容器的环境变量。变量名和变量值分别为 ：
- 变量名：Foo，变量值：foo。
- 变量名：BAR，变量值：bar。

### Command 和 Args
您可以在 docker run 的时候，指定进程的命令和参数。例如：
```
docker run --name=kubedns gcr.io/google_containers/kubedns-amd64:1.7 /kube-dns --domain=cluster.local. --dns-port=10053 -v 2
```
指定了容器进程的命令为： /kube-dns，并指定了三个参数：`-domain=cluster.local.` `--dns-port=10053` 和 `-v 2`。在控制台中参数设置如下图所示：
![](https://mc.qcloudimg.com/static/img/cf991cd098b96c19b70b1da4e11507c5/image.png)
