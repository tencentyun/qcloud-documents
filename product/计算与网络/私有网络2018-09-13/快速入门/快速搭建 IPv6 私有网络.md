本教程将帮助您搭建一个具有 IPv6 CIDR 的私有网络（VPC），并为 VPC 内的云服务器或者弹性网卡开启 IPv6，实现 IPv6 的内外网通信。

## 操作场景
1. 云服务器启用 IPv6，和 VPC 内云服务器 IPv6 双向通信。
2. 云服务器启用 IPv6，和 Internet 的 IPv6 用户进行双向通信。
![](https://main.qcloudimg.com/raw/21eb23c9b65349e06568806f36ddee2f.png)

## 前提条件
1. 在开始使用腾讯云产品前，您需要先完成 [账号注册与认证](https://cloud.tencent.com/doc/product/213/6090) 。
2. 目前支持 IPv6 的地域为上海、北京和广州，请在这些地域部署 IPv6 服务。
3. IPv6 地址为GUA地址，每个VPC分配1个`/56`的 IPv6 CIDR，每个子网分配1个`/64`的 IPv6 CIDR，每个弹性网卡分配1个 IPv6 地址。
4. 主网卡支持申请 IPv6 地址，辅助网卡也支持申请 IPv6 地址。想要了解更多云服务器和弹性网卡的关系，可参见 [弹性网卡](https://cloud.tencent.com/document/product/576) 产品文档。

## 操作步骤
### 步骤1：VPC 分配 IPv6 CIDR
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在需要开启 IPv6 的 VPC 所在行的操作栏下，单击【获取 IPv6 CIDR】，系统将为该 VPC 分配一个`/56`的 IPv6  CIDR 地址块。
![](https://main.qcloudimg.com/raw/3f23dcb2c354d90593181aebe1f2fd53.png)

### 步骤2：为子网分配 IPv6 CIDR
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在需要开启 IPv6 的子网所在行的操作栏下，单击【获取 IPv6 CIDR】并确认操作，系统将从 VPC 的`/56` IPv6 CIDR 分配一个`/64`的 IPv6 CIDR。
![](https://main.qcloudimg.com/raw/8f9eb15cc6ad71594551fe8f501d3c75.png)

### 步骤3：弹性网卡获取 IPv6 地址
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择【IP 与网卡】>【弹性网卡】，在列表页中单击需要获取 IPv6 地址的弹性网卡 ID，进入详情页。
3. 选择【IPv6 地址管理】标签页，单击【分配 IP】。
![](https://main.qcloudimg.com/raw/3988ff4d36229c8ce99a9276875204a9.png)
4. 在弹窗中单击【确定】即可。
![](https://main.qcloudimg.com/raw/737f2b30db0766ebf09ce99f2bdc4e01.png)
5. 系统将会为弹性网卡分配一个 IPv6 地址，如下图所示。
![](https://main.qcloudimg.com/raw/309e8e9d70b69ddb4c70a0ead71f7862.png)

### 步骤4：为弹性网卡的 IPv6 开启公网
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择【IP 与网卡】>【弹性公网 IPv6】，为 IPv6 开启公网并设置公网带宽。
3. 单击操作栏下的【调整带宽】。
![](https://main.qcloudimg.com/raw/9007bdd4fa3ca305e4654ada454d767f.png)
4. 在弹框中设置公网带宽。
>?如果带宽设置不为0，则开通公网；如果带宽设置为0，则关闭公网。
>
![](https://main.qcloudimg.com/raw/081b70cdbb104a3c0a9bbe51e74036ef.png)
5. 您也可勾选多个 IPv6 地址实例，单击【开通公网】或【关闭公网】并确定操作来批量开通或关闭 IPv6 公网。
![](https://main.qcloudimg.com/raw/244121ef0310777489b678a012b1ad60.png)

### 步骤5：登录云服务器，开启 IPv6
云服务器开启 IPv6 需要进行相关的手工设置，如下操作适用于**新购买的 CentOS7.5 /CentOS7.6**。如果云服务器镜像为存量 CentOS 7.5/CentOS 7.6，新购或者存量的其他 Linux 版本，新购或者存量的 Windows 系统，请参见下文中的 [其他镜像开启 IPv6](#other)。
1. 进入 [云服务器控制台](https://console.cloud.tencent.com/cvm) 并登录实例。
![](https://main.qcloudimg.com/raw/70a6364dfeabd537398f2bd98bc600e4.png)

2. 执行如下命令，打开`/etc/sysconfig/network-scripts/`文件夹下的`ifcfg-eth0`文件。
```
vim /etc/sysconfig/network-scripts/ifcfg-eth0
```
3. 按 i 切换至编辑模式，增加`DHCPV6C=yes`并保存。
![](https://main.qcloudimg.com/raw/94b60f6fb3177f5124339e5c017a8ac2.png)

4. 依次执行如下命令，查看是否已经获取到 IPv6 地址。
```
dhclient -6
ifconfig
```
![](https://main.qcloudimg.com/raw/25ccd3b27744ad0f056de14a39465724.png)

5. 执行如下命令，打开 `/etc/ssh/`文件夹下的`sshd_config`文件。
```
vim /etc/ssh/sshd_config
```
6. 按 i 切换至编辑模式，删除对`AddressFamily any`的注释（即删除前面的`#`）并保存，为 ssh 等应用程序开启 IPv6 监听。
![](https://main.qcloudimg.com/raw/52e9354e072a31f21071acde0262d58d.png)

### 步骤6：测试 IPv6 的连通性
可通过 ping 或 ssh 等操作来测试 IPv6 的连通性。
例如，从云服务器 ping `240c::6666` 或 `www.qq.com`，或从公网 IPv6 地址 ssh 云服务器。
![](https://main.qcloudimg.com/raw/6202b3ebe7e946884d0342d6ec2ca16d.png)
<span id="other"/>

### 其他镜像开启 IPv6
#### CentOS 7.3开启 IPv6
1. 执行如下命令，打开`etc`文件夹下的`sysctl.conf`。
```
vim /etc/sysctl.conf
```
2. 按 i 切换至编辑模式，将如下的 IPv6 相关参数设置为0并保存。
```
net.ipv6.conf.all.disableipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0
net.ipv6.conf.lo.disable_ipv6 = 0
```
![](https://main.qcloudimg.com/raw/dc1e37e0c3a89b170038ef28d6d0583d.png)
3. 执行如下命令，确认是否修改成功。
```
sysctl -a | grep ipv6 | grep disable
```
显示结果如下，则已成功修改。
![](https://main.qcloudimg.com/raw/b1294c92045d0dc5c688c6afc970a412.png)

4. 执行如下命令，打开`/etc/sysconfig/network-scripts/`文件夹下的`ifcfg-eth0`文件。
```
vim /etc/sysconfig/network-scripts/ifcfg-eth0
```
5. 按 i 切换至编辑模式，增加`DHCPV6C=yes`并保存。
![](https://main.qcloudimg.com/raw/7eb7d1dbf6e9773ca3282979587d4f55.png)

6. 执行如下命令，打开`/etc/sysconfig/network-scripts/`文件夹下的`route6-eth0`文件。
```
vim /etc/sysconfig/network-scripts/route6-eth0
```
7. 按 i 切换至编辑模式，增加`default dev eth0`并保存。
![](https://main.qcloudimg.com/raw/88a185a9dec922e4142c8ad8ffe4a354.png)
8. 执行如下命令，重新启动网卡。
```
service network restart
或者
systemctl restart network
```
9. 依次执行如下命令，查看是否已经获取到 IPv6 地址。
```
dhclient -6
ifconfig
```
![](https://main.qcloudimg.com/raw/2e42f1a5e7b9672d60461fe05edfed52.png)
10. 执行如下命令，打开 `/etc/ssh/`文件夹下的`sshd_config`文件。
```
vim /etc/ssh/sshd_config
```
11. 按 i 切换至编辑模式，删除对`AddressFamily any`的注释（即删除前面的`#`）并保存，为 ssh 等应用程序开启 IPv6 监听。
![](https://main.qcloudimg.com/raw/e0d64e3836b704bab4713697df865d81.png)

#### Debian 8.2 开启 IPv6
1. 执行如下命令，打开`etc`文件夹下的`sysctl.conf`。
```
vim /etc/sysctl.conf
```
2. 按 i 切换至编辑模式，将如下的 IPv6 相关参数设置为0并保存。
```
net.ipv6.conf.all.disable_ipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0
```
3. 执行如下命令，对参数进行加载。
```
sysctl -p
```
4. 依次执行如下命令，查看是否已经获取到 IPv6 地址。
```
dhclient -6
ifconfig
```
![](https://main.qcloudimg.com/raw/cd5a2072c73307c79b7997bbd24cec13.png)
5. 执行如下命令，配置默认路由，并通过 ping 测试公网连通性。
```
ip -6 route add default dev eth0
```
![](https://main.qcloudimg.com/raw/30f3bd7387c721b8e120d7d50bd8c92b.png)

#### Windows 开启 IPv6
1. 登录云服务器实例，进入操作系统的【控制面板】>【网络和 Internet】>【网络连接】，双击命名为“以太网”的网卡进行编辑。
![](https://main.qcloudimg.com/raw/ee56b6dd824c704e56c8ec5e0d4b013a.png)
2. 在“以太网属性”弹窗中，选中【Internet 协议版本6（TCP/IPv6）】并单击【属性】。
![](https://main.qcloudimg.com/raw/1f10d494b792d975a387ec6e38555021.png)
3. 在“Internet 协议版本6（TCP/IPv6）属性”弹窗中，手工编辑 IPv6 地址并设置 DNS，单击【确定】。
![](https://main.qcloudimg.com/raw/fac63249f22197686d68e3afffb3eb14.png)
4. 登录 powershell 依次执行如下命令配置默认路由以及查看 IPv6 地址，并通过 ping 测试公网连通性。
```
netsh interface ipv6 add route ::/0 "以太网"
ipconfig
```
![](https://main.qcloudimg.com/raw/eec1e647837d6b096ef9e022c3bafa7e.png)
