单个 CVM 可以绑定不超过限额数的公网 IP（含普通公网 IP 和 EIP），以实现流量转移，提高 CVM 的利用率。本文将为您介绍如何为 Linux 云服务器和 Windows 云服务器绑定多个 EIP。

## 前提条件
- 您已购买 Linux 云服务器和 Windows 云服务器，并且所属安全组开放了 ICMP 协议。
- 请确保您的公网 IP 在限额数内，具体限额请参见 [使用限制](https://cloud.tencent.com/document/product/1199/41648)。
- 请确保您单网卡绑定内网 IP 数在限额数内，具体限额请参见 [弹性网卡-使用限制](https://cloud.tencent.com/document/product/576/18527)。

## 操作步骤

### 步骤一：分配内网 IP
1. 登录 [CVM 控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=4)。
2. 在实例列表中单击您的 CVM ID，在详细信息页面，选择**弹性网卡**。
![](https://main.qcloudimg.com/raw/1e9965343cd6e71b2b48a6f27e01f5b6.png)
3. 在“弹性网卡”页面，单击主网卡右侧的**分配内网 IP**。
4. 在弹出的“分配内网IP”窗口中，选择自动分配或手动填写要分配的内网 IP ，若需分配多个内网 IP，请单击**新增**并填写要分配的内网 IP，完成后单击**确定**。
>?若选择手动填写要分配的内网 IP，请确认填写的内网 IP 在所属子网网段内，且不属于系统保留 IP。
>例如，所属子网网段为：`10.0.0.0/24`，则可填的内网 IP 范围 为：`10.0.0.2 - 10.0.0.254`，本次操作以手动填写 `10.0.0.3` 为例。
>
![](https://qcloudimg.tencent-cloud.cn/raw/33a3ee70ea03fae9b6ddccb0b9b5327c.png)


### 步骤二：绑定 EIP[](id:bindEIP)
1. 在“弹性网卡”页面，单击 <img src="https://main.qcloudimg.com/raw/57a0c76b72cd97bd80bf857cd30c867a.png" style="margin: 0;">，以展开主网卡信息。
![](https://main.qcloudimg.com/raw/ffa35df2be28027b390413f0d54176e4.png)
2. 在分配的类型为辅助 IP 的内网 IP 所在行，单击“已绑定公网 IP”栏下的**绑定**。
3. 在弹出的“绑定弹性公网IP”窗口中：
 - 若有可选的 EIP，选中并单击**确定**即可。
 - 若无可选的 EIP，可单击弹框上方的**新建**进行申请，详情请参见 [申请 EIP](https://cloud.tencent.com/document/product/1199/41698)，申请成功后返回弹出框并单击**刷新**，即可看见申请的 EIP，选中并单击**确定**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/6b742de292a1d10ecb7e14a7a8d0938f.png)
4. 在主网卡的列表中，即可查看相关内网 IP 绑定公网 IP 的信息。
![](https://qcloudimg.tencent-cloud.cn/raw/f1fef47ab8957e36cb911995433d6eb0.png)


### 步骤三：配置网卡
请根据您的云服务器操作系统类型，选择对应的配置网卡操作：
- [Linux 云服务器](#Linux)
- [Windows 云服务器](#Win)



#### Linux 云服务器[](id:Linux)
如下操作以 CentOS 7 云服务器为例：
1. 登录 [CVM 控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=4)。
2. 在实例列表中单击您的 CVM ID，在详细信息页面，选择**弹性网卡**。
3. 单击主网卡 ID，进入主网卡详情页，根据所属子网记录如下信息：
 - **子网掩码：**如下图所示，所属子网的 CIDR 位数为/24，即子网掩码为 `255.255.255.0`。
 - **网关：**如果您未更改其他设置，则网关为子网网段的首个 IP，如下图中的所属子网网段的首个 IP 即为`10.0.0.1`。
![](https://main.qcloudimg.com/raw/130af7fd24d0c052661bec7679545112.png)
4. 登录云服务器，具体操作请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
5. <span id="step5">执行如下命令，查看网卡信息，如下图所示，本例中主网卡名称为 eth0，具体查询结果以您实际为准。
   ```
   ip address 
   ```
 ![](https://main.qcloudimg.com/raw/a6bbd49ef85aa8f95ccdfcc839ec4383.png)
6. 执行如下命令，备份网卡信息。
>!网卡名称 **ethx** 请替换为[ 第5步 ](#step5)查询到的实际网卡名称。
> 
```
cp /etc/sysconfig/network-scripts/ifcfg-eth0{,.bak}
```
7. 执行如下命令，打开网卡配置文件。
```
vim /etc/sysconfig/network-scripts/ifcfg-eth0
```
8. 按 **i** 切换至编辑模式，把配置文件内容修改为：
```
# Created by cloud-init on instance boot automatically, do not edit.
#
# 此处修改为static
BOOTPROTO=static
DEVICE=eth0
#
# 注释此行
# HWADDR=52:54:00:8a:7a:64
#
# 添加如下几行
#
# 配置主ip
IPADDR0=10.0.0.2 # 步骤一：绑定 EIP 中查看到的主IP，请根据实际填写
NETMASK0=255.255.255.0 # 步骤3中所记录的子网掩码，请根据实际填写
# 配置辅助ip1
IPADDR1=10.0.0.3 # 步骤一：绑定 EIP 中手动填写的辅助IP，请根据实际填写
NETMASK1=255.255.255.0
# 如果您有多个辅助ip，请继续配置辅助ip2，辅助ip3...
#IPADDR2=10.0.0.4
#NETMASK2=255.255.255.0
#IPADDR3=10.0.0.5
#NETMASK3=255.255.255.0
#......
# 配置网关
GATEWAY=10.0.0.1 # 步骤3中所记录的网关，请根据实际填写
#
NM_CONTROLLED=no
ONBOOT=yes
PERSISTENT_DHCLIENT=yes
TYPE=Ethernet
USERCTL=no
```
 修改后，示例如下：
![](https://main.qcloudimg.com/raw/bbc5a78eab53c430eb3e0edcc04287aa.png)
9. 完成修改后，按 **Esc**，输入 **:wq!** 并回车，保存配置并返回。
10. 执行如下命令，重启网络服务。
```
systemctl restart network.service
```
11. 执行如下命令，查看 IP。
```
ip address 
```
 ![](https://main.qcloudimg.com/raw/40664f8d1eeae7d3ce3ae94a8e602310.png)




####  Windows 云服务器[](id:Win)
如下操作以 Windows 2012 云服务器为例：
1. 登录云服务器，具体操作请参见 [使用 RDP 文件登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435)。
2. <span id="step2" />执行如下步骤，查看云服务器的 IP 地址、子网掩码和默认网关和 DNS 服务器：
 1. 在操作系统界面，选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;width:25px">，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: -3px 0px;">，打开 “Windows PowerShell” 窗口，执行如下命令：
```
ipconfig /all
```
 2. 记录输出的网络接口信息中的 IPv4 地址、子网掩码、默认网关和 DNS 服务器值。
![](https://main.qcloudimg.com/raw/da1c82fdda00049668802559b8271799.png)
3. 进入操作系统的**控制面板**>**网络和 Internet**>**网络和共享中心**，单击命名为“以太网”的网卡进行编辑。
![](https://main.qcloudimg.com/raw/56b44bec57750b8e86a9c7f7aba40041.png)
4. 在“以太网状态”弹窗中，单击**属性**。
5. 在“以太网属性”弹窗中，选中**Internet 协议版本4（TCP/IPv4）**并单击**属性**。
![](https://main.qcloudimg.com/raw/b224af9ef0d18ca24f8e799f9c5023df.png)
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
<img src="https://main.qcloudimg.com/raw/b18a69d6b39f097af3d52e498d0dcfb7.png" />
7. 单击**高级**，配置辅助内网 IP。
8. 在“高级 TCP/IP 设置”弹窗中的 “IP 地址”模块下，单击**添加**。
9. 在 “TCP/IP 地址”弹窗中，填写 [步骤二：绑定 EIP](#bindEIP) 配置的辅助内网 IP，上述 [步骤2](#step2) 中的子网掩码，单击**添加**。若有多个辅助 IP，请重复上一步与当前步骤。
![](https://main.qcloudimg.com/raw/8bcb61eff44159b253eee726017e9744.png)
10. 在 “Internet 协议版本4（TCP/IPv4）属性”弹窗中，单击**确定**。
11. 在“以太网属性”弹窗中，单击**确定**即可完成配置。
12. 在“以太网状态”弹窗中，单击**详细信息**，可查看已配置的 IP 信息，如下图所示。
![](https://main.qcloudimg.com/raw/f6d04372be9fc71d59725e1d173cc1f3.png)

### 步骤四：结果验证
登录其他云服务器，执行 `ping <辅助 IP 外网地址>`命令，若显示如下信息则证明绑定成功。
>?若执行命令未得到如下结果，请检查 CVM 安全组配置是否开放 ICMP 协议。
>
![](https://main.qcloudimg.com/raw/b95843022195567bba1ce835c3f41bbf.png)
