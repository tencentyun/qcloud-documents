腾讯云为您提供 DockerHub 加速器以方便您快速稳定拉取 DockerHub 平台上的容器镜像，该加速器地址为：

```
https://mirror.ccs.tencentyun.com
```
请参照以下教程在CVM实例中配置该加速器地址，重新启动 Dokcker 服务并确认该配置已生效。
## TKE 集群内 CVM 实例配置
TKE集群内CVM实例无需手动配置，集群在创建节点时会自动安装 Docker 服务，并配置 Mirror 镜像。默认配置项如下：
```shell
[root@VM_1_2_centos ~]# cat /etc/docker/dockerd 
IPTABLES="--iptables=false"
STORAGE_DRIVER="--storage-driver=overlay2"
IP_MASQ="--ip-masq=false"
LOG_LEVEL="--log-level=warn"
REGISTRY_MIRROR="--registry-mirror=https://mirror.ccs.tencentyun.com"
```
## CVM 实例通用配置
### Ubuntu 16.04+、Debian 8+、CentOS 7
创建或修改 /etc/docker/daemon.json，并写入以下内容：
```shell
{
  "registry-mirrors": [
    "https://mirror.ccs.tencentyun.com"
  ]
}
```
重新启动 Docker 服务
```shell
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```

### Windows 10
打开Docker客户端软件 Setting 选项，进入配置窗口后选择 Docker Engine 并写入以下内容，之后点击 Apply & Restart，Docker 服务会保存该配置并自动重启。
```shell
{
  "registry-mirrors": [
    "https://mirror.ccs.tencentyun.com"
  ]
}
```

## 检查加速器是否生效
执行 $ docker info，如果从结果中可看到以下内容，则说明配置成功。
```shell
Registry Mirrors:
 https://mirror.ccs.tencentyun.com
```