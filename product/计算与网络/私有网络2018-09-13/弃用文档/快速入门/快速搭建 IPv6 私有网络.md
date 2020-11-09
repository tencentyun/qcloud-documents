>? 弹性公网 IPv6 即将开启内测，敬请期待。

本教程将帮助您搭建一个具有 IPv6 CIDR 的私有网络（VPC），并为 VPC 内的云服务器或者弹性网卡开启 IPv6，实现 IPv6 的内外网通信。
## 操作场景
1. 云服务器启用 IPv6，和 VPC 内其他云服务器的 IPv6 内网互通。
2. 云服务器启用 IPv6，和 Internet 的 IPv6 用户进行双向通信。
![](https://main.qcloudimg.com/raw/245f8acb1bea7b002035193b089bf1b7.png)

## 操作须知
1. 在开始使用腾讯云产品前，您需要先完成 [账号注册与认证](https://cloud.tencent.com/doc/product/213/6090) 。
2. 目前支持 IPv6 的地域为北京、上海、广州、上海金融云、深圳金融云，请在这些地域部署 IPv6 服务。
3. IPv6 地址为 GUA 地址，每个 VPC 分配1个`/56`的 IPv6 CIDR，每个子网分配1个`/64`的 IPv6 CIDR，每个弹性网卡分配1个 IPv6 地址。
4. 主网卡、辅助网卡均支持申请 IPv6 地址。想要了解更多云服务器和弹性网卡的关系，请参见 [弹性网卡](https://cloud.tencent.com/document/product/576) 产品文档。

## 操作步骤
### 步骤1：VPC 分配 IPv6 CIDR
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在需要开启 IPv6 的 VPC 所在行的操作栏下，单击【编辑 CIDR】。
3. 在弹框中的 IPv6 CIDR 单击【获取】并确认操作，系统将为 VPC 分配一个`/56`的 IPv6 地址段，您可以在列表里看到 IPv6 地址段的详细信息。
![](https://main.qcloudimg.com/raw/06cc0c14dc28e511492d5f1b5cb01f32.png)

### 步骤2：为子网分配 IPv6 CIDR
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在需要开启 IPv6 的子网所在行的操作栏下，单击【获取 IPv6 CIDR】并确认操作，系统将从 VPC 的`/56` IPv6 CIDR 分配一个`/64`的 IPv6 CIDR。
![](https://main.qcloudimg.com/raw/d3d8fcaa9c336dac11485d5f7ed95a92.png)

### 步骤3：弹性网卡获取 IPv6 地址
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择【IP 与网卡】>【弹性网卡】，在列表页中单击需要获取 IPv6 地址的弹性网卡 ID，进入详情页。
3. 选择【IPv6 地址管理】标签页，单击【分配 IP】。
![](https://main.qcloudimg.com/raw/3988ff4d36229c8ce99a9276875204a9.png)
4. 在弹窗中单击【确定】即可。
![](https://main.qcloudimg.com/raw/737f2b30db0766ebf09ce99f2bdc4e01.png)
5. 系统将会为弹性网卡分配一个 IPv6 地址，如下图所示。
![](https://main.qcloudimg.com/raw/309e8e9d70b69ddb4c70a0ead71f7862.png)

### 步骤4：为弹性网卡的 IPv6 地址开启公网
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择【IP 与网卡】>【弹性公网 IPv6】，为 IPv6 开启公网并设置公网带宽。
3. 单击操作栏下的【调整带宽】。
![](https://main.qcloudimg.com/raw/dca3e6d40d5480793fffc2d8bcc042bf.png)
4. 在弹框中设置公网带宽并单击【调整】。
>?如果带宽设置不为0，则开通公网；如果带宽设置为0，则关闭公网。
>
![](https://main.qcloudimg.com/raw/9e2a767a7b38f4668bf7a83bb8e5d295.png)
5. 您也可勾选多个 IPv6 地址实例，单击【开通公网】或【关闭公网】并确定操作来批量开通或关闭 IPv6 公网。
![](https://main.qcloudimg.com/raw/ebb907c22c5672c38e728e66f35272b1.png)

### 步骤5：登录云服务器，开启 IPv6
不同云服务器开启 IPv6 的操作方法有差异，如下列举了五种典型的云服务器的操作方法，本步骤以新购 CentOS 7.5 /新购 CentOS 7.6（2019年06月31日后购买） 开启 IPv6 为例：
- [新购 CentOS 7.5/新购 CentOS 7.6 开启 IPv6](#新购CentOS7.5/CentOS7.6)
- <a href="https://cloud.tencent.com/document/product/215/38861#CentOS6.8" target="_blank">CentOS 6.8 开启 IPv6</a>
- <a href="https://cloud.tencent.com/document/product/215/38861#CentOS7.3" target="_blank">CentOS 7.3/存量 CentOS 7.5/存量 CentOS 7.6 开启 IPv6</a>
- <a href="https://cloud.tencent.com/document/product/215/38861#Debian8.2" target="_blank">Debian 8.2 开启 IPv6</a>
- <a href="https://cloud.tencent.com/document/product/215/38861#Windows2012" target="_blank">Windows 2012 开启 IPv6</a>

<span id="新购CentOS7.5/CentOS7.6"/>

#### 新购 CentOS7.5 /新购 CentOS7.6 开启 IPv6
1. 进入 [云服务器控制台](https://console.cloud.tencent.com/cvm) 并登录实例。
![](https://main.qcloudimg.com/raw/70a6364dfeabd537398f2bd98bc600e4.png)

2. 执行如下命令，打开`/etc/sysconfig/network-scripts/`文件夹下的`ifcfg-eth0`文件。
```
vim /etc/sysconfig/network-scripts/ifcfg-eth0
```
3. 按 “i” 切换至编辑模式，增加如下内容。
```
DHCPV6C=yes
```
![](https://main.qcloudimg.com/raw/94b60f6fb3177f5124339e5c017a8ac2.png)
4. 按 “Esc”，输入 “:wq”，保存文件并返回。
5. 依次执行如下命令，查看是否已经获取到 IPv6 地址。
```
dhclient -6
ifconfig
```
![](https://main.qcloudimg.com/raw/25ccd3b27744ad0f056de14a39465724.png)

6. 执行如下命令，打开 `/etc/ssh/`文件夹下的`sshd_config`文件。
```
vim /etc/ssh/sshd_config
```
7. 按 “i” 切换至编辑模式，删除对`AddressFamily any`的注释（即删除前面的`#`），为 ssh 等应用程序开启 IPv6 监听。
![](https://main.qcloudimg.com/raw/52e9354e072a31f21071acde0262d58d.png)
8. 按 “Esc”，输入 “:wq”，保存文件并返回。
9. 执行如下命令，重启 ssh 进程。
```
service sshd restart
```
10. 执行如下命令，查看 ssh 是否已经监听 IPv6。
```
netstat -tupln
```
![](https://main.qcloudimg.com/raw/4b3937053527ea3edd3efedfa0113ca9.png)

### 步骤6：测试 IPv6 的连通性
可通过 ping 和 ssh 等操作来测试 IPv6 的连通性。
- 步骤1：从云服务器 `ping6 240c::6666` 或 `ping6 www.qq.com`，如下图所示：
![](https://main.qcloudimg.com/raw/6202b3ebe7e946884d0342d6ec2ca16d.png)
- 步骤2：从公网 IPv6 地址 ssh 云服务器，具体步骤如下：
执行如下命令查看 IPv6 地址，并用 PuTTY 或者 Xshell 等软件，测试能否通过 IPv6 地址 ssh 到云服务器。
```
ifconfig
```
![](https://main.qcloudimg.com/raw/16838301e15e59ec20f8d3ffb1dd5a69.png)
成功结果如下图所示：
![](https://main.qcloudimg.com/raw/c951d48a32b010d00b481ed26082a1bb.png)
