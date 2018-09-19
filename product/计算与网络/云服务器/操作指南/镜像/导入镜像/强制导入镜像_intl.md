If you cannot [install cloudinit](https://cloud.tencent.com/document/product/213/12587) in your Linux image for some reason, use `Forced Image Import` to import the image. At this point, Tencent Cloud cannot initialize your CVM. You need to define scripts to configure the CVM according to the configuration file provided by Tencent Cloud.
## Limits and Configuration
### Applying for Permission
Before using this feature, make sure that you have activated the image import permission. If you need to activate the permission, contact the Business Manager and submit relevant information to the ticket system.

### Image limits
* The image must meet the limits on importing Linux image in [Import Image](https://cloud.tencent.com/document/product/213/4945).
* The system partition for importing the image is not full.
* The imported image contains no vulnerability that can be exploited remotely.
* It is recommended that the user change the password immediately after the instance is created with forced image import.

### Configuration of image import
Images forcedly imported by users do not use cloudinit, so automatic configuration is not available. Tencent Cloud provides the CDROM device containing configuration information for users to manually configure the images. Users need to mount the CDROM and read the configuration information from `mount_point/qcloud_action/os.conf`. Users can directly read the files in `mount_point/` if other configuration data or UserData is required.

#### Content of os.conf configuration file
The content of os.conf is as follows.
<pre>
hostname=VM_10_20_xxxx
password=GRSgae1fw9frsG.rfrF
eth0&#95;ip&#95;addr=10.104.62.201
eth0&#95;mac&#95;addr=52:54:00:E1:96:EB
eth0&#95;netmask=255.255.192.0
eth0&#95;gateway=10.104.0.1
dns&#95;nameserver="10.138.224.65 10.182.20.26 10.182.24.12"
</pre>
**The parameter names above are for reference, and the values are only for example purpose.**

The description of the parameters is as follows:

| Parameter Name | Description |
|----------|----------|
|hostname|CVM name|
|password|Encrypted password |
|eth0_ip_addr|LAN IP of eth0 |
|eth0_mac_addr|MAC address of eth0 |
|eth0_netmask|Subnet mask of eth0 |
|eth0_gateway|Gateway of eth0 |
|dns_nameserver|DNS resolution server |


#### Configuration script parsing

##### Notes
* The script must be executed on startup.
* Mount `/dev/cdrom` and read `os_action/os.conf` file under the mount point to obtain configuration information.
* The password placed in the CDROM by Tencent Cloud is encrypted. Users can set new password with `chpasswd -e`. Note that the encrypted password may contain special characters. It is recommended to place the password in a file and set it with `chpasswd -e < passwd_file`.
* When creating images from an instance created by forced image import, be sure to execute the script for proper configuration, or install cloudinit in the instance.

##### Example
Tencent Cloud provides an example script based on CentOS for users to define scripts for their images. Note that:

* **The script must be properly placed in the system before image import**.
* The script does not apply to all operating systems. Users need to modify it according to their own operating systems.
* The script must be set to execute on startup for normal use. Make the configuration according to the type of operating system. (For example, place the script `os_config` under /etc/init.d/ directory and execute the following command.)

```
chmod +x /etc/init.d/os_config
chkconfig --add os_config
```

Run `chkconfig --list` to check if `os_config` is added to the startup service.

* Users must ensure that the script is properly executed. If problems such as failed to connect to the instance via SSH and failed to connect network occur after importing the image, try to connect to the instance in the console to execute the script again. If the problem remains, contact Customer Service.

The following is the example script `os_config`. Users can modify the script as needed.

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

