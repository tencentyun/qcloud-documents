当您购买了云硬盘并在控制台挂载至云服务器时，需要格式化才可使用。这里以CentOS为例进行说明。

1) 根据[挂载弹性云硬盘操作指南](https://www.qcloud.com/doc/product/362/%E4%BA%91%E7%A1%AC%E7%9B%98%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97#2.-.E6.8C.82.E8.BD.BD.E5.BC.B9.E6.80.A7.E4.BA.91.E7.A1.AC.E7.9B.98)进行云硬盘挂载

2) 输入命令`fdisk -l`查看您的云硬盘信息，注意：在没有分区和格式化数据盘之前，使用`df -h` 命令是无法看到数据盘的。在下面的示例中，有一个 54 GB 的数据盘(/vdb)需要挂载。
![](//mccdn.qcloud.com/img56a60467e297b.png)

3) 执行以下命令，对云硬盘进行分区。
```
fdisk /dev/vdb
```
按照界面的提示，依次输入“n”(新建分区)、“p”(新建扩展分区)、“1”(使用第1个主分区)，两次回车(使用默认配置)，输入“wq”(保存分区表)，回车开始分区。
这里是以创建1个分区为例，开发者也可以根据自己的需求创建多个分区。

![](//mccdn.qcloud.com/img56a604c2b886f.png)

使用“fdisk -l”命令，即可查看到，新的分区vdb1已经创建完成。
![](//mccdn.qcloud.com/img56a605027a966.png)

5) 分区后需要对分好的区进行格式化，您可自行决定文件系统的格式，如ext2、ext3等。本例以“ext3”为例：

使用下面的命令对新分区进行格式化。 

```
mkfs.ext3 /dev/vdb1
```
![](//mccdn.qcloud.com/img56a6053fb5aa0.png)

6) 使用以下命令创建mydata目录并将分区挂载在该目录下：
```
mkdir /mydata
mount /dev/vdb1 /mydata
```
最后用以下命令查看
```
df -h
```
出现如图信息则说明挂载成功，即可以查看到数据盘了。
![](//mccdn.qcloud.com/img56a60615c0984.png)

7) 如果希望云服务器在重启或开机时能自动挂载数据盘，必须将分区信息添加到/etc/fstab中。如果没有添加，则云服务器重启或重新开机后，都不能自动挂载数据盘。在`/etc/fstab`配置文件中可以使用三种不同的方法表示文件系统：内核名称、UUID 或者 label。对于独立购买的云盘，在使用fstab配置静态文件系统信息时，文件系统标识应使用文件系统的UUID或者label，防止由于多个独立云盘在同一子机上多次挂载、卸载后导致云盘在子机中的内核名称发生变化。
> 注：建议同时配置nofail选项，防止由于独立云盘从系统卸载后导致系统启动时报错。 

使用`lsblk -f`命令（MBR分区）或`blkid`命令（GPT分区）查看文件系统的label和uuid信息：
![](//mccdn.qcloud.com/static/img/9a8f1c4c2f465ea0711210b9b95920d1/image.png)

使用以下命令添加分区信息：
```
UUID=[disk uuid] 挂载点 文件系统类型 defaults,nofail 0 0
```

或通过云硬盘路径进行挂载：

```
ls -l /dev/disk/by-id/
```
找到disk id后，使用以下方式设置fstab：

```
/dev/disk/by-id/[disk-id] 挂载点 文件系统类型 defaults,nofail 0 0
```
![](//mccdn.qcloud.com/static/img/f2638a02c67cadf4335bb3c87c0a2ec2/image.png)

![](//mccdn.qcloud.com/static/img/d9cf9de2b1d9fd6d71ab071c959d099f/image.png)

可以看到，这时对应的文件系统结构为：
![](//mccdn.qcloud.com/static/img/1b40296fe6615f7075c7d178cc76f257/image.png)

