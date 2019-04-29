## 简介
本文为您详细介绍如何使用 CFS 文件系统。

## 操作步骤
使用 CFS 文件系统操作流程：“[创建和配置 CVM 实例](#.E5.88.9B.E5.BB.BA.E5.92.8C.E9.85.8D.E7.BD.AE-cvm-.E5.AE.9E.E4.BE.8B)” > “[创建文件系统及挂载点](#.E5.88.9B.E5.BB.BA.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F.E5.8F.8A.E6.8C.82.E8.BD.BD.E7.82.B9)” > “[连接实例](#.E8.BF.9E.E6.8E.A5.E5.AE.9E.E4.BE.8B)” > “[挂载文件系统](#.E6.8C.82.E8.BD.BD.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F)” > “[终止资源](#.E7.BB.88.E6.AD.A2.E8.B5.84.E6.BA.90)”。详细操作步骤请阅读本文以下章节。


### 创建和配置 CVM 实例
要访问文件系统，您需要将文件系统挂载在基于 Linux 或者 Windows 的腾讯云云服务器实例上。在此步骤中，您将创建和配置一个基于 Linux 的腾讯云 CVM 实例。如果您想要使用基于 Windows 的云服务器，请参考文档 [使用 CFS 创建网络文件系统（Windows）](/doc/product/582/11524)。如果已经创建 CVM 实例，请跳转至 [创建文件系统及挂载点](#1)。

登录腾讯云官网，选择【云产品】>【计算与网络】>【云服务器】，单击【立即选购】，进入 [云服务器购买页面](https://buy.cloud.tencent.com/buy/cvm)。
#### 1. 选择地域与机型
![](//mc.qcloudimg.com/static/img/3ed8bab8cce3dde578a6e3fb14267ea5/image.png)
- 选择计费模式。包年包月或按量付费（无法购买按量付费云服务器的用户请先进行  [实名认证](https://console.cloud.tencent.com/developer/auth)）。更多信息请看 [计费模式说明](/doc/product/213/2180) 。
- 选择地域和可用区。当您需要多台云服务器时，选择不同可用区可实现容灾效果。
- 选择机型和配置。实例类型详细说明，请参见 [实例类型概述](/doc/product/213/7153) 。


#### 2. 选择镜像
![](//mc.qcloudimg.com/static/img/fd40922e47525453a58de73d0ffa266c/image.png)
- 选择镜像提供方。腾讯云提供公共镜像、自定义镜像、共享镜像、服务市场，您可参考 [镜像类型](/doc/product/213/4941) 进行选择。对于刚开始使用腾讯云的用户，推荐选择公共镜像。
- 选择操作系统。腾讯云提供了 CentOS、 CoreOS、 Debian、 FreeBSD、 OpenSUSE、 SUSE、 Ubuntu 等操作系统，后续运行环境请您自行搭建。
- 选择系统版本。 

#### 3. 选择存储与网络
![](//mc.qcloudimg.com/static/img/e95a5bf7bf47c60f43dd0ee62946b67a/image.png)
- 选择硬盘类型和数据盘大小。
腾讯云提供云硬盘和本地硬盘两种类型（均默认 50GB 系统盘，系统盘大小任选）。
  - 云硬盘：采用一盘三备的分布式存储方式，数据可靠性高。
  - 本地硬盘：处在云服务器所在的物理机上的存储设备，可以获得较低的时延，但存在单点丢失风险。具体对比可以参考 [产品分类](/doc/product/362/2353) 。
- 选择网络类型。
腾讯云提供基础网络或私有网络两种可选。
 - 基础网络：适合新手用户，同一用户的云服务器内网互通。
 - 私有网络：适合更高阶的用户，不同私有网络间逻辑隔离。
- 选择公网带宽。
腾讯云提供按带宽计费或按使用流量计费两种可选。
 - 按带宽计费：选择固定带宽，超过本带宽时将丢包。适合网络波动较小的场景。
 - 按使用流量计费：按实际使用流量收费。可限制峰值带宽避免意外流量带来的费用，当瞬时带宽超过该值时将丢包。适合网络波动较大的场景。
- 选择服务器数量。
- 选择购买时长与续费方式（仅限包年包月云服务器）。

#### 4. 设置信息
![](//mc.qcloudimg.com/static/img/1c463db6e3b31abd6c1d3163f1c3108f/image.png)
- 命名主机：您可选择创建后命名，也可立即命名。
- 登录信息设置：
 - 设置密码：输入主机密码设置。
 - 立即关联密钥：关联 SSH 密钥。如您没有密钥或现有的密钥不合适，可以单击【现在创建】按钮创建，参考 [创建密钥](/doc/product/213/516#1) 指南。更多 SSH 密钥请见 [SSH密钥](/doc/product/213/503) 。
 - 自动生成密码：自动生成的密码将会以站内信方式发送。
- 选择安全组（**确保登录端口 22 开放**，更多信息见 [安全组](/doc/product/213/5221)） 。

单击【立即购买】按钮，完成支付后即可进入 [控制台](https://console.cloud.tencent.com/cvm/) 查收您的云服务器。
云服务器创建好后将会收到站内信，内容包括实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息。您可以使用这些信息登录和管理实例。
 

<span id="1"></span>
### 创建文件系统及挂载点

1. 登录 [CFS 控制台](https://console.cloud.tencent.com/cfs)。
2. 在腾讯云 CFS 控制台，单击【新建】，弹出创建文件系统弹窗。在创建文件系统弹窗中填写相关信息，确认无误后，单击【确定】即可创建文件系统。
![](https://main.qcloudimg.com/raw/3797c04469bf0da994d2e2876a2a39ad.png)
 - 名称：您可以为创建的文件系统进行命名。
 - 地域和可用区：靠近您客户的地域可降低访问延迟，提高下载速度。
 - 文件协议：NFS（更适用于Linux、Unix客户端),CIFS/SMB（更适用于 Windows 客户端）。
 - 网络类型：腾讯云提供基础网络或私有网络两种可选。基础网络适合新手用户，同一用户的云服务器内网互通。私有网络适合更高阶的用户，不同私有网络间逻辑隔离。
  	
 >!请根据您的 CVM 实例所在网络来创建并挂载文件系统。
 > - 若您要实现私有网络（VPC）下 CVM 对文件系统的共享，您需要在创建文件系统时选择私有网络。当文件系统属于私有网络时，如果未进行特殊网络设置，则只有同一私有网络内的 CVM 实例能够挂载。
 > - 若您要实现基础网络下 CVM 对文件系统的共享，您需要在创建文件系统时选择基础网络。当文件系统属于基础网络时，如果未进行特殊网络设置，则只有同在基础网路内的 CVM 实例能够挂载。
 > - 如果有多网络共享文件系统需求，请查看 [跨可用区、跨网络访问指引](/doc/product/582/9764)。

3. 获取挂载点信息。当文件系统及挂载点创建完毕后，单击实例 ID 进入到文件系统详情，单击【挂载点信息】，获取 Linux 下的挂载命令。
NFS 文件系统挂载点信息如下:
![](https://mc.qcloudimg.com/static/img/f50435216defb4083874bc78d568001e/image.png)
CIFS/SMB 文件系统挂载点信息如下: 
![](https://main.qcloudimg.com/raw/939aafe4bca9907bc391d41e8798c4a6.png)



### 连接实例
本部分操作介绍登录 Linux 云服务器的常用方法，不同情况下可以使用不同的登录方式，此处介绍控制台登录，更多登录方式请见 [登录 Linux 实例](/doc/product/213/5436) 。

**前提条件**
登录到云服务器时，需要使用管理员帐号和对应的密码。
 - 管理员账号：对于 Linux 类型的实例，管理员帐号统一为 root（Ubuntu 系统用户为 ubuntu）。
 - 密码：密码为购买云服务器时设置的密码。

**控制台登录云服务器**
- 在云服务器列表的操作列，单击【登录】按钮即可通过 VNC 连接至 Linux 云服务器。
![](//mc.qcloudimg.com/static/img/73cc4f9f702f80d95717c7a35063ab41/image.png)
- 输入帐号（root ，Ubuntu 系统用户为 ubuntu）和密码即可登录。

>!该终端为独享，即同一时间只有一个用户可以使用控制台登录。


**验证网络通信**
挂载前，需要确认客户端与文件系统的网络可达性。可以通过 telnet 命令验证，具体各个协议及客户端要求开放端口信息如下：

文件系统协议 | 客户端开放端口 | 确认网络联通性
------- | ------- | ---------
NFS 3.0 | 111，892， 2049 |  telnet 111 或者 892 或者 2049
NFS 4.0 | 2049 |  telnet 2049
CIFS/SMB | 445 |  telnet 445 

>!CFS 暂不支持 ping。

### 挂载文件系统
#### 挂载 NFS 文件系统
#### 1. 启动 NFS 客户端
挂载前，请确保系统中已经安装了`nfs-utils`或`nfs-common`，安装方法如下：
- CentOS：
```shell
sudo yum install nfs-utils
```
- Ubuntu 或 Debian：
```shell
sudo apt-get install nfs-common
```

#### 2. 创建待挂载目标目录
使用下列命令创建待挂载目标目录。
```shell
mkdir <待挂载目标目录>
```
示例：
```shell
mkdir /local/
mkdir /local/test
```

#### 3. 挂载
**NFS v4.0 挂载**
使用下列命令实现 NFS v4.0 挂载。
```shell
sudo mount -t nfs -o vers=4,noresvport <挂载点IP>:/ <待挂载目录>
```

- 挂载点IP：指创建文件系统时，自动的生成的挂载点 IP。
- 目前默认挂载的是文件系统的根目录 "/"。 在文件系统中创建子目录后，可以挂载该子目录。
- 待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。

>! `<挂载点IP>:/`与`<待挂载目标目录>`之间有一个空格。


示例：
- 挂载 CFS 根目录：
```shell
sudo mount -t nfs -o vers=4,noresvport 10.0.24.4:/ /localfolder
```
- 挂载 CFS 子目录 subfolder：
```shell
sudo mount -t nfs -o vers=4,noresvport 10.0.24.4:/subfolder /localfolder 
```
![](https://mc.qcloudimg.com/static/img/03550214c0499438e86cfd64b3c377b8/image.png)

**NFS v3.0 挂载**
使用下列命令实现 NFS v3.0 挂载。
```shell
sudo mount -t nfs -o vers=3,nolock,proto=tcp,noresvport <挂载点IP>:/<fsid> <待挂载目录>
```
- 挂载点IP：指创建文件系统时，自动的生成的挂载点 IP。
- NFS v3.0 仅支持子目录挂载，缺省文件系统子目录为 FSID。
- 待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。
示例

>! `<挂载点IP>:/<FSID>` 与 `<待挂载目标目录>`之间有一个空格。


示例：
- 挂载 CFS 子目录 subfolder：
```shell
sudo mount -t nfs -o vers=3,nolock,proto=tcp,noresvport 10.0.24.4:/z3r6k95r /localfolder 
```
![](https://mc.qcloudimg.com/static/img/03550214c0499438e86cfd64b3c377b8/image.png)

#### 4. 查看挂载点信息
挂载完成后，请使用如下命令查看已挂载的文件系统：
```shell
mount -l
```
也可以使用如下命令查看该文件系统的容量信息：
```shell
df -h
```
#### 挂载 CIFS/SMB 文件系统
#### 1. 启动 CIFS 客户端
挂载前，请确保系统中已经安装了`cifs-utils`，安装方法如下：
CentOS：
```shell
sudo yum install cifs-utils.x86_64 –y
```


#### 2. 创建待挂载目标目录
使用下列命令创建待挂载目标目录。
```shell
mkdir <待挂载目标目录>
```
示例：
```shell
mkdir /local/
mkdir /local/test
```

#### 3. 挂载
使用下列命令实现 CIFS 挂载。
```shell
mount -t cifs -o guest //<挂载点IP>/<FSID> /<待挂载目标目录>
```
- 挂载点IP：指创建文件系统时，自动的生成的挂载点 IP。
- 目前默认挂载使用文件系统的FSID。 
- 待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。

>!`<FSID>` 与 `/<待挂载目标目录>`之间有一个空格。

示例：

```shell
mount -t cifs -o guest //10.66.168.75/vj3i1135  /local/test
```

 ![](https://main.qcloudimg.com/raw/939aafe4bca9907bc391d41e8798c4a6.png)

#### 4. 查看挂载点信息
挂载完成后，请使用如下命令查看已挂载的文件系统：
```shell
mount -l
```
也可以使用如下命令查看该文件系统的容量信息：
```shell
df -h
```

#### 5. 卸载共享目录
当某些情况下需要卸载共享目录，请使用如下命令。其中 "目录名称" 为根目录或者文件系统的完整路径。
```shell
umount <目录名称>
```

示例： 
```shell
umount /local/test
```


### 终止资源
您可以从腾讯云控制台轻松终止 CVM 实例和文件系统。事实上，最好终止不再使用的资源，以免继续为其付费。
1. 终止腾讯云实例。进入云服务器 [控制台](https://console.cloud.tencent.com/cvm/index)，选中需要终止的实例，单击【更多】>【云主机状态】，可以选中【销毁】以终止 CVM 实例。
![](//mc.qcloudimg.com/static/img/76c588284e3b525702d748b5cd7b8b00/image.png)
2. 终止文件系统。进入腾讯云文件存储 [控制台](https://console.cloud.tencent.com/cfs)，选中需要终止的文件系统，单击【删除】并【确认】，即可删除文件系统。
![](//mc.qcloudimg.com/static/img/28cade4807a283ffdcb1fc2a39a7ad88/image.png)


