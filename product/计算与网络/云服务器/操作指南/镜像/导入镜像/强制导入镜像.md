当用户的linux镜像因为某些原因无法[安装cloudinit](https://cloud.tencent.com/document/product/213/12587)时，可以使用`强制导入镜像`功能完成镜像的导入。此时，腾讯云无法对用户的云服务器进行初始化配置，因此需要用户设置脚本自行根据腾讯云提供的配置文件对云服务器进行配置。
## 限制条件及配置方法
### 申请权限
在您使用本功能前，请确保您已经开通了导入镜像权限。若您需要开通权限，请联系商务经理，并提交相关信息至工单系统申请。

### 镜像限制条件
* 镜像仍需要满足[导入镜像](https://cloud.tencent.com/document/product/213/4945)中关于linux镜像导入的镜像的限制（cloudinit除外）。
* 导入镜像的系统分区未满。
* 导入的镜像不得存在可以被远程利用的漏洞。
* 建议用户用强制导入镜像创建实例成功后立即修改密码。

### 镜像导入配置方法
用户强制导入的镜像并没有使用cloudinit，因此无法自动进行配置。腾讯云提供了包含了配置信息的cdrom设备供用户自行配置，用户需要挂载cdrom，然后读取`mount_point/qcloud_action/os.conf`的信息进行配置。如果用户有使用其他配置数据、UserData的需要，可以直接读取`mount_point/`下的文件。

#### os.conf配置文件内容
os.conf的基本内容如下：
<pre>
hostname=VM_10_20_xxxx
password=GRSgae1fw9frsG.rfrF
eth0&#95;ip&#95;addr=10.104.62.201
eth0&#95;mac&#95;addr=52:54:00:E1:96:EB
eth0&#95;netmask=255.255.192.0
eth0&#95;gateway=10.104.0.1
dns&#95;nameserver="10.138.224.65 10.182.20.26 10.182.24.12"
</pre>
**以上信息仅参数名有参考意义，参数值仅做示例。**

其中各个参数的意义如下：

|参数名称|参数意义|
|----------|----------|
|hostname|主机名|
|password|加密过的密码|
|eth0_ip_addr|eth0网卡的局域网IP|
|eth0_mac_addr|eth0网卡的MAC地址|
|eth0_netmask|eth0网卡的子网掩码|
|eth0_gateway|eth0网卡的网关|
|dns_nameserver|dns解析服务器|


#### 配置脚本解析

##### 注意事项
* 脚本应该开机自动执行。
* 脚本挂载 `/dev/cdrom`，然后读取挂载点下的`os_action/os.conf`文件获取配置信息。
* 腾讯云放置到cdrom中的密码为加密后的密码，用户可以使用`chpasswd -e`的方式设置。注意，加密后的密码可能包含特殊字符，建议放置到文件中后以`chpasswd -e < passwd_file`的方式设置。
* 使用强制导入镜像制作的实例再制作镜像时，需要保证脚本依然会被执行，以保证实例正确配置。或者在实例中安装cloudinit。

##### 示例
腾讯云提供一份基于centos的示例脚本，用户可以根据示例脚本制作针对自己镜像的配置脚本，需要注意：

* **该脚本需要在导入镜像前正确放置到系统中**。
* 该脚本不适合所有操作系统，用户需要根据自己的操作系统进行相对修改已满足语义。
* 该脚本需要设置为开机启动才能正确配置，请根据操作系统的类型实现该要求。(例如将脚本`os_config`放置到/etc/init.d/目录下 然后执行以下命令。）

```
chmod +x /etc/init.d/os_config
chkconfig --add os_config
```

然后通过 `chkconfig --list`检查`os_config`是否已经被添加到启动服务中。

* 用户需要自行保证脚本执行正确，如果镜像导入后遇到无法ssh连接实例，没有网络连接等问题首先尝试通过控制台连接到实例，重新执行脚本排查问题，如仍然无法处理，请联系客服。

以下为`os_config`脚本示例，用户可根据实际情况修改脚本。

```
#!/bin/bash
### BEGIN INIT INFO
# Provides:          os-config
# Required-Start:    $local_fs $network $named $remote_fs
# Required-Stop:
# Should-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: config of os-init job
# Description: run the config phase without cloud-init
### END INIT INFO

###################user settings#####################

cdrom_path=`blkid -L config-2`

load_os_config() {
	mount_path=$(mktemp -d /mnt/tmp.XXXX)
	mount /dev/cdrom $mount_path
	if [[ -f $mount_path/qcloud_action/os.conf ]]; then
		. $mount_path/qcloud_action/os.conf
		if [[ -n $password ]]; then
			passwd_file=$(mktemp /mnt/pass.XXXX)
			passwd_line=$(grep password $mount_path/qcloud_action/os.conf)
			echo root:${passwd_line#*=} > $passwd_file
		fi
		return 0
	else 
		return 1
	fi
	
}

cleanup() {
	umount /dev/cdrom
	if [[ -f $passwd_file ]]; then
		echo $passwd_file
		rm -f $passwd_file
	fi
	if [[ -d $mount_path ]]; then
		echo $mount_path
		rm -rf $mount_path
	fi
}

config_password() {
	if [[ -f $passwd_file ]]; then
		chpasswd -e < $passwd_file
	fi
}

config_hostname(){
	if [[ -n $hostname ]]; then
		sed -i "/^HOSTNAME=.*/d" /etc/sysconfig/network
		echo "HOSTNAME=$hostname" >> /etc/sysconfig/network
	fi
}

config_dns() {
    if [[ -n $dns_nameserver ]]; then
        dns_conf=/etc/resolv.conf
        sed -i '/^nameserver.*/d' $dns_conf
        for i in $dns_nameserver; do
            echo "nameserver $i" >> $dns_conf
        done
    fi
}

config_network() {
    /etc/init.d/network stop
    cat << EOF > /etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=eth0
IPADDR=$eth0_ip_addr
NETMASK=$eth0_netmask
HWADDR=$eth0_mac_addr
ONBOOT=yes
GATEWAY=$eth0_gateway
BOOTPROTO=static
EOF
    if [[ -n $hostname ]]; then
    	sed -i "/^${eth0_ip_addr}.*/d" /etc/hosts
		echo "${eth0_ip_addr} $hostname" >> /etc/hosts
	fi
    /etc/init.d/network start
}

config_gateway() {
	sed -i "s/^GATEWAY=.*/GATEWAY=$eth0_gateway" /etc/sysconfig/network
}

###################init#####################
start() {
	if load_os_config ; then
		config_password
		config_hostname
		config_dns
		config_network
		cleanup
		exit 0
	else 
		echo "mount ${cdrom_path} failed"
		exit 1
	fi
}

RETVAL=0

case "$1" in
	start)
		start
		RETVAL=$?
	;;
	*)
		echo "Usage: $0 {start}"
		RETVAL=3
	;;
esac

exit $RETVAL


```
