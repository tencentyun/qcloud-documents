若单个 CVM 可绑定的公网 IP 的限额不满足您的需求时，可以添加辅助网卡来绑定多个公网 IP，以实现流量转移，提高 CVM 的利用率。本文将为您介绍如何为 Linux 云服务器和 Windows 云服务器添加辅助网卡并绑定多个 EIP。

## 前提条件
- 您已购买 Linux 云服务器和 Windows 云服务器，并且所属安全组开放了 ICMP 协议。
- 请确保您的公网 IP 在限额数内，具体限额请参见 [使用限制](https://cloud.tencent.com/document/product/1199/41648)。
- 请确保您的辅助网卡绑定内网 IP 数在限额数内，具体限额请参见 [弹性网卡-使用限制](https://cloud.tencent.com/document/product/576/18527)。

## 操作步骤
### <span id="add" />步骤一：添加辅助网卡
1. 登录 [CVM 控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=4)。
2. 在实例列表中，单击您的 CVM ID，在详细信息页面选择【弹性网卡】。
![](https://main.qcloudimg.com/raw/44111f021a232564c8a9502ae51e3445.png)
3. 在“弹性网卡”页面，单击【绑定弹性网卡】。
4. 在弹出的“绑定弹性网卡”窗口中，选择待绑定的弹性网卡。若您未创建弹性网卡，请单击【新建弹性网卡并绑定】，填写名称，选择弹性网卡的所属私有网络、子网后，选择分配的内网 IP （可自动分配也可手动填写），如需添加标签可展开【高级选项】进行添加。
>?
>- 若需分配多个 IP 请单击【增加一个辅助IP】。
>- 若选择手动填写要分配的内网 IP，请确认填写的内网 IP 在所属子网网段内，且不属于系统保留 IP。
>例如，所属子网网段为：`10.0.0.0/24`，则可填的内网 IP 范围 为：`10.0.0.2 - 10.0.0.254`，本次操作以手动填写 `10.0.0.7` 为主 IP，`10.0.0.8`为辅助 IP 为例。
>
![](https://main.qcloudimg.com/raw/99c25b7fd0708218cd385fd06a459643.png)
5. 在“弹性网卡”页面，单击 <img src="https://main.qcloudimg.com/raw/57a0c76b72cd97bd80bf857cd30c867a.png" style="margin: 0;">，以展开绑定的辅助网卡信息。
![](https://main.qcloudimg.com/raw/5032fdfa89ef927aadf89ef03fe997ba.png)
6. 在分配的 IP 的“已绑定公网 IP”栏下，单击【绑定】，分别为分配的 IP 绑定 EIP。
7. 在弹出的“绑定弹性公网IP”窗口中：
 - 若有可选的 EIP，选中并单击【确定】即可。
 - 若无可选的 EIP，可单击弹框上方的【新建】进行申请，详情请参见 [申请 EIP](1199/41698)，申请成功后返回弹出框并单击【刷新】，即可看见申请的 EIP，选中并单击【确定】即可。
![](https://main.qcloudimg.com/raw/a31ebe5ad4ac8bc6924af36279e2eb63.png)
8. 在辅助网卡的列表中，即可查看相关内网 IP 绑定公网 IP 的信息。
![](https://main.qcloudimg.com/raw/6768e7a3ce6052cbc4439459da9b764b.png)

### 步骤二：配置网卡
请根据您的云服务器操作系统类型，选择对应的配置网卡操作：
- [Linux 云服务器](#Linux)
- [Windows 云服务器](#Win)

#### <span id="Linux" />Linux 云服务器
如下操作以 CentOS 7 云服务器为例：
1. 登录 [CVM 控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=4)。
2. 在实例列表中单击您的 CVM ID，在详细信息页面，选择【弹性网卡】。
3. 单击辅助网卡 ID，进入辅助网卡详情页，根据所属子网记录如下信息：
 - **子网掩码：**如下图所示，所属子网的 CIDR 位数为/24，即子网掩码为 `255.255.255.0`。
 - **网关：**如果您未更改其他设置，则网关为子网网段的首个 IP，如下图中的所属子网网段的首个 IP 即为 `10.0.0.1`。
![](https://main.qcloudimg.com/raw/130af7fd24d0c052661bec7679545112.png)
4. 登录云服务器，具体操作请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://tcloud-doc.isd.com/document/product/213/5436)。
5. 执行如下命令，复制主网卡文件。
```
cp /etc/sysconfig/network-scripts/ifcfg-eth{0,1}
```
6. 执行如下命令，打开辅助网卡配置文件。
```
vim /etc/sysconfig/network-scripts/ifcfg-eth1
```
7. 按 **i** 切换至编辑模式，把配置文件内容修改为：
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
IPADDR0=10.0.0.7 # 步骤一：添加辅助网卡中手动填写的主IP，请根据实际填写
NETMASK0=255.255.255.0 # 步骤3中所记录的子网掩码，请根据实际填写
# 配置辅助ip1
IPADDR1=10.0.0.8 # 步骤一：添加辅助网卡中手动填写的辅助IP，请根据实际填写
NETMASK1=255.255.255.0 # 步骤3中所记录的子网掩码，请根据实际填写
#
# 配置网关
GATEWAY=10.0.0.1 # 步骤3中所记录的网关，请根据实际填写
#
NM_CONTROLLED=no
ONBOOT=yes
TYPE=Ethernet
USERCTL=no
PERSISTENT_DHCLIENT=yes
```
8. 完成修改后，按 **Esc**，输入 **wq!** 并回车，保存配置并返回。
9. 执行如下命令，打开`/etc/sysctl.conf`文件。
```
vim /etc/sysctl.conf
```
10. 按 **i** 切换至编辑模式，进行如下修改，关闭 `rp_filter` 校验。
```
# 找到第16行的 rp_filter 并注释
# net.ipv4.conf.default.rp_filter = 1   如果有就注释
# 在文件结尾加上如下4行
net.ipv4.conf.default.rp_filter = 0
net.ipv4.conf.all.rp_filter = 0
net.ipv4.conf.eth0.rp_filter = 0
net.ipv4.conf.eth1.rp_filter = 0
```
11. 完成修改后，按 **Esc**，输入 **wq!** 并回车，保存配置并返回。
12. 执行如下命令，使配置文件生效。
```
sysctl -p
```
13. 执行如下命令，重启网络服务。
```
systemctl restart network.service
```
14. 执行如下命令，查看 IP。
```
ip address
```
![](https://main.qcloudimg.com/raw/96250722974a05786034ca559fedec80.png)

#### <span id="Win" />Windows 云服务器
如下操作以 Windows 2012 云服务器为例：
1. 登录云服务器，具体操作请参见 [使用 RDP 文件登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435)。
2. <span id="step2" />执行如下步骤，查看云服务器辅助网卡的 IP 地址、子网掩码和默认网关和 DNS 服务器：
 1. 在操作系统界面，选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;width:25px">，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: -3px 0px;">，打开 “Windows PowerShell” 窗口，执行如下命令：
```
ipconfig /all
```
 2. 记录输出的“以太网适配器 以太网 2”信息中的 IPv4 地址、子网掩码、默认网关和 DNS 服务器值。
 ![](https://main.qcloudimg.com/raw/c12ee37a6aee579326275f1f02bc3416.png)
3. 进入操作系统的【控制面板】>【网络和 Internet】>【网络和共享中心】，单击命名为“以太网 2”的网卡进行编辑。
4. 在 “以太网 2 状态” 弹窗中，单击【属性】。
![](https://main.qcloudimg.com/raw/663f2c94b7c1fca7605b770affb249c8.png)
5. 在“以太网 2 属性”弹窗中，双击【Internet 协议版本4（TCP/IPv4）】。
![](https://main.qcloudimg.com/raw/6f5ad88fd6bdbea09ac206b587fd868a.png)
6. 在 “Internet 协议版本4（TCP/IPv4）属性”弹窗中，填写如下信息：
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数值</th>
</tr>
</thead>
<tbody><tr>
<td>IP 地址</td>
<td>上述 <a href="#step2">步骤2</a> 中的 IPv4 地址。</td>
</tr>
<tr>
<td>子网掩码</td>
<td>上述 <a href="#step2">步骤2</a> 中的子网掩码。</td>
</tr>
<tr>
<td>默认网关</td>
<td>上述 <a href="#step2">步骤2</a> 中的默认网关地址。</td>
</tr>
<tr>
<td>首选 DNS 服务器</td>
<td>上述 <a href="#step2">步骤2</a> 中的 DNS 服务器。</td>
</tr>
<tr>
<td>备用 DNS 服务器</td>
<td>上述 <a href="#step2">步骤2</a> 中的备用 DNS 服务器。如果未列出备用 DNS 服务器，则无需填写此参数。</td>
</tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/baa33bf96c2fc833006f5b17e0347c9b.png" />
7. 单击【高级】，配置辅助内网 IP。
8. 在“高级 TCP/IP 设置”弹窗中的 “IP 地址”模块下，单击【添加】。
9. 在 “TCP/IP 地址”弹窗中，填写 [步骤一：添加辅助网卡](#add) 配置的辅助内网 IP，上述 [步骤2](#step2) 中的子网掩码，单击【添加】。若有多个辅助 IP，请重复上一步与当前步骤。
![](https://main.qcloudimg.com/raw/28de15eed49b374969340748ea615a50.png)
10. 在 “Internet 协议版本4（TCP/IPv4）属性”弹窗中，单击【确定】。
11. 在“以太网 2 属性”弹窗中，单击【确定】即可完成配置。
12. 在“以太网 2 状态”弹窗中，单击【详细信息】，可查看已配置的 IP 信息，如下图所示。
![](https://main.qcloudimg.com/raw/23f9f5bd806787314efa7f8ec28ab5af.png)

### 步骤三：结果验证
登录其他云服务器，执行 `ping <辅助网卡公网地址>`命令，若显示以下信息证明绑定成功。
>?若执行命令未得到以下结果，请检查 CVM 安全组配置是否开放 ICMP 协议。
>
![](https://main.qcloudimg.com/raw/aa70b56e1c53fa94bfdb828f00c15b78.png)
