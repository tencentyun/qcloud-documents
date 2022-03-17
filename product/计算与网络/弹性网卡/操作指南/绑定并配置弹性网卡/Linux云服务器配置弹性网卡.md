本文将指引您在 Linux 操作系统下为云服务器配置弹性网卡。

本文提供两种常用镜像类型（CentOS 和 Ubuntu）的服务器配置弹性网卡的操作指导：
+ [CentOS 云服务器配置弹性网卡](#centos)
+ [Ubuntu 云服务器配置弹性网卡](#ubuntu)


## CentOS 云服务器 配置弹性网卡[](id:centos)

### 方式一：工具配置
>!
>+ 该方式适用于 CentOS 8.0、7.8、7.6、7.5、7.4和7.2版本。
>+ “nic-hotplug.tgz”工具将在绑定弹性网卡或云服务器重启时被触发，自动创建网卡配置文件，并下发弹性网卡的路由。
>+ 当云服务器已有弹性网卡时，请务必确保存量弹性网卡的路由均已正确配置，再执行工具配置新弹性网卡；如可以接受云服务器重启对业务的影响，也可在配置完成后，参考[ 步骤5 ](#step5)重启云服务器使工具配置对所有网卡均生效。
>

#### 操作步骤
1. 登录云服务器，在云服务器中直接执行如下命令下载 nic-hotplug.tgz 工具。 
```plaintext
wget https://iso-1255486055.cos.ap-guangzhou.myqcloud.com/nic-hotplug.tgz
```
2. 执行如下命令解压文件。
```plaintext
tar -zxvf nic-hotplug.tgz
```
3. 执行如下命令，赋予执行权限后，安装工具。
```plaintext
cd nic-hotplug
chmod +x ./install.sh
./install.sh
```
4.  参考 [绑定弹性网卡](https://cloud.tencent.com/document/product/576/18535)，绑定弹性网卡，绑定后可执行如下操作验证新增网卡 eth1 的路由已正常下发。
 1. 执行 ip rule show，可查看到 eth1 的策略路由已添加。
  ![](https://main.qcloudimg.com/raw/7900394af6f0f53871af6c4093f3e728.png)
 2. 执行 ip route show table eth1，可查看到 eth1 路由表信息。
 ![](https://main.qcloudimg.com/raw/75e122a79e96b81de31bf0124c2cf5eb.png)
5. [](id:step5)（可选）如有存量网卡，可在云服务器控制台或执行 `reboot` 命令重启云服务器，重启后所有网卡的路由将自动下发正常。
    控制台重启：
	![](https://main.qcloudimg.com/raw/f282450fba6a0a61102a3e674ead325b.png)
    命令重启：
  ![](https://main.qcloudimg.com/raw/84053ed92ec9eda498beaad1479af930.png)

### 方式二：手动配置
>?以 Centos 7.8举例。
>

#### 前提条件
已将弹性网卡绑定到云服务器，具体参考 [绑定弹性网卡](https://cloud.tencent.com/document/product/576/18535)。

#### 操作步骤	
1. 以管理员身份 [登录云服务器](https://cloud.tencent.com/document/product/213/35700)，执行如下命令，查看需配置（未显示 IP）的网卡信息，如图所示，需配置的网卡名称为 `eth1`：
```plaintext
ip addr
```
 ![](https://main.qcloudimg.com/raw/37c65397f52bce5702edb4b594bf708a.png)
2. 执行如下命令，进入`/etc/sysconfig/network-scripts/`文件夹：
```plaintext
cd /etc/sysconfig/network-scripts/
```
3. 根据实际情况创建新网卡的配置文件，如下以创建命名为 `ifcfg-eth1` 的配置文件为例 ：
   1. 输入命令：
```plaintext
cp ifcfg-eth0 ifcfg-eth1
```
   2. 输入命令修改配置文件内容：
```plaintext
vim ifcfg-eth1
```
   3. 按 “i” 切换至编辑模式，把配置文件内容修改为：
> ?查看弹性网卡上的 IP 地址与子网掩码的方法，请在 [附录](#.E9.99.84.E5.BD.95) 中进行查看。
> 
    + 方式一：静态手工配置 IP
```plaintext
DEVICE='eth1' # 此处填写步骤1中查看到的需配置的弹性网卡名称，请根据实际填写
NM_CONTROLLED='yes'
ONBOOT='yes'
IPADDR='192.168.1.62'  # 此处填写弹性网卡上的 IP 地址，请根据实际填写
NETMASK='255.255.255.192'  # 此处填写子网掩码，请根据实际填写
#GATEWAY='192.168.1.1'  # 填写网卡所在子网的网关 IP 地址，请根据实际填写，本例由于 eth1 和 eth0 在同一个子网，已经定义了网关，这里不再重复填写，避免网关冲突
```
	+ 方式二：动态获取 IP 地址
```plaintext
BOOTPROTO=dhcp     #自动获取 IP 地址
DEVICE=eth1        # 填写需配置的弹性网卡名
HWADDR=20:90:6F:63:98:CC    # 请替换为弹性网卡实际的 MAC 地址
ONBOOT=yes
PERSISTENT_DHCLIENT=yes
TYPE=Ethernet
USERCTL=no
PEERDNS=no
DEFROUTE=no    # 默认路由，即是否将该网卡设置为默认路由，此处为防止路由冲突不设置 eth1 为默认路由
```
  4. 修改后保存配置文件并退出（在 vim 的末行模式下按 “Esc”，输入 “wq!” 并回车）。
4. 输入如下命令，重启网络服务使配置生效。
>!如果您配置了 DNS，在重启网络后可能导致 resolv.conf 文件被重置，影响 DNS 解析，请评估后操作。
>
```plaintext
systemctl restart network
```
5. 检查和确认 IP 配置正确。
 1. 输入如下查看 IP 的命令。
 ```plaintext
ip addr
```
 2. 确认辅助网卡和辅助网卡上的 IP 可见，如下图所示。
 ![](https://main.qcloudimg.com/raw/d99d81a7bd973cb0a748d785c326cd22.png)
如果 IP 配置不正确，请执行如下检查：
	1. 检查配置文件是否正确，如不正确请重新配置。
	2. 检查网络是否重启，如未重启，请执行如下命令重启网络，使配置生效。
	```plaintext
	systemctl restart network
	```
6. 根据业务实际情况配置路由策略。
按照上述步骤配置好后，Linux 镜像依旧默认从主网卡发包。您可通过策略路由来指定报文从某个网卡进，并从该网卡返回。
 1. <span id="6.1">创建两张路由表。
```plaintext
echo "10 t1" >> /etc/iproute2/rt_tables    #10为自定义的路由ID，t1为自定义的路由表名称，请根据实际填写。
echo "20 t2" >> /etc/iproute2/rt_tables   #20为自定义的路由ID，t2为自定义的路由表名称，请根据实际填写。
```
 2. 给两个路由表添加默认路由，有两种方式。
     + 配置临时策略路由（即重启网络后路由消失，需重新配置），请执行如下命令。
  ```plaintext
ip route add default dev eth0 via 192.168.1.1 table 10   #192.168.1.1请替换为主网卡所属子网的网关
ip route add default dev eth1 via 192.168.1.1 table 20   #192.168.1.1请替换为辅助网卡所属子网的网关
```
<dx-alert infotype="explain" title="">
具体网关，请参考 [查看网关](#.E6.9F.A5.E7.9C.8B.E7.BD.91.E5.85.B3) 。</dx-alert>
    + 配置永久路由，即可利用配置文件将策略路由保存下来，此处以 centos7.8 为例。[](id:pzyjly)
       1. 编辑“/etc/sysconfig/network-scripts/”目录中的配置文件“route-网卡名”，如route-eth0。
  ```plaintext
vim /etc/sysconfig/network-scripts/route-eth0    # 编辑 route-eth0 文件
      ```
       2. 增加添加一行命令：`default dev [网卡名 如 eth0] via [该网卡的网关 如192.168.1.1] table [策略路由表的代号 如10]`，如下：       
 ```plaintext
default dev eth0 via 192.168.1.1 table 10        # 在 route-eth0 文件中为路由表10增加默认网关
```
		3. 按“ESC”，并输入“:wq!”保存并退出，然后再按照同样操作配置 route-eth1 文件。
      ```plaintext
vim /etc/sysconfig/network-scripts/route-eth1     # 编辑 route-eth1 文件
default dev eth1 via 192.168.1.1 table 20         # 在 route-eth1 文件中为路由表20增加默认网关
```
	   4. 重启网络使配置生效。
```plaintext
systemctl restart network
```
 3. 配置策略路由规则。
```plaintext
ip rule add from 192.168.1.5 table 10     #IP 请替换为主网卡上的 IP，请根据实际情况填写。
ip rule add from 192.168.1.62 table 20     #IP 请替换为辅助网卡上的 IP，请根据实际情况填写。
```   
7. 配置完成后，可用同一个子网下的 CVM，来 Ping 内网地址，能 Ping 通即说明配置成功。如无其他 CVM，可以给辅助网卡的内网 IP 绑定公网 IP，Ping 该公网 IP 来验证。

## Ubuntu 云服务器 配置弹性网卡[](id:ubuntu)
1. 以管理员身份[ 登录云服务器](https://cloud.tencent.com/document/product/213/35700)，执行如下命令，查看需配置（未显示 IP）的网卡信息，如图所示，需配置的网卡名称为 `eth1`：
```plaintext
ip addr
```
 ![](https://main.qcloudimg.com/raw/ade946a6b92207acb1fe80bef696379e.png)
2. 执行如下命令，进入`/etc/network/`文件夹。
```plaintext
cd /etc/network/
```
3. 修改配置文件 interfaces。
   1. 执行如下命令切换至 root 用户，并修改配置文件内容。
```plaintext
sudo su
vim interfaces
```
   2. 按 “i” 切换至编辑模式，并增加如下配置内容。
   <dx-alert infotype="explain" title="">
查看弹性网卡上的 IP 地址与子网掩码的方法，请在 [附录](#.E9.99.84.E5.BD.95) 中进行查看。
</dx-alert>
```plaintext
auto eth1 # 此处填写步骤1中查看到的需配置的弹性网卡名称，请根据实际填写
iface eth1 inet static # 此处填写步骤1中查看到的需配置的弹性网卡名称，请根据实际填写
address 172.21.48.3 # 此处填写弹性网卡上的 IP 地址，请根据实际填写
netmask 255.255.240.0 # 此处填写子网掩码，请根据实际填写
```
   3. 修改后保存配置文件并退出（在 vim 的末行模式下按 “Esc”，输入 “wq!” 并回车）。
4. 重启网卡 eth1。
 1. 执行如下命令切换至 root 用户，并安装 ifupdown。
```plaintext
sudo su
apt install ifupdown
```
 2. 关闭网卡 eth1。
```plaintext
ifdown eth1
```
 3. 启动网卡 eth1。
```plaintext
ifup eth1
```
5. 检查和确认 IP 配置正确。
 1. 输入如下命令查看 IP。
```plaintext
ip addr
```
 2. 确认辅助网卡和辅助网卡上的 IP 可见，如下图所示。
 ![](https://main.qcloudimg.com/raw/2c7060691fc51a212295e209a9dcee83.png)
 如果 IP 配置不正确，请执行如下检查：
  1. 检查配置文件是否正确，如不正确请重新配置。
  2. 检查网卡是否重启，如未重启，请执行如下命令重启网卡，使配置生效。
```plaintext
ifdown eth1
ifup eth1
```
6. 根据业务实际情况配置路由策略。
<dx-alert infotype="notice" title="">
按照上述步骤配置好后，Linux 镜像依旧默认从主网卡发包。您可通过策略路由来指定报文从某个网卡进，并从该网卡返回。该方式配置的为临时静态路由，网络重启后需要重新配置路由。
</dx-alert>

 1. 执行如下命令创建两张路由表。<span id="Linux6.1">
```plaintext
echo "10 t1" >> /etc/iproute2/rt_tables   #10为自定义的路由ID，t1为自定义的路由表名称，请根据实际填写。
echo "20 t2" >> /etc/iproute2/rt_tables    #20为自定义的路由ID，t2为自定义的路由表名称，请根据实际填写。
```
 2. 执行如下命令为两个路由表添加默认路由。
```plaintext
ip route add default dev eth0 via 172.21.48.1 table 10   #172.21.48.1要分别替换成主网卡所属子网的网关
ip route add default dev eth1 via 172.21.48.1 table 20   #172.21.48.1要分别替换成辅助网卡所属子网的网关
```
<dx-alert infotype="explain" title="">
具体网关，请参考 [查看网关](#.E6.9F.A5.E7.9C.8B.E7.BD.91.E5.85.B3) 。
</dx-alert>
 3. 执行如下命令，配置策略路由。
```plaintext
ip rule add from 172.21.48.11 table 10   #替换成主网卡上的 IP，请根据实际情况填写。
ip rule add from 172.21.48.3 table 20    #替换成辅助网卡上的 IP，请根据实际情况填写。
```
7. 配置完成后，可用同一个子网下的 CVM，来 Ping 内网地址，能 Ping 通即说明成功。如无其他 CVM，可以给辅助网卡的内网 IP 绑定公网 IP，Ping 该公网 IP 来验证。

## 附录

### 查看弹性网卡上的 IP 地址
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc) 。
2. 单击左侧目录中的 **IP 与网卡** > **弹性网卡**，进入弹性网卡列表页。
3. 单击弹性网卡 ID，进入详情页。
4. 选择 **IPv4 地址管理**标签页，查看弹性网卡上的 IP 地址，即内网 IP。
![](https://main.qcloudimg.com/raw/e13d8391fdf23565662408050caa89b8.png)

### 查看弹性网卡的子网掩码
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc) 。
2. 单击左侧目录中的 **IP 与网卡** > **弹性网卡**，进入弹性网卡列表页。
3. 单击弹性网卡 ID，进入详情页，查看弹性网卡的子网掩码。
如下图所示，所属子网的 CIDR 位数为/20，即弹性网卡的子网掩码为：`255.255.240.0`。
![](https://main.qcloudimg.com/raw/5ccac8fb71177dff5fa24061a13f1bea.png)
CIDR 位数与子网掩码的对应关系如下表所示：
<table style="width:400px;important!">
<thead>
<tr>
<th width="150px">CIDR 位数</th>
<th width="250px">子网掩码</th>
</tr>
</thead>
<tbody><tr>
<td>/28</td>
<td>255.255.255.240</td>
</tr>
<tr>
<td>/27</td>
<td>255.255.255.224</td>
</tr>
<tr>
<td>/26</td>
<td>255.255.255.192</td>
</tr>
<tr>
<td>/25</td>
<td>255.255.255.128</td>
</tr>
<tr>
<td>/24</td>
<td>255.255.255.0</td>
</tr>
<tr>
<td>/23</td>
<td>255.255.254.0</td>
</tr>
<tr>
<td>/22</td>
<td>255.255.252.0</td>
</tr>
<tr>
<td>/21</td>
<td>255.255.248.0</td>
</tr>
<tr>
<td>/20</td>
<td>255.255.240.0</td>
</tr>
<tr>
<td>/19</td>
<td>255.255.224.0</td>
</tr>
<tr>
<td>/18</td>
<td>255.255.192.0</td>
</tr>
<tr>
<td>/17</td>
<td>255.255.128.0</td>
</tr>
<tr>
<td>/16</td>
<td>255.255.0.0</td>
</tr>
</tbody></table>

### 查看网关
如果您未更改其他设置，则网关为子网网段的首个 IP。例如，子网网段为：`192.168.0.0/24`，则网关为：`192.168.0.1`。
如果您不清楚弹性网卡的所属子网网段，您可：
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc) 。
2. 单击左侧目录中的 **IP 与网卡** > **弹性网卡**，进入弹性网卡列表页。
3. 单击弹性网卡 ID，进入详情页，查看弹性网卡的所属子网，如下图中的所属子网网段的首个 IP 即为：`10.200.16.17`。
![](https://main.qcloudimg.com/raw/3497cabed23ed4af369ca4b978c611eb.png)
