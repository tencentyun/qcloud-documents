## 如何使用DockerHub镜像加速器

docker软件源地址：`https://mirror.ccs.tencentyun.com`

### CCS集群CVM主机

无需手动配置，在创立节点时会自动安装docker服务，配置Mirror镜像,配置项如下：

```shell
[root@VM_1_2_centos ~]# cat /etc/docker/dockerd 
IPTABLES="--iptables=false"
STORAGE_DRIVER="--storage-driver=overlay2"
IP_MASQ="--ip-masq=false"
LOG_LEVEL="--log-level=warn"
REGISTRY_MIRROR="--registry-mirror=https://mirror.ccs.tencentyun.com"
```

### CVM主机配置

#### Linux：

a.适用于 Ubuntu14.04、Debian、CentOS6 、Fedora、OpenSUSE ，其他版本可能有细微不同

修改Docker配置文件/etc/default/docker, 如下：

```shell
DOCKER_OPTS="--registry-mirror=https://mirror.ccs.tencentyun.com"
```

b.适用于Centos7

修改Docker配置文件vi /etc/sysconfig/docker, 添加下面
```shell
OPTIONS='--registry-mirror=https://mirror.ccs.tencentyun.com'
```

注：Docker 1.3.2版本以上才支持Docker Hub Mirror机制，如果您还没有安装Docker或者版本过低，请安装或升级版本

#### Windows：

如果你是用的Boot2Docker，配置命令为：进入Boot2Docker Start Shell，并执行

```shell
sudo su echo "EXTRA_ARGS=\"–registry-mirror=http://https://mirror.ccs.tencentyun.com"">> /var/lib/boot2docker/profile  exit #  重启Boot2Docker
```

## 启动docker
执行以下命令
```shell
sudo service docker start
```