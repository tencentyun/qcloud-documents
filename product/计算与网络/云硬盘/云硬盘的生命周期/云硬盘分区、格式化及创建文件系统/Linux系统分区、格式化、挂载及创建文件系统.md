实例可以识别连接的云硬盘并将其视为普通硬盘。用户可以使用任何文件系统将云块存储设备格式化、分区及创建文件系统。此后任何写入文件系统的数据均写入云硬盘中，并且对使用该设备的应用程序是透明的。本文档通过一个示例演示如何在云主机中使用块存储设备，并对一些需要注意的事项进行了详细的说明。您还可以从 [Windows 系统分区、格式化、联机及创建文件系统](https://cloud.tencent.com/document/product/362/6734
) 获得有关 Windows 实例上使用云硬盘的指引。

本示例使用的云主机启动时一并购买了一块 20GB 的系统盘和一块 30GB 的数据盘（即非弹性云硬盘），而后又在云硬盘控制台购买了一块 10GB 的弹性云盘。

## 前提条件
- 请确保您已进行 [将云硬盘连接到 CVM 实例](/doc/product/362/5745) 及 [登录 Linux 实例](/doc/product/213/5436)。
- <font color="red">格式化后，数据盘中的数据将被全部清空。请在格式化之前，确保数据盘中没有数据或对重要数据已进行备份。为避免服务发生异常，格式化前请确保云服务器已停止对外服务。</font>
- 当用户购买了多块云硬盘时，建议您对存放重要数据的弹性云盘设置自定义名称，并设置自动续费，防止因为没有及时续费导致弹性云盘到期对您的业务产生影响。 
- 用户可以在[云硬盘控制台](https://console.cloud.tencent.com/cvm/cbs)中根据自定义名称或者关联的云主机内网 IP 快速查找云硬盘。

本示例中，弹性云盘 ID 为 `ins-kjo6azag`，名称为`弹性云盘使用演示`。 


## 查看已挂载的硬盘
1) 运行`fdisk -l`命令查看硬盘信息。

此时可以看到随云主机创建的非弹性云硬盘 `vdb` 和刚刚挂载的弹性云盘 `vdc` 都尚未格式化。
![](//mccdn.qcloud.com/static/img/0096d7b0af255789bc68356ae8861ca7/image.png)

2) 执行 `ls -l /dev/disk/by-id/` 命令，可以在此处看到弹性云盘与设备名的对应关系。注意，非弹性云盘目前不会在这里显示任何信息。
![](//mccdn.qcloud.com/static/img/c004f380599b1ac12475f325f24b9d77/image.png)

硬盘从未进行初始化时，您需要先创建文件系统，然后才能够使用它。从快照创建的云硬盘中可能已经含有文件系统，<font color="red">如果您在现有的文件系统上创建新的文件系统，则将覆盖原有的全部数据。</font>

使用 `file -s device` 命令可列出特殊信息，例如文件系统类型。

```

sudo file -s /dev/xvdf
/dev/xvdf: data

```
如果前面的命令的输出仅显示该设备的 data，则说明设备上没有文件系统，您需要创建一个文件系统。您可继续下面的所有步骤。如果在包含文件系统的设备上运行此命令，则输出将有所不同，若返回形如 `Linux rev 1.0 ext4 filesystem data`的输出则说明此硬盘上已经创建了文件系统，您可以跳过分区和格式化操作。

- 若磁盘已经初始化，可从`System`字段判断是否需要创建新的文件系统。如果 System 字段显示 EXT3、EXT4 等文件系统类型，则不需新建文件系统，可以跳过分区和格式化操作步骤。

## （可选）对磁盘进行分区操作
1) 对云硬盘进行分区操作。当然用户也可以无需分区直接进行格式化操作。这里我们演示了将弹性云盘划分为两个分区使用。执行以下命令：
```
fdisk /dev/vdb
```
按照界面的提示，依次输入“n”(新建分区)、“p”(新建扩展分区)、“1”(使用第1个主分区)，两次回车(使用默认配置)，输入“wq”(保存分区表)，回车开始分区。

这里是以创建 1 个分区为例，开发者也可以根据自己的需求创建多个分区。
![](//mccdn.qcloud.com/img56a604c2b886f.png)

使用“fdisk -l”命令，即可查看到，新的分区 `vdb1` 已经创建完成。
![](//mccdn.qcloud.com/img56a605027a966.png)


![](//mccdn.qcloud.com/static/img/049a61e867c38eacbe636b11764461bf/image.png)

2) 分区后执行 `ls -l /dev/disk/by-id` 命令，可以看到以下内容：
![](//mccdn.qcloud.com/static/img/1b88d2d8deb8d7a421e65ce6e27b82d6/image.png)

##（有条件）硬盘格式化
> 此步骤假定您在处理初始化的硬盘。如果该硬盘已经包含数据（如，从快照创建的云硬盘），请勿使用 mkfs（而应跳到下一步）。否则，您会格式化并删除现有数据。

运行`mkfs.ext4 device_name`命令格式化并创建 ext4 文件系统。用设备名称（例如，/dev/vdb）替换 device_name。根据应用程序的要求或操作系统的限制，您可以选择其他文件系统类型，如 ext3 或 XFS。

![](//mccdn.qcloud.com/static/img/1339a1feb56d7eab4715146d52045f74/image.png)

## 挂载硬盘
```
mkdir /data/part1 -p  # 创建示例挂载点
mkdir /data/part5 -p # 创建示例挂载点
mount /dev/vdc1 /data/part1 # 将vdc1挂载到/data/part1处
mount /dev/vdc5 /data/part5 # 将vdc5挂载到/data/part5处
touch /data/part1/disk-bm42ztpm-part1.txt # 创建一个空文件用于后续演示
touch /data/part5/disk-bm42ztpm-part5.txt # 创建一个空文件用于后续演示
yum install tree -y # 安装一个用于展示目录结构的工具
tree /data  # 查看/data目录结构
```

此时可以看到如下的结构树：
![](//mccdn.qcloud.com/static/img/2f4b8f43bb0d19ee8e62761dcc51a5c1/image.png)

执行 `lsblk -f` 命令查询文件系统UUID和挂载点信息：
![](//mccdn.qcloud.com/static/img/5d14f104ce38e76af50758031aecab20/image.png)

## （可选）设置自动挂载

如果此时重启云主机，可以发现刚刚挂载点已经消失。如果希望云服务器在重启或开机时能自动 mount 数据盘，必须将分区信息添加到 `/etc/fstab` 中。如果没有添加则云服务器重启或重新开机后都不能自动挂载数据盘。在 `/etc/fstab` 配置文件中可以使用三种不同的方法使文件系统可以找到 mount 点：


|自动mount方法|优点|缺点|
|---|---|--|
|使用设备名称||假如您将云主机上的弹性云盘解挂后再次挂载（例如迁移数据时），该名称有可能会发生变化，因此有可能会导致您的自动挂载设置失效|
|使用文件系统 UUID||与文件系统相关，重新格式化文件系统后，UUID将会发生变化，因此有可能会导致您的自动挂载设置失效|
|使用弹性云盘软链接|与设备名及文件系统无关，与实际使用的云硬盘唯一对应的名称|只有弹性云盘才会有此软链接，无法感知到分区的格式化操作|

从下图可以看出，重新格式化文件系统后 UUID 发生了变化：
![](//mccdn.qcloud.com/static/img/12b7d1675e6cf0271a53f5a69213856c/image.png)

同理，从下图可以看出，在控制台卸载弹性云盘并重新挂载后，设备名称发生了变化：
![](//mccdn.qcloud.com/static/img/e31475d93916a83f5fba8cb31c456936/image.png)

综上，我们建议您始终使用第三种方式实现自动挂载弹性云盘。创建 `/etc/fstab` 文件的备份，保证意外损坏或删除文件的情况下，可以使用该备份。

```

 cp /etc/fstab /etc/fstab.backup

```

打开 `/etc/fstab` 文件。

```
vi /etc/fstab

使用弹性云盘软链接（推荐）
输入：device_name  mount_point  file_system_type  fs_mntops  fs_freq  fs_passno  

示例：
/dev/disk/by-id/virtio-disk-bm42ztpm-part1 /data/part1 ext3 defaults,nofail 0 1
/dev/disk/by-id/virtio-disk-bm42ztpm-part5 /data/part5 ext3 defaults,nofail 0 1
```
最后三个字段分别是文件系统安装选项、文件系统转储频率和启动时的文件系统检查顺序。一般使用示例中的值 (defaults,nofail 0 2)即可。有关 `/etc/fstab` 条目的更多信息，在命令行上输入 man fstab 即可查看。

运行 `mount -a` 命令，如果运行通过则说明文件正常，刚刚创建的文件系统会在下次启动时自动安装。


## （可选）使用自定义镜像及数据盘快照启动新实例时自动挂载数据盘
在启动新的云服务器实例时，如果用户指定 ***自定义镜像*** 及***数据盘快照***，腾讯云云硬盘可以支持启动云服务器实例后自动挂载（即不需要进行一系列的添加、分区、格式化等操作可直接读写数据盘）。用户需要在制作自定义镜像和数据盘快照前在原实例上进行一些操作，下文将详细描述。

在 Linux 系统下如果用户希望指定数据盘快照生产出来的云硬盘能够自动挂载至新的云服务器实例，指定的自定义镜像和数据盘快照必须满足以下要求：
- 数据盘在制作快照前 ***必须*** 已经格式化过，也即在原云服务器上已经 mount 成功。
- 系统盘在制作自定义镜像前，需要在 `/etc/rc.local` 文件中添加以下命令，将数据盘挂载点写入文件中：

```
mkdir -p <mount-point>
mount <device-id> <mount-point>
```

其中：`<mount-point>`请填入文件系统的挂载点如 `/mydata`， `<device-id>`请填入用户的实际文件分区位置，如 `/dev/vdb(无分区有文件系统的设备名)` 和 `/dev/vdb1(有分区有文件系统)` 。

只有同时满足以上两个条件才能保证新启动的 Linux 云服务器实例数据盘可以被自动识别和挂载。