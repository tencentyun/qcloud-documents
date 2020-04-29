一个 CVM 服务器可以绑定不超过限额数的公网 IP（含普通公网 IP 和 EIP），本文将以 CentOS 7 云服务器和 Windows 2012 云服务器为例介绍如何绑定多个公网 IP。

## 前提条件
- 您已购买 CentOS 7 云服务器或 Windows 2012 云服务器，并且所属安全组开放了 ICMP 协议。
- 请确保您的公网 IP 在限额数内，具体限额请参见 [使用限制](https://cloud.tencent.com/document/product/1199/41648)。

## CentOS 7 服务器绑定多 IP
### 步骤一：绑定 EIP
1. 登录 [CVM 控制台](https://console.cloud.tencent.com/cvm/overview)，在左侧导航栏单击【实例】。
2. 在实例列表中单击您的 CVM ID，在详细信息页面，选择【弹性网卡】。
![](https://main.qcloudimg.com/raw/1e9965343cd6e71b2b48a6f27e01f5b6.png)
3. 在“弹性网卡”页面，单击主网卡右侧的【分配内网IP】。
4. 在弹出的“分配内网IP”窗口中，选择手动填写要分配的内网 IP ，若需分配多个内网 IP，请单击【新增】并填写要分配的内网 IP，完成后单击【确定】。
>?请确认手动填写的内网 IP 在所属子网网段内，且不属于系统保留 IP。
>例如，所属子网网段为：`10.0.0.0/24`，则可填的内网 IP 范围 为：`10.0.0.2 - 10.0.0.254`。
>
![](https://main.qcloudimg.com/raw/52a8ef1b3ea39a692fc764ea9a4291c6.png)
5. 在“弹性网卡”页面，单击<img src="https://main.qcloudimg.com/raw/57a0c76b72cd97bd80bf857cd30c867a.png" style="margin: 0;">展开主网卡信息。
6. 在分配的辅助 IP 的“已绑定公网 IP”下，单击【绑定】。
7. 在弹出的“绑定弹性IP”窗口中：
 - 若有可选的弹性公网 IP，选中并单击【确定】即可。
 - 若无可选的弹性公网 IP，可单击弹框上方的【新建】进行申请，详情请参见 [申请 EIP](1199/41698)，申请成功后返回弹出框并单击【刷新】，即可看见申请的弹性公网 IP，选中并单击【确定】即可。

### 步骤二：配置网卡
1. 登录 CentOS 7 云服务器，具体操作请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://tcloud-doc.isd.com/document/product/213/5436)。
2. 执行如下命令，备份网卡信息。
```
cp /etc/sysconfig/network-scripts/ifcfg-eth0{,.bak}
```
3. 执行如下命令，打开网卡配置文件。
```
vim /etc/sysconfig/network-scripts/ifcfg-eth0
```
4. 按 **i** 切换至编辑模式，把配置文件内容修改为：
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
IPADDR0=10.2.1.62
NETMASK0=255.255.255.0
# 配置辅助ip1
IPADDR1=10.2.1.101
NETMASK1=255.255.255.0
# 配置辅助ip2
IPADDR2=10.2.1.102
NETMASK2=255.255.255.0
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
6. 执行如下命令，重启网络服务。
```
systemctl restart network.service
```
7. 执行如下命令，查看 IP。
```
ip addr 
```

### 步骤三：结果验证
登录其他服务器，执行 `ping <辅助 IP 外网地址>`命令，若显示以下信息证明绑定成功。
>?若执行命令未得到以下结果，请检查 CVM 安全组配置。
>
![](https://main.qcloudimg.com/raw/b95843022195567bba1ce835c3f41bbf.png)

## Windows 服务器绑定多 IP
### 步骤一：绑定 EIP
1. 登录 [CVM 控制台](https://console.cloud.tencent.com/cvm/overview)，在左侧导航栏单击【实例】。
2. 在实例列表中单击您的 CVM ID，在详细信息页面，选择【弹性网卡】。
![](https://main.qcloudimg.com/raw/1e9965343cd6e71b2b48a6f27e01f5b6.png)
3. 在“弹性网卡”页面，单击主网卡右侧的【分配内网IP】。
4. 在弹出的“分配内网IP”窗口中，选择手动填写要分配的内网 IP ，若需分配多个内网 IP，请单击【新增】并填写要分配的内网 IP，完成后单击【确定】。
>?请确认手动填写的内网 IP 在所属子网网段内，且不属于系统保留 IP。
>例如，所属子网网段为：`10.0.0.0/24`，则可填的内网 IP 范围 为：`10.0.0.2 - 10.0.0.254`。
>
![](https://main.qcloudimg.com/raw/52a8ef1b3ea39a692fc764ea9a4291c6.png)
5. 在“弹性网卡”页面，单击<img src="https://main.qcloudimg.com/raw/57a0c76b72cd97bd80bf857cd30c867a.png" style="margin: 0;">展开主网卡信息。
6. 在分配的辅助 IP 的“已绑定公网 IP”下，单击【绑定】。
7. 在弹出的“绑定弹性IP”窗口中：
 - 若有可选的弹性公网 IP，选中并单击【确定】即可。
 - 若无可选的弹性公网 IP，可单击弹框上方的【新建】进行申请，详情请参见 [申请 EIP](1199/41698)，申请成功后返回弹出框并单击【刷新】，即可看见申请的弹性公网 IP，选中并单击【确定】即可。

### 步骤二：配置网卡
1. 登录 Windows 2012 云服务器，具体操作请参见 [使用 RDP 文件登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435)。
2. <span id="step2" />执行如下步骤，查找云服务器的 IP 地址、子网掩码和默认网关和 DNS 服务器：
 1. 在操作系统界面，选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;width:25px">，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: -3px 0px;">，打开 “Windows PowerShell” 窗口，执行如下命令：
```
ipconfig /all
```
 2. 记录输出的网络接口信息中的 IPv4 地址、子网掩码、默认网关和 DNS 服务器值。
![](https://main.qcloudimg.com/raw/1a4a6f0557ff809a27607fee24549eb3.png)
3. 进入操作系统的【控制面板】>【网络和 Internet】>【网络和共享中心】，单击命名为“以太网”的网卡进行编辑。
![](https://main.qcloudimg.com/raw/56b44bec57750b8e86a9c7f7aba40041.png)
4. 在“以太网状态”弹窗中，单击【属性】。
5. 在“以太网属性”弹窗中，选中【Internet 协议版本4（TCP/IPv4）】并单击【属性】。
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
<td>上述 <a href="#step2">步骤1</a> 中的 IPv4 地址。</td>
</tr>
<tr>
<td>子网掩码</td>
<td>上述 <a href="#step2">步骤1</a> 中的子网掩码。</td>
</tr>
<tr>
<td>默认网关</td>
<td>上述 <a href="#step2">步骤1</a> 中的默认网关地址。</td>
</tr>
<tr>
<td>首选 DNS 服务器</td>
<td>上述 <a href="#step2">步骤1</a> 中的 DNS 服务器。</td>
</tr>
<tr>
<td>备用 DNS 服务器</td>
<td>上述 <a href="#step2">步骤1</a> 中的备用 DNS 服务器。如果未列出备用 DNS 服务器，则无需填写此参数。</td>
</tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/26fca0d8901235e7be62234c3e684e17.png" />
7. 单击【高级】，配置辅助内网 IP。
8. 在“高级 TCP/IP 设置”弹窗中的 “IP 地址”模块下，单击【添加】。
9. 在 “TCP/IP 地址”弹窗中，填写辅助内网 IP，上述 [步骤1](#step1) 中的子网掩码，单击【添加】，如下图所示。 
![](https://main.qcloudimg.com/raw/1fdcb2fa24e45057c5874dfbb20652bc.png)
10. 在 “Internet 协议版本4（TCP/IPv4）属性”弹窗中，单击【确定】。
11. 在“以太网属性”弹窗中，单击【确定】即可完成配置。
12. 在“以太网状态”弹窗中，单击【详细信息】，可查看已配置的 IP 信息，如下图所示。
![](https://main.qcloudimg.com/raw/172cb1189fe0886d6b0b6483a924f8cd.png)

### 步骤三：结果验证
登录其他服务器，执行 `ping <辅助 IP 外网地址>`命令，若显示以下信息证明绑定成功。
>?若执行命令未得到以下结果，请检查 CVM 安全组配置。
>
![](https://main.qcloudimg.com/raw/b95843022195567bba1ce835c3f41bbf.png)
