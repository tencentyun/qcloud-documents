## 操作场景
本文指导您如何在轻量应用服务器上安装 Docker，以及使用 Docker 镜像源加速镜像下载。

## 操作步骤

### 在轻量应用服务器中安装 Docker
请根据实例的操作系统类型，参考相应的文档进行安装。

| 操作系统 | 说明 |
|---------|---------|
| CentOS | 参考 [Docker 官方文档 - 在 CentOS 中安装 Docker](https://docs.docker.com/engine/install/centos/) 进行安装。 |
| Ubuntu | 参考 [Docker 官方文档 - 在 Ubuntu 中安装 Docker](https://docs.docker.com/engine/install/ubuntu/) 进行安装。 |
| Windows | 参考 [Docker 官方文档 - 在 Windows 中安装 Docker](https://docs.docker.com/docker-for-windows/install/) 进行安装。 |


### 使用腾讯云 Docker 镜像源加速镜像下载

安装 Docker 软件后，您可以直接通过 `docker pull` 命令拉取镜像。如您未配置镜像加速源，直接拉取 DockerHub 中的镜像，通常下载速度会比较慢。
为此，我们推荐您使用腾讯云 Docker 镜像源加速镜像下载。请根据实例的操作系统类型，选择相应的操作步骤进行配置。
- 适用于基于 Ubuntu 操作系统的实例：
 1. 执行以下命令，打开 `/etc/default/docker` 配置文件。
```
vim /etc/default/docker
```
 2. 按 **i** 切换至编辑模式，添加以下内容，并保存。
```
DOCKER_OPTS="--registry-mirror=https://mirror.ccs.tencentyun.com"
```
- 适用于基于 CentOS 操作系统的实例：
 1. 执行以下命令，打开 `/etc/docker/daemon.json` 配置文件。
```
vim /etc/docker/daemon.json
```
 2. 按 **i** 切换至编辑模式，添加以下内容，并保存。
```
{
   "registry-mirrors": [
       "https://mirror.ccs.tencentyun.com"
  ]
}
```
- 适用于已安装 Boot2Docker 的 Windows 操作系统实例：
 1. 进入 Boot2Docker Start Shell，并执行以下命令：
```
sudo su echo "EXTRA_ARGS=\"–registry-mirror=https://mirror.ccs.tencentyun.com\"" >> /var/lib/boot2docker/profile  exit 
```
 2. 重启 Boot2Docker。
