Docker 软件源地址：`https://mirror.ccs.tencentyun.com`。

## TKE 集群 CVM 主机
无需手动配置，在创建节点时会自动安装 Docker 服务，配置 Mirror 镜像。配置项如下：
```shell
[root@VM_1_2_centos ~]# cat /etc/docker/dockerd 
IPTABLES="--iptables=false"
STORAGE_DRIVER="--storage-driver=overlay2"
IP_MASQ="--ip-masq=false"
LOG_LEVEL="--log-level=warn"
REGISTRY_MIRROR="--registry-mirror=https://mirror.ccs.tencentyun.com"
```

## CVM 主机配置
### Linux：
- 适用于 Ubuntu14.04、Debian、CentOS6 、Fedora 和 OpenSUSE 版本，其他版本可能有细微不同。
修改 Docker 配置文件 `/etc/default/docker`，如下：
```shell
DOCKER_OPTS="--registry-mirror=https://mirror.ccs.tencentyun.com"
```
- 适用于 Centos7 版本。
修改 Docker 配置文件 `vi /etc/sysconfig/docker`，如下：
```shell
OPTIONS='--registry-mirror=https://mirror.ccs.tencentyun.com'
```
>**注意：**
>Docker 1.3.2 版本以上才支持 Docker Hub Mirror 机制，如果您还没有安装 Docker 或者版本过低，请安装或升级版本。

### Windows：
如果你使用的是 Boot2Docker，进入 Boot2Docker Start Shell 并执行：
```shell
sudo su echo "EXTRA_ARGS=\"–registry-mirror=https://mirror.ccs.tencentyun.com"">> /var/lib/boot2docker/profile  exit #  重启Boot2Docker
```

## 启动 Docker
执行如下命令
```shell
sudo service docker start
```
