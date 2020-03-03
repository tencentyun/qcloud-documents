## 操作场景
当您已完成云硬盘的扩容，可根据实际情况，通过以下两种方式扩展分区及文件系统：
- [将扩容部分的容量划分至原有 GPT 分区](#Add)
- [将扩容部分的容量格式化成独立的 GPT 分区](#New)



## 前提条件
e2fsck/resize2fs 自动扩容工具适用于 Linux 操作系统，用于将新扩容的云硬盘空间添加到已有的文件系统中，扩容能够成功必须满足以下条件：
- 已确认扩容分区格式，详情请参考 [如何确认扩展方式](https://cloud.tencent.com/document/product/362/37738)。
- 文件系统是 EXT 或 XFS。
- 当前文件系统不能有错误。


## 操作步骤

<span id="Add"></span>
### 将扩容部分的容量划分至原有 GPT 分区
1. 以 root 用户执行以下命令，确认云硬盘的容量变化。
```
parted <磁盘路径> print
```
本文以磁盘路径以 `/dev/vdb` 为例，则执行：
```
parted /dev/vdb print
```
若在过程中提示如下图所示信息，请输入 `Fix`。
![](https://main.qcloudimg.com/raw/ec2ec164e146e46c2a4d11489dceecfa.png)
扩容后的云硬盘大小为2169GB，已有分区的大小为10.7GB。如下图所示：
![](https://main.qcloudimg.com/raw/d902d173106fdb9b5ff44c494ba8147a.png)
2. 执行以下命令，查看该云硬盘是否有已挂载分区。
```
mount | grep '<磁盘路径>' 
```
本文以磁盘路径以 `/dev/vdb` 为例，则执行：
```
mount | grep '/dev/vdb'
```
 - 返回结果如下，则说明云硬盘上有一个分区（vdb1）挂载在 `/data` 上。
![](https://main.qcloudimg.com/raw/3b786b5ccc36f2819b2659cf47afb422.png)
执行以下命令，将云硬盘上的**所有分区**都解挂。
```
umount <挂载点>
```
本文以挂载点以 `/data` 为例，则执行：
```
umount /data
```
 - 返回结果如下所示，则无已挂载分区，请执行下一步。
 ![](https://main.qcloudimg.com/raw/c51d1e9215493837b4b0968aecb94f5c.png)
3. 执行以下命令，进入 parted 分区工具。
```
parted '<磁盘路径>'
```
本文以磁盘路径以 `/dev/vdb` 为例，则执行：
```
parted '/dev/vdb'
```
4. 执行以下命令，将显示和操纵单位变成 sector（默认为GB）。
```
unit s
```
5. <span id="step5"></span>执行以下命令，查看分区信息，并记录已有分区的 Start 值。
```
print
```
>! 请务必记录 Start 值。删除分区并新建后，Start 值必须保持不变，否则将会引起数据丢失。
>
![](https://main.qcloudimg.com/raw/47e0e8ae7f2c085cd4ff5d0d9cb97a69.png)
6. 执行以下命令，删除原有分区。
```
rm <分区 Number>
```
由上图可知云硬盘上有一个分区，Number 为“1”，则执行：
```
 rm 1
```
7. 执行以下命令，确定分区已删除，回显信息如下图所示。
```
print
```
![](https://main.qcloudimg.com/raw/22477795f49dc195fa2447e821c5bfa3.png)
>!如果误删分区，可立即执行 `rescue` 命令，并根据提示输入 Start、End 值确认恢复分区。
>
8. 执行以下命令，新建一个主分区。
```
mkpart primary <原分区起始扇区> 100%
```
100%表示此分区到磁盘的最末尾，且由 [步骤5](#step5) 可得 Start 值，请根据您的实际情况填写。本文中原分区删除前扇区由2048s开始，则 Start 值为2048，执行：
```
mkpart primary 2048s 100%
```
如果出现如下图所示的状态，请输入`Ignore`。
![](//mccdn.qcloud.com/static/img/c45966e20dc856817c65fd6b81155e4a/image.png)
9. 执行以下命令，查看新分区是否已创建成功。
```
print
```
返回结果如下图所示，即表示新分区已创建成功。
![](https://main.qcloudimg.com/raw/436896f6b8c0c4fffa52162c10d4abf2.png)
10. 执行以下命令，退出 parted 工具。
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
12. 请根据您的实际情况，对新建分区上的文件系统进行扩容操作。
 - **EXT 文件系统**执行以下命令：
```
resize2fs <分区路径>
```
本文以分区路径以 `/dev/vdb1` 为例，则执行：
```
resize2fs /dev/vdb1
```
扩容成功则如下图所示：
![](//mccdn.qcloud.com/static/img/57d66da9b5020324703498dbef0b12f9/image.png)
 -  **XFS 文件系统**执行以下命令：
```
xfs_growfs <分区路径>
```
本文以分区路径是`/dev/vdb1`为例，则执行：
```
xfs_growfs /dev/vdb1
```
13. 执行以下命令，手动挂载新分区。
```
mount <分区路径> <挂载点>
```
本文以分区路径以`/dev/vdb1`，挂载点 `/data` 为例，则执行：
```
mount /dev/vdb1 /data
```
14. 执行以下命令，查看新分区。
```
df -h
```
返回如下图信息说明挂载成功，即可以查看到数据盘。
![](https://main.qcloudimg.com/raw/b99b58b68ae1d156325392767cdc5c72.png)

<span id="New"></span>
### 将扩容部分的容量格式化成独立的 GPT 分区
1. 以 root 用户执行以下命令， 确认云硬盘的容量变化。
```
parted <磁盘路径> print
```
本文以磁盘路径是`/dev/vdb`为例，则执行：
```
parted /dev/vdb print
```
若在过程中提示如下图所示信息，请输入 `Fix`。
![](https://main.qcloudimg.com/raw/69791b332c9237f5b4b4b392a4f0001f.png)
扩容后的云硬盘大小为2169GB，已有分区的大小为10.7GB。如下图所示：
![](https://main.qcloudimg.com/raw/26ddf5d567cb6d28c87ed40222ffede6.png)
2. 执行以下命令，查看该云硬盘是否有已挂载分区。
```
mount | grep '<磁盘路径>' 
```
本文以磁盘路径以 `/dev/vdb` 为例，则执行：
```
mount | grep '/dev/vdb'
```
 - 返回结果如下，则说明云硬盘上有一个分区（vdb1）挂载在 `/data` 上。
![](https://main.qcloudimg.com/raw/3b786b5ccc36f2819b2659cf47afb422.png)
执行以下命令，将云硬盘上的**所有分区**都解挂。
```
umount <挂载点>
```
本文以挂载点以 `/data` 为例，则执行：
```
umount /data
```
 - 返回结果如下所示，则无已挂载分区，请执行下一步。
 ![](https://main.qcloudimg.com/raw/c51d1e9215493837b4b0968aecb94f5c.png)
3. 执行以下命令，进入 parted 分区工具。
```
parted '<磁盘路径>'
```
本文以磁盘路径以 `/dev/vdb` 为例，则执行：
```
parted '/dev/vdb'
```
4. <span id="Step4"></span>执行以下命令，查看分区信息，并记录已有分区的 End 值，以此值作为下一个分区的起始偏移值。
```
print
```
![](https://main.qcloudimg.com/raw/89e8e0e17f6fe713f5160267ee32348d.png)
5. 执行以下命令，新建一个主分区。此分区将从已有分区的末尾开始，覆盖硬盘所有的新增空间。
```
mkpart primary start end
```
由 [步骤4](#Step4) 可得 End 值，请您根据实际情况填写。本文中 End 值为10.7GB， 则执行：
```
mkpart primary 10.7GB 100%
```
6. 执行以下命令，查看新分区是否已创建成功。
```
print
```
输出结果如下，则已成功新建分区：
![](https://main.qcloudimg.com/raw/ccf3226b3efa667f8d098bc9d809e6a5.png)
7.  执行以下命令，退出 parted 工具。
```
quit
```
8. 执行以下命令，格式化新建的分区。您可以自行选择文件系统的格式，例如 EXT2、EXT3 等。
```
mkfs.<fstype> <分区路径> 
```
本文以 EXT3 为例，则执行： 
```
mkfs.ext3 /dev/vdb2
```
9. 执行以下命令，手动挂载新分区。
```
mount <分区路径> <挂载点>
```
本文以分区路径以 `/dev/vdb2`，挂载点 `/data` 为例，则执行：
```
mount /dev/vdb2 /data
```
10. 执行以下命令，查看新分区。
```
df -h
```
返回如下图信息说明挂载成功，即可以查看到数据盘。
![](https://main.qcloudimg.com/raw/52dc0e48943bb4d8635f1529c03bcdba.png)
