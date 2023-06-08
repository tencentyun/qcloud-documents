如需实现单网卡多 IP，您可为弹性网卡申请辅助内网 IP，操作如下：

## 步骤一：分配辅助内网 IP
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 单击左侧目录中的 **IP 与网卡** > **弹性网卡**，进入弹性网卡列表页。
3. 单击需要申请辅助内网 IP 的实例 ID，进入详情页。
4. 单击选项卡中的 **IPv4 地址管理**，查看内网 IP 信息。
![](https://main.qcloudimg.com/raw/c360781a44e6a7f976c5fd3bf0b87bd0.png)
5. 单击**分配内网 IP**，在弹出框中选择自动分配，或手动填写要分配的内网 IP 地址，单击**确定**即可。
>?如果您选择手动填写，请确认填写内网 IP 在所属子网网段内，且不属于系统保留 IP。
>例如，所属子网网段为：`10.0.0.0/24`，则可填的内网 IP 范围 为：`10.0.0.2 - 10.0.0.254`。
>
![](https://main.qcloudimg.com/raw/1c9e2d055fb464d22559bf7e1d922a64.png)

## 步骤二：配置辅助内网 IP
登录上述弹性网卡绑定的云服务器，配置辅助内网 IP 使其生效，可参考如下操作：

### Linux 云服务器

#### REHL 系列操作系统
  - 适用的操作系统：TencentOS、CentOS 6/7/8、Red Hat 6/7/8、AlmaLinux、Rocky Linux 等。
  - 示例网卡：以主网卡 eth0 为例演示操作。如果您的操作对象为辅助弹性网卡，请根据实际情况修改网卡标识符。

1. 在云服务器中查看当前网络信息，并使用 route -n 命令查询默认网关。其中，netmask 为`255.255.255.0`，Gateway（默认网关）为`172.16.2.1`。
![](https://qcloudimg.tencent-cloud.cn/raw/e93e9254745398ebaf400bf2ed20fddd.png)
2. 修改网络配置文件
如果配置单个私网 IPv4 地址，运行`vi /etc/sysconfig/network-scripts/ifcfg-eth0:0`命令，并添加相应的配置项。
文件配置信息如下：
```
[root@mufei /]# vi /etc/sysconfig/network-scripts/ifcfg-eth0:0
DEVICE=eth0:0                 // 这里修改为eth0:0跟文件名保持一致
BOOTPROTO=static              // 协议为静态，用none也可以
HWADDR=00:0C:29:6F:62:A7      // MAC地址,与eth0一致
ONBOOT=yes                    // 开机启用此网卡
IPADDR=172.16.2.6           // 新绑定的IP
NETMASK=255.255.255.0         // 子网掩码
GATEWAY=172.16.2.1           // 网关
```
3. 启动网卡或重启网络服务（二选一）。
重启网卡如下：
```
[root@mufei /]# ifup eth0:0
```
4. 运行 `ifconfig` 查看配置效果。
配置1个辅助私网 IP 的效果示例如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b316d5a525f317c9d1963e5fc1c8cacc.png)
配置完成后，从同 VPC 内其他云服务器 Ping 测试辅助 IP 联通是否正常。
![](https://qcloudimg.tencent-cloud.cn/raw/006e74b128c463fe9d320afaa36a654c.png)

#### Debian 系列操作系统
  - 适用的操作系统：Ubuntu 18/20、Ubuntu 14/16、Debian 8/9/10。
  - 示例网卡：以主网卡 eth0 为例演示操作。如果您的操作对象为辅助弹性网卡，请根据实际情况修改网卡标识符。

1. 在云服务器中查看当前网络信息，并使用 `route -n` 命令查询默认网关。
2. 根据实例操作系统，选择配置辅助私网 IP 地址的方式。
	- Debian 系列：Ubuntu 18/20
Ubuntu 18.04 采用 netplan 作为网络配置管理，与16.04及之前的版本区别很大。
		1. 修改配置文件：`sudo vim /etc/netplan/50-cloud-init.yaml`
		配置文件内容如下：
```
ubuntu@VM-2-13-ubuntu:~$ sudo vim  /etc/netplan/50-cloud-init.yaml
network:
    version: 2
    ethernets:
        eth0:
            addresses:
            - 172.16.2.13/24  //主ip
            - 172.16.2.17/24  //辅助ip
            match:
                macaddress: 52:54:00:cb:12:30
            gateway4: 172.16.2.1     
```
		2. 运行配置后，生效命令：
```
ubuntu@VM-2-13-ubuntu:~$ sudo  netplan apply
```
		3. 通过“IP a”查看网卡信息确认配置生效。
	![](https://qcloudimg.tencent-cloud.cn/raw/fe2e89f251fc9f7e67e5c04f8ee27019.png)
		4. 同 vpc 服务器测试辅助 ip 确认联通正常。
![](https://qcloudimg.tencent-cloud.cn/raw/f9ef52d6e79242ba904247f975833633.png)
	- Debian 系列：Ubuntu 14/16、Debian 8/9/10。
		1. 运行 `vi /etc/network/interfaces` 命令打开网络配置文件，并新增相应的配置项。
```
auto eth0:0
iface eth0:0 inet static
address 172.16.2.2      //辅助ip
mask 255.255.255.0
```
		2. 运行 `/etc/init.d/networking restart` 使网卡配置生效。
![](https://qcloudimg.tencent-cloud.cn/raw/88c502454a8b01382a7333deb0310995.png)
		3. 运行 `ifconfig` 查看配置效果。
![](https://qcloudimg.tencent-cloud.cn/raw/56e851ba3042e0f615880c61734f594e.png)

#### SLES 系列操作系统
   - 适用的操作系统：OpenSUSE 15/42。
   - 示例网卡：以主网卡 eth0 为例演示操作。如果您的操作对象为辅助弹性网卡，请根据实际情况修改网卡标识符。

1. 运行 `vi /etc/sysconfig/network/ifcfg-eth0` 命令打开网络配置文件，添加如下配置项：
```
IPADDR_0=172.16.2.8     //辅助ip
NETMASK_0=255.255.255.0   //掩码
LABEL_0='0'    //子网卡编号
```
2. 运行 `service network restart` 或 `systemctl restart network` 命令重启网络服务。
3. 运行 `ifconfig` 查看配置效果
![](https://qcloudimg.tencent-cloud.cn/raw/6b7d0fa7a2cb5234af91be9fd6b3805a.png)


### Windows 云服务器
1. <span id="step1" />执行如下步骤，查看云服务器的 IP 地址、子网掩码和默认网关和 DNS 服务器：
 1. 在操作系统界面，选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;width:25px">，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: -3px 0px;">，打开 “Windows PowerShell” 窗口，执行如下命令：
```
ipconfig /all
```
 2. 记录输出的网络接口信息中的 IPv4 地址、子网掩码、默认网关和 DNS 服务器值。
![](https://main.qcloudimg.com/raw/1a4a6f0557ff809a27607fee24549eb3.png)
2. 进入操作系统的**控制面板** > **网络和 Internet** > **网络和共享中心**，单击命名为**以太网**的网卡进行编辑。
![](https://main.qcloudimg.com/raw/56b44bec57750b8e86a9c7f7aba40041.png)
3. 在**以太网状态**弹窗中，单击**属性**。
4. 在**以太网属性**弹窗中，选中 **Internet 协议版本4（TCP/IPv4）**并单击**属性**。
![](https://main.qcloudimg.com/raw/b224af9ef0d18ca24f8e799f9c5023df.png)
5. 在 **Internet 协议版本4（TCP/IPv4）属性**弹窗中，填写如下信息：
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数值</th>
</tr>
</thead>
<tbody><tr>
<td>IP 地址</td>
<td>上述 <a href="#step1">步骤1</a> 中的 IPv4 地址。</td>
</tr>
<tr>
<td>子网掩码</td>
<td>上述 <a href="#step1">步骤1</a> 中的子网掩码。</td>
</tr>
<tr>
<td>默认网关</td>
<td>上述 <a href="#step1">步骤1</a> 中的默认网关地址。</td>
</tr>
<tr>
<td>首选 DNS 服务器</td>
<td>上述 <a href="#step1">步骤1</a> 中的 DNS 服务器。</td>
</tr>
<tr>
<td>备用 DNS 服务器</td>
<td>上述 <a href="#step1">步骤1</a> 中的备用 DNS 服务器。如果未列出备用 DNS 服务器，则无需填写此参数。</td>
</tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/26fca0d8901235e7be62234c3e684e17.png" />
6. 单击**高级**，配置辅助内网 IP。
7. 在**高级 TCP/IP 设置**弹窗中的 **IP 地址**模块下，单击**添加**。
8. 在 **TCP/IP 地址**弹窗中，填写辅助内网 IP，上述 [步骤1](#step1) 中的子网掩码，单击**添加**，如下图所示。 
![](https://main.qcloudimg.com/raw/1fdcb2fa24e45057c5874dfbb20652bc.png)
9. 在 **Internet 协议版本4（TCP/IPv4）属性**弹窗中，单击**确定**。
10. 在**以太网属性**弹窗中，单击**确定**即可完成配置。
11. 在**以太网状态**弹窗中，单击**详细信息**，可查看已配置的 IP 信息，如下图所示。
![](https://main.qcloudimg.com/raw/172cb1189fe0886d6b0b6483a924f8cd.png)

 
