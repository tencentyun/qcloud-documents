腾讯云为您提供如下 DockerHub 加速器，以方便您快速拉取 DockerHub 平台上的容器镜像。
此加速器地址需在腾讯云云服务器中配置才可生效，请勿通过浏览器直接访问，请参照以下教程进行配置。
```
https://mirror.ccs.tencentyun.com
```


## TKE 集群内 CVM 实例配置
TKE 集群内 CVM 实例无需手动配置，集群在创建节点时会自动安装 Docker 服务，并配置 Mirror 镜像。默认配置项如下：
```shell
[root@VM_1_2_centos ~]# cat /etc/docker/dockerd 
IPTABLES="--iptables=false"
STORAGE_DRIVER="--storage-driver=overlay2"
IP_MASQ="--ip-masq=false"
LOG_LEVEL="--log-level=warn"
REGISTRY_MIRROR="--registry-mirror=https://mirror.ccs.tencentyun.com"
```
## CVM 实例通用配置
### Linux 
>?本文以 Ubuntu 16.04+、Debian 8+、CentOS 7 的配置为例，其他版本请结合实际情况进行配置。
>
1. 创建或修改 `/etc/docker/daemon.json` 文件，并写入以下内容：
```shell
{
  	"registry-mirrors": [
	  	"https://mirror.ccs.tencentyun.com"
	 ]
}
```
2. 依次执行以下命令，重新启动 Docker 服务。
```shell
$ sudo systemctl daemon-reload
```
```
$ sudo systemctl restart docker
# Ubuntu16.04 请执行 sudo systemctl restart dockerd 命令
```

### Windows 10
1. 打开 Docker 客户端软件的 Setting 选项。
2. 打开配置窗口后选择 Docker Engine，并写入以下内容。
```shell
{
	 "registry-mirrors": [
	  	"https://mirror.ccs.tencentyun.com"
	 ]
}
```
2. 单击【Apply & Restart】，Docker 服务会保存该配置并自动重启。

## 检查加速器是否生效
执行 `docker info` 命令，返回结果中包含以下内容，则说明配置成功。
```shell
Registry Mirrors:
 https://mirror.ccs.tencentyun.com
```
