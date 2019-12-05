腾讯云私有网络 VPC 可以通过加密的 VPN 通道连接客户 IDC，只需在 VPC 及用户 IDC 中设置 VPN 网关及对端网关即可。客户如果暂时不打算使用 Cisco、Juniper 或 H3C 等厂家的硬件 VPN 设备，也可以使用开源软件在服务器上搭建对端网关。本文以在 CentOS 上安装 ipsec-tools 为例，介绍如何通过开源软件连接腾讯云 VPC，建立混合云场景。

## 1. 环境说明
![](//mccdn.qcloud.com/img56c6836ccfc95.png)

如上图所示，左边是您在腾讯云上建立的私有网络。为了将 VPC 与右边的客户 IDC 互通，可以利用公网在两者之间建立加密 Ipsec VPN 通道，保障传输数据的安全可靠。

首先您需要在腾讯云上建立您的私有网络，并根据您的需求规划子网、购买 VPN 网关，并设置好到需要互通的 IDC 网络的 VPC 路由（注意路由设置中【下一跳】请选择您购买的 VPN 网关）。具体操作步骤请见 <a href="http://cloud.tencent.com/doc/product/215/%E5%88%9B%E5%BB%BA%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%8F%8A%E5%AD%90%E7%BD%91" target="_blank">创建私有网络及子网</a>[创建私有网络及子网](http://cloud.tencent.com/doc/product/215/%E5%88%9B%E5%BB%BA%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%8F%8A%E5%AD%90%E7%BD%91)、<a href="" target="_blank"></a>[向私有网络中添加云服务](http://cloud.tencent.com/doc/product/215/%E5%90%91%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E4%B8%AD%E6%B7%BB%E5%8A%A0%E4%BA%91%E6%9C%8D%E5%8A%A1)、<a href="" target="_blank"></a>[关联子网路由](http://cloud.tencent.com/doc/product/215/%E5%85%B3%E8%81%94%E5%AD%90%E7%BD%91%E8%B7%AF%E7%94%B1)、<a href="" target="_blank"></a>[修改默认路由表](http://cloud.tencent.com/doc/product/215/%E4%BF%AE%E6%94%B9%E9%BB%98%E8%AE%A4%E8%B7%AF%E7%94%B1%E8%A1%A8) 和 <a href="" target="_blank"></a>[创建VPN网关](http://cloud.tencent.com/doc/product/215/%E5%88%9B%E5%BB%BAVPN%E7%BD%91%E5%85%B3)，将上图左边部分创建设置完成。


若您暂时不打算使用任何硬件厂家 VPN 设备，您也可按照本文档下面部分的操作方式，在位于 IDC 机房的一端使用 Ipsec-tools 开源工具搭建 VPN 网关。

## 2. 安装 Ipsec-tools
系统环境要求，以 CentOS 6.4 为例：
```
Linux version 2.6.32-431.23.3.el6.x86_64
(mockbuild@c6b8.bsys.dev.centos.org) (gcc version 4.4.7 20120313 
(Red Hat 4.4.7-4) (GCC) ) #1 SMP Thu Jul 31 17:20:51 UTC 2014
```
根据系统平台不同选择使用 `ipsec-tools-0.8.0-25.3.x86_64.rpm` 包或者 `ipsec-tools-0.8.0-25.3.i686.rpm` 包，可以由下面的链接进入下载：
<a href="" target="_blank">链接 1</a>
ftp://ftp.pbone.net/mirror/ftp5.gwdg.de/pub/opensuse/repositories/home:/aevseev/CentOS_CentOS-6/x86_64/ipsec-tools-0.8.0-25.3.x86_64.rpm
<a href="" target="_blank">链接 2</a>
ftp://ftp.pbone.net/mirror/ftp5.gwdg.de/pub/opensuse/repositories/home:/aevseev/CentOS_CentOS-6/i686/ipsec-tools-0.8.0-25.3.i686.rpm

下载完成后，使用以下命令进行安装：

```
rpm -ivh ipsec-tools-0.8.0-25.3.x86_64.rpm
```
或
```
rpm -ivh ipsec-tools-0.8.0-25.3.i686.rpm
```

安装结束后，使用以下命令检查安装结果：

```
racoon –V
```
![](//mccdn.qcloud.com/img56c68a299aed9.png)

## 3. 配置 Ipsec-tools
需要配置的文件包括：

IPSec 策略配置文件：`/etc/racoon/setkey.conf`
密钥配置文件：`/etc/racoon/psk.txt`
IKE配置文件：`/etc/racoon/racoon.conf`

### 3.1. 配置 Ipsec 策略
使用以下命令打开配置文件：

```
vi /etc/racoon/setkey.conf
```

设置如下信息：

假设您 VPC 的 CIDR 为`10.100.2.0/24`，VPC 上 VPN 网关的 IP 地址为 `112.\*.\*.251`。您IDC的CIDR为 `172.16.2.0/24`，本地 VPN 设备的 IP 地址为 `112.\*.\*.152`，则配置如下：
![](//mccdn.qcloud.com/img56c68be5ba93c.png)

### 3.2. 配置密钥
使用以下命令打开配置文件：

```
vi /etc/racoon/psk.txt
```
仍然假设您 VPC 上 VPN 网关的 IP 地址为 `112.\*.\*.251`，预共享密钥为 tes t，则 psk.txt 配置内容如下：
![](//mccdn.qcloud.com/img56c68ca34b349.png)

并执行以下命令：

```
chmod 600 psk.txt   
chown root psk.txt
```

### 3.3. 配置 IKE
使用以下命令打开配置文件：

```
vi /etc/racoon/racoon.conf
```

仍然假设您 VPC 上 VPN 网关的 IP 地址为 `112.\*.\*.251`，您本地 VPN 设备的 IP 地址为 `112.\*.\*.152`，则 racoon.conf 配置内容如下：
<div style="text-align:center'>
![](//mccdn.qcloud.com/img56c68dc067617.png)

</div>
## 4. 启动 Ipsec-tools

执行以下命令启动 Ipsec-tools：

```
echo 1 > /proc/sys/net/ipv4/ip_forward
/usr/sbin/setkey -f /etc/racoon/setkey.conf
/usr/sbin/racoon -f /etc/racoon/racoon.conf
```

为保障设备重启后 ipsec 服务自动开启，同时需要将这三条命令写入 `/etc/rc.local` 文件中。

## 5. 检查通道状态
通过以下命令查看是否完成通道 sa的协商：


```
setkey -D
```
![](//mccdn.qcloud.com/img56c68edfa569d.png)


在您的 IDC 网络中需要将目的 IP 为 VPC 的 CIDR 的报文路由到您的对端 VPN 网关，即前面介绍的配置 Ipsec-tools 的机器。

在 IDC 中的机器上 ping 您在 VPC 里的子机 IP，检测通信是否顺利建立。

## 6. 其他问题
若经过设置后 VPC 与 IDC 无法进行加密通信，请按照以下步骤检查：

1) 检测 VPC 网关 IP 是否可达
 `ping` 您在腾讯云上购买的 VPN 网关公网 IP 地址是否可达。

2) 是否缺少路由
通过以下命令检查是否有到 VPC 网段的路由或默认路由。

```
route –n
```

3) 是否存在防火墙过滤规则
通过以下命令检查是否有防火墙将 IKE 或内网通信报文过滤掉。

```
iptables   -nvL
```

4) 检查防火墙 NAT 规则
是否有将内网通信报文进行 NAT 导致命中不了 Ipsec 策略。

```
iptables    -t    nat   -nvL
```
