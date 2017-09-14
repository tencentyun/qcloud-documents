用户在云服务器购买页购买数据盘时默认是脱机状态不自动挂载，数据盘未做分区和格式化时无法使用。本教程将引导您进行Windows系统挂载数据盘，分区以及格式化。

虽然不同的Windows版本（win2012,win2008,win2003等）在进入“磁盘管理”界面的路径不同，但进入磁盘管理界面后对于磁盘分区格式化的操作基本一致。

本文将从Windows2012，Windows2008两种系统来引导用户进行数据盘挂载、分区和格式化。

>注：

> <font color="red">格式化后，数据盘中的数据将被全部清空。请在格式化之前，确保数据盘中没有数据或对重要数据已进行备份。为避免服务发生异常，格式化前请确保云服务器已停止对外服务。</font>

## 1. Windows2012磁盘分区和格式化

Win2012进入磁盘管理的路径为：【开始】-【服务器管理】-【工具】-【计算机管理】-【磁盘管理】。

点击【开始】按钮：

![](//mccdn.qcloud.com/img56b1ae00cc2f5.jpg)

点击【服务器管理】：

![](//mccdn.qcloud.com/img56b1ae17e6f48.jpg)

点击【工具】-【计算机管理】：

![](//mccdn.qcloud.com/img56b1aed3a67b3.jpg)

点击【磁盘管理】：

![](//mccdn.qcloud.com/img56b1af025f7e1.jpg)

如下图所示，”磁盘1”为未分区的磁盘，这里以对”磁盘1”进行1个分区为例进行说明。在磁盘1上右键点击，选择【联机】：

![](//mccdn.qcloud.com/img56b1b00b8935c.jpg)

再一次右键点击，选择【初始化磁盘】：

![](//mccdn.qcloud.com/img56b1b057ada88.jpg)

根据分区方式的不同，选择【GPT】或【MBR】，点击【确定】按钮：

![](//mccdn.qcloud.com/img56b1b0a1cd741.jpg)

>注：磁盘大于2TB，一定要选择GPT分区形式。

在未分配的空间处右击，选择【新建简单卷】：

![](//mccdn.qcloud.com/img56b1b0bead71b.jpg)

在弹出的“新建简单卷向导”窗口中，点击【下一步】：

![](//mccdn.qcloud.com/img56b1b0fae959f.jpg)

输入分区所需磁盘大小，点击【下一步】：

![](//mccdn.qcloud.com/img56b1b1de673fb.jpg)

输入驱动器号，点击【下一步】：

![](//mccdn.qcloud.com/img56b1b2f078870.jpg)

选择文件系统，格式化分区，点击【下一步】：

![](//mccdn.qcloud.com/img56b1b32b1846e.jpg)

完成新建简单卷，点击【完成】：

![](//mccdn.qcloud.com/img56b1b37e6e5f2.jpg)

查看新分区：

![](//mccdn.qcloud.com/img56b1b39fb404d.jpg)

![](//mccdn.qcloud.com/img56b1b3a3e4dd4.jpg)


## 2. Windows2008磁盘分区和格式化
Windows2008进入磁盘管理方法与win2012不同，通过【服务器管理】-【存储】-【磁盘管理】的路径进入磁盘管理。

点击【服务器管理】：
![](//mccdn.qcloud.com/img56b1b5c4cd2ad.jpg)

点击【存储】-【磁盘管理】：

![](//mccdn.qcloud.com/img56b1b6b60f2fd.jpg)

如上图所示，”磁盘1”为未分配的磁盘，这里以对”磁盘1”进行1个分区为例进行说明。

“磁盘1”初始情况下未联机，右键点击”磁盘1”, 在弹出的菜单里点击【联机】：

![](//mccdn.qcloud.com/img56b1b71f7e7d4.jpg)

再次右键点击”磁盘1”, 在弹出的菜单里点击”初始化磁盘”：

![](//mccdn.qcloud.com/img56b1b75941a79.jpg)

选择GPT的初始化方式，点击【确定】按钮：
![](//mccdn.qcloud.com/img56b1b89cb0675.jpg)
注：磁盘大于2TB时一定要选择GPT分区形式。

右键点击“磁盘1”后未分配的区域，在弹出的快捷菜单中选择【新建简单卷】：
![](//mccdn.qcloud.com/img56b1b91f2445b.jpg)

根据向导提示进行操作，输入分区磁盘的大小，点击【下一步】：
![](//mccdn.qcloud.com/img56b1b93ab1e4a.jpg)

选择文件系统，格式化分区，点击【下一步】：
![](//mccdn.qcloud.com/img56b1b95a7f09a.jpg)

完成新建简单卷，点击【完成】按钮：
![](//mccdn.qcloud.com/img56b1b9829f98e.jpg)

显示正在格式化：
![](//mccdn.qcloud.com/img56b1b99be5831.jpg)

在计算机界面可以看到新分区的数据盘：
![](//mccdn.qcloud.com/img56b1b9b953e21.jpg)

>注：请勿将基本硬盘转换到动态硬盘，倘若因此操作造成数据丢失，我们将不承担责任。

## 3. 联机设置
在Windows操作系统下，常需要在磁盘管理中设置联机。为了方便您更好的使用弹性云硬盘，建议您对操作系统执行以下修改：
进入cmd命令行，执行以下命令
```
diskpart
san policy=onlineall
```

![](//mccdn.qcloud.com/static/img/cfb2f1d6d9b99c6786db612f343df525/image.png)
操作后，当此弹性云硬盘重新挂载到Windows云服务器上后，如果弹性云硬盘包含有效的文件系统，用户则可以无需操作直接使用此弹性云硬盘了。