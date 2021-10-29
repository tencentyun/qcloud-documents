Linux 云服务器配置 IPv6 有两种方式：[工具配置](#gjpz) 和 [手动配置](#manual)。请根据您的实际情况选择对应的方式，推荐您使用更高效的自动配置工具配置 IPv6 地址。

>?默认云服务器的 IPv6 地址仅具有私网通信能力，若您想要通过该 IPv6 地址访问公网或被公网访问，则需通过弹性公网 IPv6 为该 IPv6 地址开通公网能力，操作详情请参见 [为云服务器的 IPv6 地址开通公网](https://cloud.tencent.com/document/product/1142/47665#step4)。

- **工具配置**：指通过工具一键配置 IPv6，根据镜像类型及购买时间的不同，使用的配置方法也不同，具体如下表所示。
<table>
<tbody>
<tr>
<tr style="text-align:center;">
<th><strong>镜像类型</strong></th>
<th><strong>购买时间</strong></th>
<th><strong>是否默认已开启 IPv6</strong></th>
<th><strong>工具配置<br>（推荐）</strong></th>
</tr><tr>
<td >CentOS 8.0以上</td>
<td >任何时间购买</td>
<td >是</td>
<td >
<a href="#open">config_ipv6 工具</a>
</td>
</tr>
<tr >
<td rowspan="2">CentOS 7.5/CentOS 7.6</td>
<td>2019-06-30后购买</td>
<td>是</td>
<td >
<a href="#open">config_ipv6 工具</a>
</td>
</tr>
<tr>
<td>2019-06-30前购买</td>
<td>否</td>
<td >
<a href="#unopen">enable_ipv6 工具</a>
</td>
</tr>
<tr>
<td rowspan="2">CentOS 6.x/CentOS 7.x（不含7.5/7.6）</td>
<td>2019-11-13 01:00后购买</td>
<td>是</td>
<td >
<a href="#open">config_ipv6 工具</a>
</td>
</tr>
<tr>
<td>2019-11-13 01:00前购买</td>
<td>否</td>
<td >
<a href="#unopen">enable_ipv6 工具</a>
</td>
</tr>
<tr>
<td rowspan="2">
<ul>
<li>Ubuntu14.04/Ubuntu 12.04/Ubuntu 16/Ubuntu 18/Ubuntu16.04/Ubuntu18.04</li>
<li>Debian 8/Debian 9</li>
<li>CoreOS 17</li>
<li>Tencent Linux</li>
</ul>
</td>
<td>2019-11-13 01:00后购买</td>
<td>是</td>
<td >
<a href="#open">config_ipv6 工具</a>
</td>
</tr>
<tr>
<td>2019-11-13 01:00前购买</td>
<td>否</td>
<td >
<a href="#unopen">enable_ipv6 工具</a>
</td>
<tr>
<td rowspan="2" >FreeBSD、Suse、OpenSUSE
</td>
<td>2019-11-13 01:00前购买</td>
<td>否</td>
<td rowspan="2">不支持工具配置，
请参见 <a href="#manual">手动配置</a></td>
</tr>
<tr>
<td>2019-11-13 01:00后购买</td>
<td>是</td>
</tr >
</tbody>
</table>

- **手动配置**：需要您对 Linux 命令有一定的熟练掌握程度。本文列举了几种常用镜像的手动配置方法供您参考，如果您有其他镜像类型的手动配置需求，请 <a href="https://console.cloud.tencent.com/workorder/category?step=0" target="_blank">提交工单</a> 申请。
	- [CentOS 7.3/CentOS 7.5/ CentOS 7.6 配置 IPv6](#CentOS7.3)
	- [CentOS 6.8 配置 IPv6](#CentOS6.8)
	-  [Ubuntu 14/Ubuntu 16/Ubuntu 18 配置 IPv6](#Ubuntu18)
	- [Debian 8.2 配置 IPv6](#Debian8.2)
	- [OpenSUSE 42 配置 IPv6](#Opensuse)
	- [SUSE 10 配置IPv6](#suse)
	- [FreeBSD 11 配置 IPv6](#Freebsd11)


## 工具配置[](id:gjpz)

### config_ipv6 工具配置[](id:open)
config_ipv6 工具可以为已开启 IPv6 且已分配 IPv6 地址的 CVM 实例，一键配置 IPv6 地址。

#### 使用限制
- config_ipv6 工具仅适用于 VPC 网络环境下。
- config_ipv6 工具运行时会自动重启网卡、网络服务，短时间内网络可能会不可用，请慎重执行。

#### **操作步骤**
1. 登录云服务器，执行` ifconfig` 或 `ip address` 命令确定需要配置 IPv6 地址的网卡，如下图所示，本例 eth0 无 IPv6 地址（fe80::是本机私有地址）。
  <img src="https://main.qcloudimg.com/raw/beda0d051a43188ac9f6d07aef63ef9b.png" width="50%" />
2. 在云服务器中直接执行如下命令下载 config_ipv6 工具。
```plaintext
wget https://iso-1251783334.cos.ap-guangzhou.myqcloud.com/scripts/config_ipv6.sh
```
3. 赋予执行权限后使用管理员权限执行如下命令，配置过程中请输入`y`确认配置操作。
```plaintext
chmod +x ./config_ipv6.sh  # 赋予执行权限
./config_ipv6.sh [网卡名称]   # 网卡名称请根据步骤1查询到的实际接口填写，本例以 eth0 为例
# 示例 1：./config_ipv6.sh eth0
# 示例 2：./config_ipv6.sh eth1
```
 ![](https://main.qcloudimg.com/raw/2763e0e1cc85ece1ca63afa62226f90c.png)
3. 执行 `ifconfig` 查询 IPv6 地址的配置情况，出现如下所示报文表示配置成功。
  <img src="https://main.qcloudimg.com/raw/b6c466912558224a5543caaa72af668a.png" width="50%" />
4. （此步骤仅适用于 CoreOS 操作系统）重启云服务器，使上述配置生效。


#### **开机自动配置IPv6**
对于需要自动化配置 IPv6 实例的需求，例如大批量配置，建议您使用实例自定义数据配合脚本的方式来调用。详情请参见 [实例自定义数据](https://cloud.tencent.com/document/product/213/17525)。如下为脚本示例（假设是 RHEL 系列，Bash Shell 脚本）。

> ?该示例仅对 eth0 进行配置，实际操作时注意修改为实际使用的网卡名。
> 
```plaintext
#!/bin/sh
install_dir=/usr/sbin
install_path="$install_dir"/config-ipv6
if [ ! -f "$install_path" ]; then
    tool_url="https://iso-1251783334.cos.ap-guangzhou.myqcloud.com/scripts/config_ipv6.sh"
    # download the tool
    if ! wget "$tool_url" -O "$install_path"; then
        echo "[Error] download tool failed, code $?"
        exit "$?"
    fi
fi
# chmod the tool
if ! chmod +x "$install_path"; then
    echo "[Error] chmod tool failed, code $?"
    exit "$?"
fi
# run the tool
$install_path eth0
```

### enable_ipv6 工具配置[](id:unopen)
enable_ipv6 工具可以为已分配 IPv6 地址的 CVM 实例，一键配置 IPv6 地址。

#### **使用限制**
- enable_ipv6 工具仅适用于 VPC 网络环境下。
- enable_ipv6 工具运行时会自动重启网卡、网络服务，短时间内网络可能会不可用，请慎重执行。

#### **操作步骤**
1. 登录云服务器，在云服务器中直接执行如下命令下载 enable_ipv6 工具。
```plaintext
wget https://iso-1251783334.cos.ap-guangzhou.myqcloud.com/scripts/enable_ipv6.sh
```
2. 赋予执行权限后，使用管理员权限执行如下命令：
```plaintext
 chmod +x ./enable_ipv6.sh
 ./enable_ipv6.sh [网卡名称]  
 # 示例 1：./enable_ipv6.sh eth0
 # 示例 2：./enable_ipv6.sh eth1
```
3. （此步骤仅适用于 CoreOS 操作系统）重启云服务器，使上述配置生效。




## 手动配置[](id:manual)

### CentOS 7.3/CentOS 7.5/CentOS 7.6 配置 IPv6[](id:CentOS7.3)
1. 远程连接实例，具体操作请参见 [登录及远程连接](https://cloud.tencent.com/document/product/213/35701)。
2. 检查实例是否已开启 IPv6 功能支持，执行如下命令：
```plaintext
ip addr | grep inet6
或者
ifconfig | grep inet6
```
 + 若实例未开启 IPv6 功能支持，请根据下文继续开启 IPv6 功能支持。 
 + 若返回 `inet6` 相关内容，表示实例已成功开启 IPv6 功能支持，您可以跳至 [第6步](#centstep6) 继续操作。
3. 执行以下步骤修改并保存`sysctl.conf`文件。
 1. 执行如下命令，打开`etc`文件夹下的`sysctl.conf`文件。
```plaintext
vim /etc/sysctl.conf
```
 2.  按 “i” 切换至编辑模式，将如下的 IPv6 相关参数设置为0。
```plaintext
net.ipv6.conf.all.disable_ipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0
net.ipv6.conf.lo.disable_ipv6 = 0
```
    ![](https://main.qcloudimg.com/raw/dc1e37e0c3a89b170038ef28d6d0583d.png)
 3. 按 “Esc”，输入 “:wq”，保存文件并返回。
4. 执行如下命令，对参数进行加载。
```plaintext
sysctl -p
```
5. 执行如下命令，查看是否修改成功。
```plaintext
sysctl -a | grep ipv6 | grep disable
```
 显示结果如下，则已成功修改。
  ![](https://main.qcloudimg.com/raw/b1294c92045d0dc5c688c6afc970a412.png)
6. 执行以下步骤修改并保存`ifcfg-eth0`文件。[](id:centstep6)
 1. 执行如下命令，打开`/etc/sysconfig/network-scripts/`文件夹下的`ifcfg-eth0`文件。
```plaintext
vim /etc/sysconfig/network-scripts/ifcfg-eth0
```
  2.  按 “i” 切换至编辑模式，增加如下内容。
```plaintext
DHCPV6C=yes
```
    ![](https://main.qcloudimg.com/raw/7eb7d1dbf6e9773ca3282979587d4f55.png)
  3. 按 “Esc”，输入 “:wq”，保存文件并返回。
7. 执行以下步骤修改并保存`route6-eth0`文件。
 1. 执行如下命令，打开`/etc/sysconfig/network-scripts/`文件夹下的`route6-eth0`文件。
```plaintext
vim /etc/sysconfig/network-scripts/route6-eth0
```
  2. 按 “i” 切换至编辑模式，增加如下内容，为网卡的 IPv6 添加默认出口。
```plaintext
default dev eth0 via fe80::feee:ffff:feff:ffff
```
    ![](https://main.qcloudimg.com/raw/3baffe425e598460caf1fc2de45e10d8.png)
 3. 按 “Esc”，输入 “:wq”，保存文件并返回。
8. 执行如下命令，重新启动网卡。
```plaintext
service network restart
或者
systemctl restart network
```
9. 依次执行如下命令，查看是否已经获取到 IPv6 地址。
```plaintext
ifconfig
```
 若出现以下报文表示已成功获取到 IPv6 地址。
![](https://main.qcloudimg.com/raw/2e42f1a5e7b9672d60461fe05edfed52.png)
10. 请参考 [SSH 支持 IPv6 配置](#ssh-ipv6) 为 SSH 开启 IPv6 功能。

### CentOS 6.8 配置 IPv6[](id:CentOS6.8)
1. 远程连接实例，具体操作请参见 [登录及远程连接](https://cloud.tencent.com/document/product/213/35701)。
2. 检查实例是否已开启 IPv6 功能支持，执行如下命令：
```plaintext
ip addr | grep inet6
或者
ifconfig | grep inet6
```
 + 若实例未开启 IPv6 功能支持，请根据下文继续开启 IPv6 功能支持。 
 + 若返回`inet6`相关内容，表示实例已成功开启 IPv6 功能支持，您可以跳至 [第5步](#centstep5) 继续操作。
3. 执行以下步骤修改并保存`ipv6.conf`文件。
	1. 执行如下命令，打开`/etc/modprobe.d/`文件夹下的`ipv6.conf`文件。
```plaintext
vi /etc/modprobe.d/ipv6.conf
```
	2.  按 “i” 切换至编辑模式，将如下的内核参数设置为0。
```plaintext
options ipv6 disable=0
```
    ![](https://main.qcloudimg.com/raw/37a4754fd0a8f6192d5f3818bcd685fe.png) 
	3.  按 “Esc”，输入 “:wq”，保存文件并返回。
4. 执行以下步骤修改并保存`sysctl.conf.first`文件。
  1. 执行如下命令，打开`etc`文件夹下的`sysctl.conf.first`文件。
```plaintext
vim /etc/sysctl.conf.first
```
   2. 按 “i” 切换至编辑模式，将如下的配置文件参数设置为0。
```plaintext
net.ipv6.conf.all.disable_ipv6 = 0
```
    ![](https://main.qcloudimg.com/raw/e5faf656a6aa6fcbd8a4ac190a13759e.png)
   3. 按 “Esc”，输入 “:wq”，保存文件并返回。
5. 执行以下步骤修改并保存`network`文件。[](id:centstep5)
  1. 执行如下命令，打开`/etc/sysconfig/`文件夹下的`network`文件。
```plaintext
vi /etc/sysconfig/network
```
  2. 按 “i” 切换至编辑模式，增加如下内容。
```plaintext
NETWORKING_IPV6=yes
DHCPV6C=yes
```
    ![](https://main.qcloudimg.com/raw/477077b3418849b62dc7479df9839859.png)
   3. 按 “Esc”，输入 “:wq”，保存文件并返回。
6. 执行以下步骤修改并保存`route6-eth0`文件。
 1. 执行如下命令，打开或创建`/etc/sysconfig/network-scripts/`文件夹下的`route6-eth0`文件。
```plaintext
vim /etc/sysconfig/network-scripts/route6-eth0
```	
 2. 按 “i” 切换至编辑模式，增加如下内容，为网卡的 IPv6 添加默认出口。
```plaintext
default dev eth0 via fe80::feee:ffff:feff:ffff
```
    ![](https://main.qcloudimg.com/raw/3baffe425e598460caf1fc2de45e10d8.png)
 3. 按 “Esc”，输入 “:wq”，保存文件并返回。
7. 重启云服务器，若仅通过 `service network restart`，IPv6 无法正常加载。
8. 执行如下命令查看重启后 IPv6 是否已经正常加载。
```plaintext
sysctl -a | grep ipv6 | grep disable
```
 若出现以下报文说明 IPv6 已经正常加载。
![](https://main.qcloudimg.com/raw/866730d160b1f0b893b2c00cd0cb4257.png)
9. 依次执行如下命令，查看是否已经获取到 IPv6 地址。
```plaintext
ifconfig
```
 若出现以下报文说明成功获取 IPv6 地址。
 ![](https://main.qcloudimg.com/raw/cedd7cbd7f5e649c01345356fa0d2688.png) 
10. 请参考 [SSH 支持 IPv6 配置](#ssh-ipv6) 为 SSH 开启 IPv6 功能。




### Ubuntu 14/Ubuntu 16/Ubuntu 18 配置 IPv6[](id:Ubuntu18)
1. 远程连接实例，具体操作请参见 [登录及远程连接](https://cloud.tencent.com/document/product/213/35701)。
2. 检查实例是否已开启 IPv6 功能支持，执行如下命令：
```plaintext
ip addr | grep inet6
或者
ifconfig | grep inet6
```
 + 若实例未开启 IPv6 功能支持，请根据下文继续开启 IPv6 功能支持。 
 + 若返回`inet6`相关内容，表示实例已成功开启 IPv6 功能支持，您可以跳至 [第5步](#ubstep5) 或 [第6步](#ubstep6) 继续操作。
3. 运行如下命令，并做相应修改，开启 IPv6 功能支持。
```plaintext
vi /etc/sysctl.conf
```
 并做如下修改：
```plaintext
#net.ipv6.conf.all.disable_ipv6 = 1
#net.ipv6.conf.default.disable_ipv6 = 1
#net.ipv6.conf.lo.disable_ipv6 = 1

net.ipv6.conf.all.disable_ipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0
net.ipv6.conf.lo.disable_ipv6 = 0
```
4. 运行`sysctl -p`使配置生效。
5. <span id="ubstep5"/>如果镜像类型为 Ubuntu 14/Ubuntu16，请执行如下操作配置 IPv6。
 1. 运行如下命令，打开网卡配置文件。
```plaintext
vi /etc/network/interfaces
```
 `eth0`为网卡标识符，您需要修改成实际的标识符，在文件中根据实际信息添加以下配置：
	- 单 IPv6 地址：
```plaintext
auto eth0
iface eth0 inet6 static
address <IPv6地址>
netmask <子网前缀长度>
gateway <IPv6网关>
```
	- 多 IPv6 地址：
```plaintext
auto eth0
iface eth0 inet6 static
address <IPv6地址>
netmask <子网前缀长度>
gateway <IPv6网关>

auto eth0:0
iface eth0:0 inet6 static
address <IPv6地址1>
netmask <子网前缀长度>
gateway <IPv6网关>
auto eth0:1

iface eth0:1 inet6 static
address <IPv6地址2>
netmask <子网前缀长度>
gateway <IPv6网关>
```
 2. 重启网络服务：运行`service network restart` 或 `systemctl restart networking`。
6. <span id="ubstep6"/>如果镜像类型为 Ubuntu 18，请执行如下操作配置 IPv6。
 1. 编辑网卡配置文件。
```plaintext
vi /etc/netplan/50-cloud-init.yaml
```
 2. 添加 IPv6 地址和网关配置。
> !只添加 addresses 和 gateway6。
>
```plaintext
network:
version: 2
ethernets:
eth0:
dhcp4: true                         //开启dhcp4
match:
macaddress: 52:54:00:75:ce:c2  //MAC地址
set-name: eth0                      //网卡名
addresses:
		 - 2a00:7b80:454:2000::xxx/64    //设置IPv6地址和掩码
gateway6: 2a00:7b80:454::1          //设置IPv6网关地址
```
 3. 执行如下命令，使配置生效。
```plaintext
netplan apply
```
7. 请参考[ SSH 支持 IPv6 配置 ](#ssh-ipv6)开启 SSH 的 IPv6 功能。

<span id="Debian8.2"/>

### Debian 8.2 配置 IPv6[](id:Debian8.2)
1. 远程连接实例，具体操作请参见 [登录及远程连接](https://cloud.tencent.com/document/product/213/35701)。
2. 检查实例是否已开启 IPv6 功能支持，执行如下命令：
```plaintext
ip addr | grep inet6
或者
ifconfig | grep inet6
```
 + 若实例未开启 IPv6 功能支持，请根据下文继续开启 IPv6 功能支持。 
 + 若返回`inet6`相关内容，表示实例已成功开启 IPv6 功能支持，您可以跳至 [第5步](#debianstep5) 继续操作。
3. 执行以下步骤修改并保存`sysctl.conf`文件。
	1. 执行如下命令，打开`etc`文件夹下的`sysctl.conf`。
```plaintext
vim /etc/sysctl.conf
```
	2.  按 “i” 切换至编辑模式，将如下的 IPv6 相关参数设置为0。
```plaintext
net.ipv6.conf.all.disable_ipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0
```
	3.  按 “Esc”，输入 “:wq”，保存文件并返回。
4. 执行如下命令，对参数进行加载。
```plaintext
sysctl -p
```
5. <span id="debianstep5" />依次执行如下命令，查看是否已经获取到 IPv6 地址。
```plaintext
ifconfig
```
 若出现以下报文，证明成功获取 IPv6 地址。
![](https://main.qcloudimg.com/raw/cd5a2072c73307c79b7997bbd24cec13.png)
6. Debian 8.2 系统默认为 ssh（22端口）开启 IPv6 监听，无需特殊配置，您可执行如下命令，进行查看。
```plaintext
netstat -tupln
```
 ![](https://main.qcloudimg.com/raw/8bdb6f9672f81d8a6df56b61418fe492.png)
7. 执行如下命令，配置默认路由。
```plaintext
ip -6 route add default dev eth0 via fe80::feee:ffff:feff:ffff
```
8. 请参考[ SSH 支持 IPv6 配置](#ssh-ipv6) 为 SSH 开启 IPv6 功能。




### OpenSUSE 42 配置 IPv6[](id:Opensuse)
1. 远程连接实例，具体操作请参见 [登录及远程连接](https://cloud.tencent.com/document/product/213/35701)。
2. 执行如下命令，检查实例是否已开启 IPv6 功能支持。
```plaintext
ip addr | grep inet6
或者
ifconfig | grep inet6
```
 + 若实例未开启 IPv6 功能支持，请根据下文继续开启 IPv6 功能支持。 
 + 若返回`inet6`相关内容，表示实例已成功开启 IPv6 功能支持，您可以跳至 [第4步](#opensusestep4) 继续操作。
3. 运行如下命令，并做相应修改，开启 IPv6 功能支持。
```plaintext
vi /etc/sysctl.conf
```
 做如下修改：
```plaintext
#net.ipv6.conf.all.disable_ipv6 = 1
#net.ipv6.conf.default.disable_ipv6 = 1
#net.ipv6.conf.lo.disable_ipv6 = 1

net.ipv6.conf.all.disable_ipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0
net.ipv6.conf.lo.disable_ipv6 = 0
```
4. 运行`sysctl -p`使配置生效。
5. 配置 IPv6，OpenSUSE 42镜像类型的云服务器 IPv6 操作步骤有[ 脚本方式 ](#jbfs)和[ 手动方式 ](#sdfs)。请根据实际情况选择配置方式。[](id:opensusestep4)
 -  **脚本方式**[](id:jbfs)
    1. 将如下脚本拷贝到 shell 文件中，这里以 test.sh 为例。
		 + dev表示网卡设备名，例如 eth0、eth1。
		 + index 表示这是第几个 ipv6 地址，从0开始计数。
		 + ip6 表示本机的 ipv6 地址，例如2607:f0d0:1002:0011:0000:0000:0000:0002。
		 + prefix_len 表示子网前缀长度，例如64。
```plaintext
	dev=$1
		index=$2
	ip6=$3
		prefix_len=$4

		ifcfg_file="/etc/sysconfig/network/ifcfg-$dev"

		if [ ! -f "$ifcfg_file" ]; then
			touch "$ifcfg_file"
		fi

		echo -e "\nIPADDR_$index='$ip6'\nPREFIXLEN_$index='$prefix_len'" >> "$ifcfg_file"
		# update default IPv6 routing
	netip=$(echo $ip6 | awk -F":" '{print $1":"$2":"$3":"$4}')
		echo "default $netip::1 - $ifcfg" >> /etc/sysconfig/network/routes

	 service network restart
	```
    2. 执行脚本，举例如下。
```plaintext
./test.sh eth0 0 2402:4e00:1000:4200:0:8f0c:d527:b985 64
```
 - **手动方式**[](id:sdfs)
    1. 运行如下脚本，打开网卡配置文件。
```plaintext
vi /etc/sysconfig/network/ifcfg-eth0
```
    `eth0`为网卡标识符，您需要修改成实际的标识符。在文件中根据实际信息添加以下配置：
      - 单 IPv6 地址：
```plaintext
	IPADDR_0=<IPv6地址>
	PREFIXLEN_0=<子网前缀长度>
```
      - 多 IPv6 地址：
```plaintext
IPADDR_0=<IPv6地址>
PREFIXLEN_0=<子网前缀长度>

IPADDR_1=<IPv6地址1>
PREFIXLEN_1=<子网前缀长度>

IPADDR_2=<IPv6地址2>
PREFIXLEN_2=<子网前缀长度>
```
    2. 运行`vi /etc/sysconfig/network/routes`打开路由配置文件，添加配置项。
```plaintext
default <IPv6网关> - -
```
    3. 重启网络服务：运行`service network restart`或`systemctl restart networking`。
6. 请参考[ SSH 支持 IPv6 配置 ](#ssh-ipv6)开启 SSH 的 IPv6 功能。


### SUSE 10 配置 IPv6[](id:suse)
1. 远程连接实例，具体操作请参见 [登录及远程连接](https://cloud.tencent.com/document/product/213/35701)。
2. 运行如下命令，并做相应修改，开启 IPv6 功能支持。
```plaintext
vi /etc/sysctl.conf
```
 做如下修改：
```plaintext
#net.ipv6.conf.all.disable_ipv6 = 1
#net.ipv6.conf.default.disable_ipv6 = 1
#net.ipv6.conf.lo.disable_ipv6 = 1

net.ipv6.conf.all.disable_ipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0
net.ipv6.conf.lo.disable_ipv6 = 0
```
3. 运行`sysctl -p`使配置生效。
4. 配置 IPv6，SUSE 10镜像类型的云服务器 IPv6 操作步骤有 [脚本方式](#jbfs1) 和 [手动方式](#sdfs1)。请根据实际情况选择配置方式。
 - **脚本方式**[](id:jbfs1)
      1. 将如下脚本拷贝到 shell 文件中，这里以 test.sh 为例。
	 + dev 表示网卡设备名，例如 eth0、eth1。
	 + index 表示这是第几个 ipv6 地址，从0开始计数。
	 + ip6 表示本机的 ipv6 地址，例如2607:f0d0:1002:0011:0000:0000:0000:0002。
	 + prefix_len 表示子网前缀长度，例如64。
```plaintext
dev=$1
	index=$2
ip6=$3
	prefix_len=$4

	ifcfg_file="/etc/sysconfig/network/ifcfg-$dev"

	if [ ! -f "$ifcfg_file" ]; then
		touch "$ifcfg_file"
	fi
	echo -e "\nIPADDR_$index='$ip6'\nPREFIXLEN_$index='$prefix_len'" >> "$ifcfg_file"
	# update default IPv6 routing
netip=$(echo $ip6 | awk -F":" '{print $1":"$2":"$3":"$4}')
	echo "default $netip::1 - $ifcfg" >> /etc/sysconfig/network/routes
	service network restart
```
      2. 执行脚本，举例如下。
```plaintext
./test.sh eth0 0 2402:4e00:1000:4200:0:8f0c:d527:b985 64
```
 - **手动方式**[](id:sdfs1)
      1. 运行如下脚本，打开网卡配置文件。
```plaintext
vi /etc/sysconfig/network/ifcfg-eth0
```
     `eth0`为网卡标识符，您需要修改成实际的标识符。在文件中根据实际信息添加以下配置：
	 + 单 IPv6 地址：
```plaintext
IPADDR_0=<IPv6地址>
PREFIXLEN_0=<子网前缀长度>
```
	 + 多 IPv6 地址：
```plaintext
IPADDR_0=<IPv6地址>
PREFIXLEN_0=<子网前缀长度>

IPADDR_1=<IPv6地址1>
PREFIXLEN_1=<子网前缀长度>

IPADDR_2=<IPv6地址2>
PREFIXLEN_2=<子网前缀长度>
```
      2. 运行`vi /etc/sysconfig/network/routes`打开路由配置文件，添加配置项。
      ```plaintext
      default <IPv6网关> - -
      ```
      3. 重启网络服务：运行`service network restart`或`systemctl restart networking`。
5. 请参考[ SSH 支持 IPv6 配置](#ssh-ipv6) 开启 SSH 的 IPv6 功能。

### FreeBSD 11 配置 IPv6[](id:Freebsd11)
FreeBSD 11 配置 IPv6 有 [脚本方式](#jbfs2) 和 [手动方式](#sdfs2)，请根据实际情况选择配置方式。

#### 脚本方式[](id:jbfs2)
>!脚本方式配置会重启网络，请谨慎执行。
> 
1. 远程连接实例，具体操作请参见 [登录及远程连接](https://cloud.tencent.com/document/product/213/35701)。
2. 将如下脚本拷贝到 shell 文件中，这里以“test.sh”为例。
       + dev 表示网卡设备名，例如 eth0、eth1。
       + ip6 表示本机的 ipv6 地址，例如 2607:f0d0:1002:0011:0000:0000:0000:0002。
       + prefix_len 表示子网前缀长度，例如 64。
```plaintext
key_value_editer() 
{
local file=$1
local key=$2
local value=$3
[ ! -f "$file" ] && return
if ! grep -i "^${key}[[:space:]]*=" "$file" &>/dev/null; then
 echo "$key=$value" >> "$file"
else
 value=${value//\//\\/}
 sed -i "s/^${key}[[:space:]]*=.*/$key=$value/" "$file"
fi
}
dev=$1
ipv6=$2
prefix_len=$3
rc_conf_file="/etc/rc.conf"
if [ ! -f "$rc_conf_file" ]; then
exit 1
fi
# enable ipv6
sed -i -e "s/ipv6_network_interfaces='none'//" $rc_conf_file
sed -i -e "s/ipv6_activate_all_interfaces='NO'//" $rc_conf_file
key_value_editer "$rc_conf_file" "ipv6_activate_all_interfaces" "'YES'"
tail="_ipv6"
# config ipv6 address
echo "ifconfig_$dev$tail='inet6 $ipv6 prefixlen $prefix_len'" >> /etc/rc.conf
# config ipv6 defaultrouter
netip=$(echo $ipv6 | awk -F":" '{print $1":"$2":"$3":"$4}')
echo "ipv6_defaultrouter='$netip::1'" >> /etc/rc.conf
/etc/netstart restart
```
3. 执行脚本，举例如下。
```plaintext
sh ./test.sh vtnet0 2402:4e00:1000:4200:0:8f0c:d527:b985 64
```
4. 请参考[ SSH 支持 IPv6 配置 ](#ssh-ipv6)开启 SSH 的 IPv6 功能。

#### 手动方式[](id:sdfs2)
1. 远程连接实例，具体操作请参见 [登录及远程连接](https://cloud.tencent.com/document/product/213/35701)。
2. 运行`vi /etc/rc.conf`命令。
3. 删除`ipv6_network_interfaces='none'` ，并修改`ipv6_activate_all_interfaces='NO'`为`ipv6_activate_all_interfaces='YES'`后保存退出。
4. 运行`/etc/netstart restart`重启网络。
5. 运行`vi /etc/rc.conf`打开网卡配置文件，`vtnet0`为网卡标识符，您需要修改成实际的标识符。在文件中根据实际信息添加以下配置：
>?为区分单个 IPv6 与多个 IPv6 地址，您只需在同一网卡标识符的基础上重复添加地址信息即可。
> 
 - 单 IPv6 地址：
```plaintext
ipv6_ifconfig_vtnet0="<IPv6地址>"
ipv6_defaultrouter="<IPv6网关>"
```
 - 多 IPv6 地址：
```plaintext
ipv6_ifconfig_vtnet0="<IPv6地址1>"
ipv6_ifconfig_vtnet0="<IPv6地址2>"
ipv6_defaultrouter="<IPv6网关>"
```
6. 运行 `/etc/netstart restart` 重启网络服务，使配置生效。
7. 请参考[ SSH 支持 IPv6 配置 ](#ssh-ipv6)开启 SSH 的 IPv6 功能。


## 附录[](id:ssh-ipv6)

### SSH 支持 IPv6 配置
> !如果需要使用 IPv6 地址远程连接，则需要开启 ssh 的 IPv6 支持。
> 
1. 执行如下命令，打开 `/etc/ssh/`文件夹下的`sshd_config`文件。
```plaintext
vim /etc/ssh/sshd_config
```
2. 按 “i” 切换至编辑模式，删除对`AddressFamily any`的注释（即删除前面的`#`），为 ssh 等应用程序开启 IPv6 监听。
![](https://main.qcloudimg.com/raw/e0d64e3836b704bab4713697df865d81.png)
3. 按 “Esc”，输入 “:wq”，保存文件并返回。
4. 执行如下命令，重新加载配置。
```plaintext
service sshd reload
```
5. 执行`netstat -tupln`命令，若出现以下报文，表示查 ssh 已成功监听 IPv6。
![](https://main.qcloudimg.com/raw/4b3937053527ea3edd3efedfa0113ca9.png)
