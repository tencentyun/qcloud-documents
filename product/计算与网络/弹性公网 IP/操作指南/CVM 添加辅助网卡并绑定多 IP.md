云服务器（CVM ）添加辅助网卡后可以绑定不超过限额数的公网 IP（含普通公网 IP 和 EIP），本文将以 CentOS 7 云服务器和 Windows 2012 云服务器为例，介绍如何添加辅助网卡并绑定多个公网 IP。

## 前提条件
- 您已购买 CentOS 7 云服务器或 Windows 2012 云服务器，并且所属安全组开放了 ICMP 协议。
- 请确保您的公网 IP 在限额数内，具体限额请参见 [使用限制](https://cloud.tencent.com/document/product/1199/41648)。

## CentOS 7 云服务器添加辅助网卡并绑定多 IP
### 步骤一：添加辅助网卡
1. 登录 [CVM 控制台](https://console.cloud.tencent.com/cvm/overview)，在左侧导航栏单击【实例】。
2. 在实例列表中，单击您的 CVM ID，在详细信息页面选择【弹性网卡】。
![](https://main.qcloudimg.com/raw/44111f021a232564c8a9502ae51e3445.png)
3. 在“弹性网卡”页面，单击【绑定弹性网卡】。
4. 在弹出的“绑定弹性网卡”窗口中，选择待绑定的弹性网卡。若您未创建弹性网卡，请单击【新建弹性网卡并绑定】，填写名称，选择弹性网卡的所属私有网络、子网后，选择分配的内网 IP （可自动分配也可手动填写），如需添加标签可展开【高级选项】进行添加。
> ?若需分配多个 IP 请单击【增加一个辅助IP】。
> 
![](https://main.qcloudimg.com/raw/dc41f6263537973777ed22b30f5cb0d8.png)
5. 在“弹性网卡”页面，单击<img src="https://main.qcloudimg.com/raw/57a0c76b72cd97bd80bf857cd30c867a.png" style="margin: 0;">展开绑定的辅助网卡信息。
6. 在分配的 IP 的“已绑定公网 IP”栏下，单击【绑定】。
7. 在弹出的“绑定弹性IP”窗口中：
 - 若有可选的弹性公网 IP，选中并单击【确定】即可。
 - 若无可选的弹性公网 IP，可单击弹框上方的【新建】进行申请，详情请参见 [申请 EIP](1199/41698)，申请成功后返回弹出框并单击【刷新】，即可看见申请的弹性公网 IP，选中并单击【确定】即可。

### 步骤二：配置网卡
1. 登录 CentOS 7 云服务器，具体操作请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://tcloud-doc.isd.com/document/product/213/5436)。
2. 执行如下命令，复制主网卡文件。
```
cp /etc/sysconfig/network-scripts/ifcfg-eth{0,1}
```
3. 执行如下命令，打开辅助网卡配置文件。
```
vim /etc/sysconfig/network-scripts/ifcfg-eth1
```
4. 按 **i** 切换至编辑模式，把配置文件内容修改为：
```
# Created by cloud-init on instance boot automatically, do not edit.
#
# 此处修改为static
BOOTPROTO=static
#
# 此处改为eth1
DEVICE=eth1
# 注释此行
# HWADDR=52:54:00:8a:7a:64
# 添加如下几行
#
# 配置主ip
IPADDR0=10.2.1.211
NETMASK0=255.255.255.0
# 配置辅助ip1
IPADDR1=10.2.1.212
NETMASK1=255.255.255.0
#
# 配置网关
GATEWAY=10.2.1.1
#
NM_CONTROLLED=no
ONBOOT=yes
TYPE=Ethernet
USERCTL=no
PERSISTENT_DHCLIENT=yes
```
5. 完成修改后，按 **Esc**，输入 **wq!** 并回车，保存配置并返回。
6. 执行如下命令，打开`/etc/sysctl.conf`文件。
```
vim /etc/sysctl.conf
```
7. 按 **i** 切换至编辑模式，进行如下修改，关闭 `rp_filter` 校验。
```
# 找到第16行的 rp_filter 并注释
# net.ipv4.conf.default.rp_filter = 1   如果有就注释
# 在文件结尾加上如下4行
net.ipv4.conf.default.rp_filter = 0
net.ipv4.conf.all.rp_filter = 0
net.ipv4.conf.eth0.rp_filter = 0
net.ipv4.conf.eth1.rp_filter = 0
```
8. 完成修改后，按 **Esc**，输入 **wq!** 并回车，保存配置并返回。
9. 执行如下命令，使配置文件生效。
```
sysctl -p
```
10. 执行如下命令，重启网络服务。
```
systemctl restart network.service
```
11. 执行如下命令，查看 IP。
```
ip addr
```

### 步骤三：结果验证
登录其他云服务器，执行 `ping <辅助网卡公网地址>`命令，若显示以下信息证明绑定成功。
>?若执行命令未得到以下结果，请检查 CVM 安全组配置。
>
![](https://main.qcloudimg.com/raw/aa70b56e1c53fa94bfdb828f00c15b78.png)

## Windows 2012 云服务器添加辅助网卡并绑定多 IP
### 步骤一：添加辅助网卡
1. 登录 [CVM 控制台](https://console.cloud.tencent.com/cvm/overview)，在左侧导航栏单击【实例】。
2. 在实例列表中，单击您的 CVM ID，在详细信息页面选择【弹性网卡】。
![](https://main.qcloudimg.com/raw/44111f021a232564c8a9502ae51e3445.png)
3. 在“弹性网卡”页面，单击【绑定弹性网卡】。
4. 在弹出的“绑定弹性网卡”窗口中，选择待绑定的弹性网卡。若您未创建弹性网卡，请单击【新建弹性网卡并绑定】，填写名称，选择弹性网卡的所属私有网络、子网后，选择分配的内网 IP （可自动分配也可手动填写），如需添加标签可展开【高级选项】进行添加。
> ?若需分配多个 IP 请单击【增加一个辅助IP】。
> 
![](https://main.qcloudimg.com/raw/dc41f6263537973777ed22b30f5cb0d8.png)
5. 在“弹性网卡”页面，单击<img src="https://main.qcloudimg.com/raw/57a0c76b72cd97bd80bf857cd30c867a.png" style="margin: 0;">展开绑定的辅助网卡信息。
6. 在分配的 IP 的“已绑定公网 IP”栏下，单击【绑定】。
7. 在弹出的“绑定弹性IP”窗口中：
 - 若有可选的弹性公网 IP，选中并单击【确定】即可。
 - 若无可选的弹性公网 IP，可单击弹框上方的【新建】进行申请，详情请参见 [申请 EIP](1199/41698)，申请成功后返回弹出框并单击【刷新】，即可看见申请的弹性公网 IP，选中并单击【确定】即可。

### 步骤二：配置网卡
1. 登录 Windows 2012 云服务器，具体操作请参见 [使用 RDP 文件登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435)。
2. 进入操作系统的【控制面板】>【网络和 Internet】>【网络和共享中心】，单击命名为“以太网 2”的网卡进行编辑。
3. 在 “以太网 2 状态” 弹窗中，单击【属性】。
![](https://main.qcloudimg.com/raw/663f2c94b7c1fca7605b770affb249c8.png)
4. 在“以太网 2 属性”弹窗中，双击【Internet 协议版本4（TCP/IPv4）】。
![](https://main.qcloudimg.com/raw/6f5ad88fd6bdbea09ac206b587fd868a.png)
5. 在 “Internet 协议版本4（TCP/IPv4）属性”弹窗中，填写内网 IP 地址、子网掩码和网关、DNS 地址等信息。查看 DNS 地址具体操作请参见[内网 DNS](https://cloud.tencent.com/document/product/213/5225?from=3776#.E5.86.85.E7.BD.91-dns)。
![](https://main.qcloudimg.com/raw/e85d545792755daed4f4d535c3821f48.png)
6. 单击【高级】，配置辅助内网 IP。
7. 在“高级 TCP/IP 设置”弹窗中的 “IP 地址”模块下，单击【添加】。
![](https://main.qcloudimg.com/raw/9549151193063a3b690a48c460558c8c.png)
9. 在 “TCP/IP 地址”弹窗中，填写辅助内网 IP、子网掩码，单击【添加】。若有多个辅助 IP，请重复上一步与当前步骤。
![](https://main.qcloudimg.com/raw/62ed4c415fefffddc4000021de05b4a3.png)
10. 在操作系统界面，选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;width:25px">，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: -3px 0px;">，打开 “Windows PowerShell” 窗口，执行 `ipconfig`  命令查看配置的 IP。

### 步骤三：结果验证
登录其他云服务器，执行 `ping <辅助网卡公网地址>`命令，若显示以下信息证明绑定成功。
>?若执行命令未得到以下结果，请检查 CVM 安全组配置。
>
![](https://main.qcloudimg.com/raw/aa70b56e1c53fa94bfdb828f00c15b78.png)
