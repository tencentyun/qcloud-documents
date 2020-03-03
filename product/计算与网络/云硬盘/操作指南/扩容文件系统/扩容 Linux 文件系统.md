## 操作场景
云硬盘是云上可扩展的存储设备，您可以在创建云硬盘后随时扩展其大小，以增加存储空间，同时不失去云硬盘上原有的数据。
[扩容云硬盘](https://cloud.tencent.com/document/product/362/5747) 完成后，需要将扩容部分的容量划分至已有分区内，或者将扩容部分的容量格式化成一个独立的新分区。



## 前提条件
>!扩容文件系统操作不慎可能影响已有数据，因此强烈建议您在操作前手动 [创建快照](https://cloud.tencent.com/document/product/362/5755) 备份数据。
>
- 已 [扩容云硬盘](https://cloud.tencent.com/document/product/362/5747)  空间。
- 该云硬盘已 [挂载](https://cloud.tencent.com/document/product/362/5745) 到 Linux 云服务器并已创建文件系统。
- 已 [登录](https://cloud.tencent.com/document/product/213/5436) 待扩展分区及文件系统的 Linux 云服务器。

## 操作步骤
### 确认扩展方式
<span id="fdisk"></span>
1. 以 root 用户执行以下命令，查询云硬盘使用的分区形式。
```
fdisk -l
```
 - 若结果展示的设备无分区（如仅展示 /dev/vdb），请您参考 [扩容文件系统](#ExpandTheFileSystem)。
 - 若结果如下两图所示（根据操作系统不同略有不同），则说明使用 GPT 分区形式。
![](https://main.qcloudimg.com/raw/5ff70adb58a223d32d334470c5b29e0e.png)
![](https://main.qcloudimg.com/raw/ce19715fc8494a9735b714d86f0cccfa.png)
 - 若结果如下图所示（根据操作系统不同略有不同），则说明使用 MBR 分区形式。
 >! MBR 分区形式支持的磁盘最大容量为2TB。如果您的硬盘分区为 MBR 格式，且需要扩容到超过 2TB 时，建议您重新创建并挂载一块数据盘，使用 GPT 分区方式后将数据拷贝至新盘上。对于 Linux 操作系统而言，当磁盘分区形式选用 GPT 时，fdisk 分区工具将无法使用，需要采用 parted 工具。
 >
![](https://main.qcloudimg.com/raw/0e336cd3354c098cf5e70d0672e6f625.png)
2. 根据 [步骤1](#fdisk) 查询到的云硬盘分区形式，选择对应的操作指引。
<table>
     <tr>
         <th nowrap="nowrap">分区形式</th>  
         <th>操作指引</th>  
         <th>说明</th>  
     </tr>
		 	 <tr>      
         <td>-</td>   
	     <td nowrap="nowrap"><a href="#ExpandTheFileSystem">扩容文件系统</a></td>
	     <td>适用于没有创建分区、直接在裸设备上创建了文件系统的场景。</td>
     </tr>
	 <tr>      
         <td rowspan="2">GPT</td>   
	     <td nowrap="nowrap"><a href="#AddToTheExistingGPTPart">将扩容部分的容量划分至原有分区（GPT）</a></td>
	     <td>同样适用于未分区直接格式化的场景。</td>
     </tr> 
	 <tr>
         <td><a href="#CreateANewGPTPart">将扩容部分的容量格式化成独立的新分区（GPT）</a></td> 
	     <td>可保持原有分区不变。</td>
     </tr> 
	 <tr>
         <td rowspan="2">MBR</td>   
	     <td><a href="#AddToTheExistingMBRPart">将扩容部分的容量划分至原有分区（MBR）</a></td> 
	     <td>同样适用于未分区直接格式化的场景。</td>
     </tr> 
	 <tr>
         <td><a href="#CreateANewMBRPart">将扩容部分的容量格式化成独立的新分区（MBR）</a></td> 
	     <td>可保持原有分区不变。</td>
     </tr> 
</table>

<span id="ExpandTheFileSystem"></span>
### 扩容文件系统

1. 根据文件系统的类型，执行不同的命令进行扩容。
 - 对于 EXT 文件系统，请执行 `resize2fs` 命令扩容文件系统。
 - 对于 XFS 文件系统，请执行`xfs_growfs`命令扩容文件系统。

 以 `/dev/vdb` 为例， EXT 文件系统执行以下命令：
```
resize2fs /dev/vdb
```
以 `/dev/vdb` 为例， XFS 文件系统执行以下命令：
```
xfs_growfs /dev/vdb
```
2. 执行以下命令，查看新分区。
```
df -h
```

<span id="AddToTheExistingGPTPart"></span>
### 将扩容部分的容量划分至原有分区（GPT）
1. 以 root 用户执行以下命令，确认云硬盘的容量变化。
 ```
parted <磁盘路径> print
```
本文以磁盘路径是 `/dev/vdb`为例，则执行：
```
parted /dev/vdb print
```
若在过程中提示如下图所示信息，请输入`Fix`。
![](//mccdn.qcloud.com/static/img/cf51cda9a12085f76949ab0d5dd0fbfc/image.png)
如下图所示，扩容后的云硬盘大小为107GB，已有分区的大小为10.7GB。
![](//mccdn.qcloud.com/static/img/01a0a7a8fdfe6f05f2739f0326a74ef9/image.png)

2. 执行以下命令，确认该云硬盘是否还有分区已挂载。
```
mount | grep '<磁盘路径>' 
```
本文以磁盘路径是`/dev/vdb`为例，则执行：
```
mount | grep '/dev/vdb'
```
如下图所示，云硬盘上有一个分区（vdb1）挂载在`/data`上。
![](//mccdn.qcloud.com/static/img/edc5bbd6834e1dd929ce0eb00acd53ca/image.png)
3. 执行以下命令，解挂数据盘。
```
umount <挂载点>
```
本文以挂载点是`/data`为例，则执行：
```
umount /data
```
>? 请将云硬盘上所有分区的文件系统都解挂，再执行 [步骤4](#step4) 操作。可重复执行以下命令，确认该硬盘上所有分区的文件系统都已解挂。
```
mount | grep '/dev/vdb'
```
云硬盘上所有的分区文件系统均已解挂。如下图所示：
![](https://main.qcloudimg.com/raw/9242efdec1aab382ae74f975ca68d68a.png)
4. <span id="step4"></span>执行以下命令，进入 parted 分区工具。
```
parted '<磁盘路径>'
```
本文以磁盘路径是`/dev/vdb`为例，则执行：
```
parted '/dev/vdb'
```
5. 执行以下命令，将显示和操纵单位变成 sector（默认为GB）。
```
unit s
```
6. 执行以下命令，查看分区信息，并记录已有分区的 Start 值。
>! 删除分区并新建后，Start 值必须保持不变，否则将会引起数据丢失。
>
```
print
```
本文中 Start 值为 `2048s`。如下图所示：
![](//mccdn.qcloud.com/static/img/67ba54c1d9d63c307d4b8a157b70c722/image.png)

7. 执行以下命令，删除原有分区。
```
rm <分区 Number>
```
例如，由上图可知云硬盘上有一个分区，Number 为“1”，则执行：
```
 rm 1
```
回显信息如下图所示。
![](//mccdn.qcloud.com/static/img/3384eeada87ce75695e0e55125109eff/image.png)
8. 执行以下命令，新建一个主分区。
```
mkpart primary <原分区起始扇区> 100%
```
其中，100%表示此分区到磁盘的最末尾。
例如，主分区从第2048个扇区开始（必须与删除之前的分区一致，即 Start 值为2048s），则执行：
```
mkpart primary 2048s 100%
```
如果出现如下图所示的状态，请输入`Ignore`。
![](//mccdn.qcloud.com/static/img/c45966e20dc856817c65fd6b81155e4a/image.png)
6. 执行以下命令，查看新分区是否已创建成功。
```
print
```
返回结果如下图所示，即表示新分区已创建成功。
![](//mccdn.qcloud.com/static/img/cb1af5adaf6c89d066077c43fd428a38/image.png)
7. 执行以下命令，退出 parted 工具。
```
quit
```
11. 执行以下命令，检查扩容后的分区。
```
e2fsck -f <分区路径>
```
本文以新建分区是1（即分区路径是`/dev/vdb1`）为例，则执行：
```
e2fsck -f /dev/vdb1
```
返回如下图所示结果。
![](//mccdn.qcloud.com/static/img/307f7a0c98eea05ca1d4560fe4e96f57/image.png)
12. 执行以下命令，对新分区上 EXT 文件系统进行扩容操作。
```
resize2fs <分区路径>
```
本文以分区路径是`/dev/vdb1`为例，则执行：
```
resize2fs /dev/vdb1
```
扩容成功则如下图所示：
![](//mccdn.qcloud.com/static/img/57d66da9b5020324703498dbef0b12f9/image.png)
13. 执行以下命令，对新分区上 XFS 文件系统进行扩容操作。
```
xfs_growfs <分区路径>
```
本文以分区路径是`/dev/vdb1`为例，则执行：
```
xfs_growfs /dev/vdb1
```
14. 执行以下命令，手动挂载新分区。
```
mount <分区路径> <挂载点>
```
本文以分区路径是`/dev/vdb1`，挂载点是`/data`为例，则执行：
```
mount /dev/vdb1 /data
```
15. 执行以下命令，查看新分区。
```
df -h
```
返回如下图信息说明挂载成功，即可以查看到数据盘。
![](//mccdn.qcloud.com/static/img/a2bd04c79e8383745689e19033a0daaa/image.png)

<span id="CreateANewGPTPart"></span>
### 将扩容部分的容量格式化成独立的新分区（GPT）

1. 以 root 用户执行以下命令， 确认云硬盘的容量变化。
 ```
parted <磁盘路径> print
```
本文以磁盘路径是`/dev/vdb`为例，则执行：
```
parted /dev/vdb print
```
若在过程中提示如下图所示信息，请输入 `Fix`。
![](//mccdn.qcloud.com/static/img/cf51cda9a12085f76949ab0d5dd0fbfc/image.png)
如下图所示，扩容后的云硬盘大小为107GB，已有分区的大小为10.7GB。
![](//mccdn.qcloud.com/static/img/01a0a7a8fdfe6f05f2739f0326a74ef9/image.png)
2. 执行以下命令，确认该云硬盘是否还有分区已挂载。
```
mount | grep '<磁盘路径>' 
```
本文以磁盘路径是`/dev/vdb`为例，则执行：
```
mount | grep '/dev/vdb'
```
如下图所示，云硬盘上有一个分区（vdb1）挂载在`/data`上。
![](//mccdn.qcloud.com/static/img/edc5bbd6834e1dd929ce0eb00acd53ca/image.png)
3. 执行以下命令，解挂数据盘。
```
umount <挂载点>
```
本文以挂载点是`/data`为例，则执行：
```
umount /data
```
>? 请将云硬盘上所有分区的文件系统都解挂，再执行 [步骤4](#Step4) 操作。可重复执行以下命令，确认该硬盘上所有分区的文件系统都已解挂。
```
mount | grep '/dev/vdb'
```
云硬盘上所有的分区文件系统均已解挂。如下图所示：
![](https://main.qcloudimg.com/raw/d1a9a33f0d4e3725aed677f2403c91ae.png)
<span id="Step4"></span>
4. 执行以下命令，进入 parted 分区工具。
```
parted '<磁盘路径>'
```
本文以磁盘路径是`/dev/vdb`为例，则执行：
```
parted '/dev/vdb'
```
5. 执行以下命令，查看分区信息，并记录已有分区的 End 值，以此值作为下一个分区的起始偏移值。
```
print
```
![](//mccdn.qcloud.com/static/img/788ce125bba952f204ed6ee36dfb644d/image.png)
6. 执行以下命令，新建一个主分区。此分区将从已有分区的末尾开始，覆盖硬盘所有的新增空间。
```
mkpart primary start end
```
本文以 End 值是10.7GB为例，执行以下命令：
```
mkpart primary 10.7GB 100%
```
7. 执行以下命令，查看新分区是否已创建成功。
```
print
```
![](//mccdn.qcloud.com/static/img/fc54fd4c05102ee91c648526d77d1b42/image.png)
8.  执行以下命令，退出 parted 工具。
```
quit
```
9. 执行以下命令，格式化新建的分区。
```
mkfs.<fstype> <分区路径> 
```
您可以自行选择文件系统的格式，例如 EXT2、EXT3 等。
本文以文件系统是 EXT3 为例，则执行： 
```
mkfs.ext3 /dev/vdb2
```

<span id="AddToTheExistingMBRPart"></span>
### 将扩容部分的容量划分至原有分区（MBR）
fdisk/e2fsck/resize2fs 自动扩容工具适用于 Linux 操作系统，用于将新扩容的云硬盘空间添加到已有的文件系统中，扩容能够成功必须满足以下四个条件：
- 文件系统是 EXT2/EXT3/EXT4/XFS。
- 当前文件系统不能有错误。
- 扩容后的磁盘大小不超过2TB。
- 当前工具仅支持 Python 2 版本，不支持 Python 3 版本。


1. 以 root 用户执行以下命令，卸载分区。
```
umount <挂载点>
```
本文以挂载点是`/data`为例，则执行：
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
本文以硬盘路径是`/dev/vdb`且文件系统在 vdb1 上为例，则执行：
```
python /tmp/devresize.py /dev/vdb
```
![](//mccdn.qcloud.com/static/img/c7617b90578192d64d19f02325f00ffb/image.jpg)
 - 若输出 “The filesystem on /dev/vdb1 is now XXXXX blocks long.” 则表示扩容成功，请执行 [步骤4](#step4MBR)。
 - 若输出的是 “[ERROR] - e2fsck failed!!”，请执行以下步骤：
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
<span id="step4MBR"></span>
4. 执行以下命令，手动挂载扩容后的分区。
```
mount <分区路径> <挂载点>
```
本文以挂载点是`/data`为例。
 - 若扩容前已有分区且以分区路径是`/dev/vdb1`为例，则执行：
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
若返回类似如下图所示的信息，说明挂载成功，即可以查看到数据盘：
![](//mccdn.qcloud.com/static/img/2367f3e70cd0c3c1bef665cc47c1c3bc/image.jpg)
6. 执行以下命令，查看扩容后原分区的数据信息，确认新增加的存储空间是否扩容到文件系统中。
```
ll /data
```

<span id="CreateANewMBRPart"></span>
### 将扩容部分的容量格式化成独立的新分区（MBR）
1. 以 root 用户执行以下命令，查看已挂载的数据盘分区信息。
```
df -h
```
![](//mccdn.qcloud.com/static/img/0a450dfaa9cfc7b2c7fdc04861f0e754/image.png)
2. 执行以下命令，查看数据盘扩容后未分区的信息。
```
fdisk -l
```
![](//mccdn.qcloud.com/static/img/594671a1215dee3036b7940892438f62/image.png)
3. 执行以下命令，解挂所有已挂载的分区。
```
umount <挂载点>
```
本文以挂载点是`/data`为例，则执行：
```
umount /data
```
>? 请将云硬盘上所有分区的文件系统都解挂，再执行 [步骤4](#Step4MBR) 操作。可执行以下命令，确认该硬盘上所有分区的文件系统都已解挂。
```
mount | grep '<磁盘路径>'
```
如返回结果为空，则云硬盘上所有的分区文件系统均已解挂。
4. <span id="Step4MBR"></span>执行以下命令，新建一个新分区。
```
fdisk <硬盘路径>
```
本文以磁盘路径是`/dev/xvdc`为例，则执行：
```
fdisk /dev/xvdc
```
按照界面的提示，依次输入“p”（查看现有分区信息）、“n”（新建分区）、“p”（新建主分区）、“2”（新建第2个主分区），两次回车（使用默认配置），输入 “w”（保存分区表），开始分区。如下图所示：
![](//mccdn.qcloud.com/static/img/8c35d6f4dfb367e74edc27ce6822c317/image.png)
>? 本文以创建一个分区为例，您也可以根据实际需求创建多个分区。
5. 执行以下命令，查看新分区。
```
fdisk -l
```
如下图所示，表示新的分区 xvdc2 已经创建完成。
![](//mccdn.qcloud.com/static/img/e04e924d62317bc2c605c8abaac394f5/image.png)
6. 执行以下命令，格式化新分区并创建文件系统。
```
mkfs.<fstype> <分区路径> 
```
您可以自行选择文件系统的格式，例如 EXT2、EXT3 等。
本文以文件系统是 EXT3 为例，则执行：
```
mkfs.ext3 /dev/xvdc2
```
![](//mccdn.qcloud.com/static/img/074e23eaa580495f96fb532b688d2d68/image.png)
7. 执行以下命令，创建新的挂载点。
```
mkdir <新挂载点>
```
本文以新挂载点是`/data1`为例，则执行：
```
mkdir /data1
```
8. 执行以下命令，手动挂载新分区。
```
mount <新分区路径> <新挂载点>
```
本文以新分区路径是`/dev/xvdc2`，新挂载点是`/data1`为例，则执行：
```
mount /dev/xvdc2 /data1
```
9. 执行以下命令，查看新分区信息。
```
df -h
```
返回如下图所示信息则说明挂载成功，即可以查看到数据盘。
![](//mccdn.qcloud.com/static/img/7b749a4bb6e7c8267c9354e1590c35d4/image.png)
>?若您希望云服务器在重启或开机时能自动挂载数据盘，则需要执行 [步骤10](#AddNewPartINFOstep10) 和 [步骤11](#AddNewPartINFOstep11) 添加新分区信息至`/etc/fstab`中。
10. <span id="AddNewPartINFOstep10"></span>执行以下命令，添加信息。
```
echo '/dev/xvdc2 /data1 ext3 defaults 0 0' >> /etc/fstab
```
11. <span id="AddNewPartINFOstep11"></span>执行以下命令，查看信息。
```
cat /etc/fstab
```
若返回如下图所示信息，则表示添加分区信息成功。
![](//mccdn.qcloud.com/static/img/f0b5c14bf08fd3629ddf6d9b1ae01ffc/image.png)

## 相关操作
[扩展分区及文件系统（Windows）](https://cloud.tencent.com/document/product/362/6737)

## 常见问题
如果您在使用云硬盘过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
-  [使用相关问题](https://cloud.tencent.com/document/product/362/17819)
-  [功能相关问题](https://cloud.tencent.com/document/product/362/17818)
