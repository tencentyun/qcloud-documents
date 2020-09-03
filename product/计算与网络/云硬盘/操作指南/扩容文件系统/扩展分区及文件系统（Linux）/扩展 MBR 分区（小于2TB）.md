## 操作场景
当您已完成云硬盘的扩容，可根据实际情况，通过以下两种方式扩展分区及文件系统：
- [将扩容部分的容量划分至原有 MBR 分区](#Add)
- [将扩容部分的容量格式化成独立的 MBR 分区](#New)


## 前提条件
fdisk/e2fsck/resize2fs 自动扩容工具适用于 Linux 操作系统，用于将新扩容的云硬盘空间添加到已有的文件系统中，扩容能够成功必须满足以下条件：
- 已确认扩容分区格式，详情请参考 [如何确认扩展方式](https://cloud.tencent.com/document/product/362/37738)。
- 文件系统是 EXT 或 XFS。
- 当前文件系统不能有错误。
- 扩容后的磁盘大小不超过2TB。
- 文档中使用的扩容工具仅支持 Python 2 版本，不支持 Python 3 版本。



## 操作步骤

<span id="Add"></span>
### 将扩容部分的容量划分至原有 MBR 分区
1. 以 root 用户执行以下命令，卸载分区。
```
umount <挂载点>
```
本文挂载点以 `/data` 为例，则执行：
```
umount /data
```
![](//mccdn.qcloud.com/static/img/c0acc05057941681627a5fd34979d194/image.jpg)
2. 执行以下命令，下载工具。
```
wget -O /tmp/devresize.py https://raw.githubusercontent.com/tencentyun/tencentcloud-cbs-tools/master/devresize/devresize.py
```
3. 执行以下命令，使用扩容工具进行扩容。
```
python /tmp/devresize.py <硬盘路径>
```
本文以硬盘路径以 `/dev/vdb` ，文件系统在 vdb1 上为例，则执行：
```
python /tmp/devresize.py /dev/vdb
```
 - 如下图所示，若输出 `The filesystem on /dev/vdb1 is now XXXXX blocks long.` 则表示扩容成功，请执行 [步骤4](#step4MBR)。
 ![](//mccdn.qcloud.com/static/img/c7617b90578192d64d19f02325f00ffb/image.jpg)
 - 若输出 `[ERROR] - e2fsck failed!!`，请执行以下步骤：
   a. 执行以下命令，修复文件系统所在分区。
```
fsck -a <分区路径>
```
本文以硬盘路径是`/dev/vdb`且文件系统在 vdb1 上为例，则执行：
```
fsck -a /dev/vdb1
```
    b. 修复成功后，再次执行以下命令，使用扩容工具进行扩容。
```
python /tmp/devresize.py /dev/vdb
```
4. <span id="step4MBR"></span>执行以下命令，手动挂载扩容后的分区，本文以挂载点以 `/data` 为例。
```
mount <分区路径> <挂载点>
```
 - 若扩容前已有分区且以分区路径以 `/dev/vdb1` 为例，则执行：
```
mount /dev/vdb1 /data
```
 - 若扩容前没有分区，则执行：
```
mount /dev/vdb /data
```
5. 执行以下命令，查看扩容后的分区容量。
```
df -h
```
若返回类似如下图所示的信息，说明挂载成功，即可查看到数据盘：
![](//mccdn.qcloud.com/static/img/2367f3e70cd0c3c1bef665cc47c1c3bc/image.jpg)
6. 执行以下命令，查看扩容后原分区的数据信息，确认新增加的存储空间是否扩容到文件系统中。
```
ll /data
```

<span id="New"></span>
### 将扩容部分的容量格式化成独立的 MBR 分区
1. 以 root 用户执行以下命令，查看已挂载的数据盘分区信息。
```
df -h
```
已挂载数据盘分区为47GB。如下图所示：
![](//mccdn.qcloud.com/static/img/0a450dfaa9cfc7b2c7fdc04861f0e754/image.png)
2. 执行以下命令，查看数据盘扩容后未分区的信息。
```
fdisk -l
```
数据盘已扩容至107.4GB。如下图所示：
![](//mccdn.qcloud.com/static/img/594671a1215dee3036b7940892438f62/image.png)
3. 执行以下命令，解挂所有已挂载的分区。
```
umount <挂载点>
```
本文以挂载点以 `/data` 为例，则执行：
```
umount /data
```
>? 请将云硬盘上所有分区都解挂后，再执行 [步骤4](#Step4MBR)。
>
4. <span id="Step4MBR"></span>执行以下命令，新建一个新分区。
```
fdisk <硬盘路径>
```
本文以磁盘路径以 `/dev/xvdc` 为例，则执行：
```
fdisk /dev/xvdc
```
按照界面的提示，依次执行以下命令：
 1. 输入 “p”：查看现有分区信息，本文已有分区 `/dev/xvdc1`。
 2. 输入 “n”：新建分区。
 3. 输入 “p”：新建主分区。
 4. 输入 “2”：新建第2个主分区。
 5. 按2次 “**Enter**”：分区大小使用默认配置。
 6. 输入 “w”：保存分区表，开始分区。如下图所示：
![](//mccdn.qcloud.com/static/img/8c35d6f4dfb367e74edc27ce6822c317/image.png)
>? 本文以创建一个分区为例，您可以根据实际需求创建多个分区。
5. 执行以下命令，查看新分区。
```
fdisk -l
```
新的分区 xvdc2 已经创建完成。如下图所示：
![](//mccdn.qcloud.com/static/img/e04e924d62317bc2c605c8abaac394f5/image.png)
6. 执行以下命令，格式化新分区并创建文件系统，您可以自行选择文件系统的格式，例如 EXT2、EXT3 等。
```
mkfs.<fstype> <分区路径> 
```
本文以 EXT3 为例，则执行：
```
mkfs.ext3 /dev/xvdc2
```
已成功创建 EXT3 文件系统，如下图所示：
![](//mccdn.qcloud.com/static/img/074e23eaa580495f96fb532b688d2d68/image.png)
7. 执行以下命令，创建新的挂载点。
```
mkdir <新挂载点>
```
本文以新挂载点以 `/data1` 为例，则执行：
```
mkdir /data1
```
8. 执行以下命令，手动挂载新分区。
```
mount <新分区路径> <新挂载点>
```
本文以新分区路径 `/dev/xvdc2`，新挂载点 `/data1` 为例，则执行：
```
mount /dev/xvdc2 /data1
```
9. 执行以下命令，查看新分区信息。
```
df -h
```
返回如下图所示信息则说明挂载成功，即可以查看到数据盘：
![](//mccdn.qcloud.com/static/img/7b749a4bb6e7c8267c9354e1590c35d4/image.png)
>?若您希望云服务器在重启或开机时能自动挂载数据盘，则需要执行 [步骤10](#AddNewPartINFOstep10) 和 [步骤11](#AddNewPartINFOstep11) 添加新分区信息至`/etc/fstab`中。
10. <span id="AddNewPartINFOstep10"></span>执行以下命令，添加信息。
```
echo '/dev/xvdc2 /data1 ext3 defaults 0 0' >> /etc/fstab
```
<span id="AddNewPartINFOstep11"></span>
11. 执行以下命令，查看信息。
```
cat /etc/fstab
```
若返回如下图所示信息，则表示添加分区信息成功。
![](//mccdn.qcloud.com/static/img/f0b5c14bf08fd3629ddf6d9b1ae01ffc/image.png)
