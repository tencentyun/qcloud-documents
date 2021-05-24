## 通过 Linux 客户端连接到卷
下面介绍如何在 Linux 下，使用 iscsi-initiator-utils RPM 包连接到网关 iSCSI 目标。

### 安装  iscsi-initiator-utils RPM 包 
使用下列命令安装该包，如果您已经安装过，请跳过此步骤。
```
sudo yum install iscsi-initiator-utils
```

### 验证 iSCSI 守护进程正在运行
使用下列命令验证 iSCSI 守护进程是否正在运行。
```
sudo /etc/init.d/iscsi status    //适用于RHEL 5 或 RHEL 6

sudo service iscsid status    //适用于RHEL 7
```

如果使用上述命令检查未返回 running 状态，请使用以下命令运行程序。
```
sudo /etc/init.d/iscsi start    
```

### 发现卷
请使用下列命令发现网关上的卷，如果使用上述命令检查未返回 running 状态，请使用以下命令运行程序。其中 GATEWAY_IP 需要替换为您的网关的 IP 变量。 网关 IP 可以到 CSG 控制台中的卷的 iSCSI Target Info (iSCSI 目标信息) 属性中找到网关 IP。
```
sudo /sbin/iscsiadm --mode discovery --type sendtargets --portal <GATEWAY_IP>:3260  
 
例如：
sudo /sbin/iscsiadm --mode discovery --type sendtargets --portal 192.168.190.11:3260
```

### 挂载卷
请使用如下命令挂载发现的卷。其中 TargetName 替换为需要挂载的卷的 TargetName，该信息可以到卷的详细信息页面获取； GATEWAY_IP 需要替换为您的网关的 IP 变量。
>!由于 iSCSI 协议限制，请勿将一个卷挂载到多个客户端上。

```
sudo /sbin/iscsiadm --mode node --targetname <TargetName> --portal <GATEWAY_IP> -l 
例如：
sudo /sbin/iscsiadm --mode node --targetname iqn.2003-07.com.qcloud:vol-10098 --portal 192.168.190.11:3260 -l
```

### 查看卷
您可以使用 fdisk –l、lsblk 等命令查看已经挂载的卷。当前状态下，卷已经成为一个裸磁盘可用。如果还需要安装文件系统，请参考下一个步骤。

![](https://main.qcloudimg.com/raw/616893311123b8912d996821a53511a2.png)

### 分区及格式化文件系统
- **执行以下命令，对数据盘进行分区。**
	```
	fdisk /dev/vdb
	```
	
	按照界面的提示，依次输入 "n" (新建分区)、"p"(新建扩展分区)、"1" (使用第1个主分区)，两次回车(使用默认配置)，输入 "wq" (保存分区表)，回车开始分区。这里是以创建 1 个分区为例，开发者也可以根据自己的需求创建多个分区。
	![](https://main.qcloudimg.com/raw/626e704268a87000aa443ed781ce7849.png)
	
- **查看分区**
	使用“fdisk -l”命令，即可查看到，新的分区 vdb1 已经创建完成。
	![](https://main.qcloudimg.com/raw/743c1027c37f8dfb3dec48f40da93ff8.png)
	
	
- **格式化分区**
	分区后需要对分好的区进行格式化，您可自行决定文件系统的格式，如 xfs、ext4 等，本例以“ext3”为例。请使用以下命令对新分区进行格式化。
	>!xfs 文件系统格式的稳定性相对较弱，但格式化速度快； ext 文件系统格式稳定性强，但是存储量越大格式化时间越长。请根据需要设置文件格式。
	
	```
	mkfs.ext3 /dev/vdb1
	```
	执行命令如下图所示：
	![](https://main.qcloudimg.com/raw/d54b711e170ff000ef5a360a0e9ce381.png)

- **挂载及查看分区**
	使用以下命令创建 mydata 目录并将分区挂载在该目录下：
	```
	mkdir /mydata
	mount /dev/vdb1 /mydata
	```

	然后使用以下命令查看
	```
	df -h
	```
	
	出现如下图信息则说明挂载成功，即可以查看到数据盘了。
	![](https://main.qcloudimg.com/raw/e2b0a2d9bc5d99989cc4873637cf540a.png)
	
- 	**自动挂载分区**
	如果希望云服务器在重启或开机时能自动挂载数据盘，必须将分区信息添加到/etc/fstab中。如果没有添加，则云服务器重启或重新开机后，都不能自动挂载数据盘。请使用以下命令添加分区信息：
	```
	echo '/dev/vdb1 /mydata ext3 defaults 0 0' >> /etc/fstab
	```

	使用以下命令查看
	```
	cat /etc/fstab
	```

	出现如下图信息则说明添加分区信息成功。
	![](https://main.qcloudimg.com/raw/fcf8458823bae33e434a33687cc95922.png)
	
	
### 卸载卷
如果挂载有误或者需要更换挂载的服务器，可以使用以下语句解除挂载。
```
sudo /sbin/iscsiadm --mode node --targetname <TargetName> --portal <GATEWAY_IP> -u
 
例如：
sudo /sbin/iscsiadm --mode node --targetname iqn.2003-07.com.qcloud:vol-10098 --portal 192.168.190.11:3260 -u
```

### 优化配置

为了保证您使用存储网关读写数据的稳定性，我们强烈建议您按照下列步骤进行优化配置。

- 修改读写请求超时配置
  通过提高 IO request 的 deadline timeout 配置，来保证卷的连接。其中，超时时间单位为秒，建议时间设置的较长一些，例如1个小时以上或者更多，有利于突发网络故障，保证业务不中断。
  
  找到并打开 /etc/udev/rules.d/50-udev.rules 文件，并找到如下的代码行。如果在 RHEL 6 / 7 的 Initiator 中未找到如下代码，请自行将如下代码添加该文件中并保存。
	```
	ACTION=="add", SUBSYSTEM=="scsi", SYSFS{type}=="0|7|14",\
	RUN+="/bin/sh -c 'echo 7200 > /sys$$DEVPATH/timeout'"  // RedHat 5
	
	ACTION=="add", SUBSYSTEM=="scsi",  ATTR{type}=="0|7|14",\
	RUN+="/bin/sh -c 'echo 7200 > /sys$$DEVPATH/timeout'"  // RedHat 6 和 RedHat 7
	```
	
  >!卸载卷会导致此项配置失效，因此，每次挂载完卷以后都要执行一次操作。
  
  查看上述配置的规则是否能够应用于当前系统，请输入以下命令，其中 "设备名" 需要替换成设备名称。
  	
	```
	udevadm test 设备名
	例如：udevadm test /dev/sda
	```
	使用如下命令验证是否已经应用生效，
  ```
	udevadm control --reload-rules && udevadm trigger 
	```
  
	
- 修改请求排队的最长时间
  找到并打开 /etc/iscsi/iscsi.conf 文件，找到下列代码并修改为建议值或更长。
	```
	node.session.timeo.replacement_timeout = 3600  //原值为 120 秒
	```
	
	说明：修改此数值后，当 Initiator 和 Csg 之间的网络连接异常断开时，Initiator 会尝试修复网络连接直到 replacement_timeout，然后再设置卷的状态为错误，对发下的每一个 IO 请求返回 -EIO。
	```
	node.conn[0].timeo.noop_out_interval = 60  //原值为5秒
	node.conn[0].timeo.noop_out_timeout = 600  //原值为5秒
	```
	
	修改此数值后，Initiator 会延长向 Csg 发送 HA 请求（ping）的间隔和超时判定，这样 Initiator 会尽可能的容忍和 Csg 的网络连接错误，不会轻易的判定和 Csg 之间发生不可恢复的网络故障
	
	在进行如上修改后，请执行如下命令重启 iSCSI 服务，来使配置生效。
	```
	service iscsid restart 
	```
	




