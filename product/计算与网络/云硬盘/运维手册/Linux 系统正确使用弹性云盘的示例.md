本示例演示了如何在 Linux 操作系统中正确使用弹性云盘。

本示例使用的云主机启动时一并购买了一块 20GB 的系统盘和一块 30GB 的数据盘（即非弹性云硬盘），而后又在云硬盘控制台购买了一块 10GB 的弹性云盘。接下来将演示该弹性云盘如何在云主机中使用，并对一些需要注意的事项进行了详细的说明。 

1) 根据说明[挂载弹性云盘](https://www.qcloud.com/doc/product/362/2922#2.-.E6.8C.82.E8.BD.BD.E5.BC.B9.E6.80.A7.E4.BA.91.E7.A1.AC.E7.9B.98)。本示例中，弹性云盘 ID 为 `ins-kjo6azag`，名称为`弹性云盘使用演示`。 

![](//mccdn.qcloud.com/static/img/22963202000e28f017c03b657c9200dd/image.png)
- 当用户购买了多块云硬盘时，建议您对存放重要数据的弹性云盘设置自定义名称，并设置自动续费，防止因为没有及时续费导致弹性云盘到期对您的业务产生影响。 
- 用户可以在[云硬盘控制台](https://console.qcloud.com/cvm/cbs)中根据自定义名称或者关联的云主机内网IP快速查找云硬盘 。

2) 输入`fdisk -l`查看硬盘信息。

此时可以看到随云主机创建的非弹性云硬盘 `vdb` 和刚刚挂载的弹性云盘 `vdc` 都尚未格式化。注意在下边的操作步骤中，我们将不会对 `vdb` 进行操作。 

![](//mccdn.qcloud.com/static/img/0096d7b0af255789bc68356ae8861ca7/image.png)

3) 执行 `ls -l /dev/disk/by-id/` 命令，可以在此处看到弹性云盘与设备名的对应关系。注意，非弹性云盘目前不会在这里显示任何信息。
![](//mccdn.qcloud.com/static/img/c004f380599b1ac12475f325f24b9d77/image.png)

4) 对弹性云盘进行分区操作。当然用户也可以无需分区直接进行格式化操作。这里我们演示了将弹性云盘划分为两个分区使用。

![](//mccdn.qcloud.com/static/img/049a61e867c38eacbe636b11764461bf/image.png)

> 这里的 `vdc1` 对应的是一个主分区，而 `vdc2` 对应的是一个扩展分区，`vdc5` 对应的是一个逻辑分区。关于三种分区方式的区别可以参考这里。 

5) 分区后执行 `ls -l /dev/disk/by-id` 命令，可以看到以下内容：
![](//mccdn.qcloud.com/static/img/1b88d2d8deb8d7a421e65ce6e27b82d6/image.png)

6) 现在我们分别对两个分区执行格式化操作。 
![](//mccdn.qcloud.com/static/img/1339a1feb56d7eab4715146d52045f74/image.png)

7) 依次执行以下命令：
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

8) 执行 `lsblk -f` 命令查询文件系统UUID和挂载点信息：
![](//mccdn.qcloud.com/static/img/5d14f104ce38e76af50758031aecab20/image.png)

9) 设置自动挂载。

如果此时重启云主机，可以发现刚刚挂载点已经消失。如果希望云服务器在重启或开机时能自动mount 数据盘，必须将分区信息添加到 `/etc/fstab` 中。如果没有添加则云服务器重启或重新开机后都不能自动挂载数据盘。在 `/etc/fstab` 配置文件中可以使用三种不同的方法使文件系统可以找到 mount 点：


|自动mount方法|优点|缺点|
|---|---|--|
|使用设备名称||假如您将云主机上的弹性云盘解挂后再次挂载（例如迁移数据时），该名称有可能会发生变化，因此有可能会导致您的自动挂载设置失效|
|使用文件系统 UUID||与文件系统相关，重新格式化文件系统后，UUID将会发生变化，因此有可能会导致您的自动挂载设置失效|
|使用弹性云盘软链接|与设备名及文件系统无关，与实际使用的云硬盘唯一对应的名称|只有弹性云盘才会有此软链接，无法感知到分区的格式化操作|



从下图可以看出，重新格式化文件系统后 UUID 发生了变化：
![](//mccdn.qcloud.com/static/img/12b7d1675e6cf0271a53f5a69213856c/image.png)

同理，从下图可以看出，在控制台卸载弹性云盘并重新挂载后，设备名称发生了变化：
![](//mccdn.qcloud.com/static/img/e31475d93916a83f5fba8cb31c456936/image.png)

综上，我们建议您始终使用第三种方式实现自动挂载弹性云盘：
```
vi /etc/fstab

# 使用弹性云盘软链接（推荐）
/dev/disk/by-id/virtio-disk-bm42ztpm-part1 /data/part1 ext3 defaults,nofail 0 1
/dev/disk/by-id/virtio-disk-bm42ztpm-part5 /data/part5 ext3 defaults,nofail 0 1
```

