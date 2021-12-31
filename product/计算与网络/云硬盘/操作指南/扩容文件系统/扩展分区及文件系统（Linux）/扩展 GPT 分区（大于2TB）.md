## 操作场景
当您的云硬盘在已有 GPT 分区并已创建文件系统的情况下，可根据实际情况，通过以下两种方式扩展分区及文件系统：
- [将扩容部分的容量划分至原有 GPT 分区](#Add)
- [将扩容部分的容量格式化成独立的 GPT 分区](#New)



## 前提条件
e2fsck/resize2fs 自动扩容工具适用于 Linux 操作系统，用于将新扩容的云硬盘空间添加到已有的文件系统中，扩容能够成功必须满足以下条件：
- 已确认扩容分区格式，详情请参考 [确认扩展方式](https://cloud.tencent.com/document/product/362/53363)。
- 文件系统是 EXT 或 XFS。
- 当前文件系统不能有错误。


## 操作步骤

[](id:Add)
### 将扩容部分的容量划分至原有 GPT 分区
1. 以 root 用户执行以下命令，确认云硬盘的容量变化。
```
parted <磁盘路径> print
```
本文以磁盘路径以 `/dev/vdc` 为例，则执行：
```
parted /dev/vdc print
```
若在过程中提示如下图所示信息，请输入 `Fix`。如下图所示：
![](https://main.qcloudimg.com/raw/bdc9f2fcb281e24ec5799e73c08535eb.png)
扩容后的云硬盘大小为2040GB，已有分区的大小为10.7GB。如下图所示：
![](https://main.qcloudimg.com/raw/40a1141f65ba7ac15b8dac4b94e0d6a5.png)
2. 执行以下命令，查看该云硬盘是否有已挂载分区。
```
mount | grep '<磁盘路径>' 
```
本文以磁盘路径以 `/dev/vdc` 为例，则执行：
```
mount | grep '/dev/vdc'
```
 - 返回结果如下，则说明云硬盘上有一个分区（vdc1）挂载在 `/data` 上。
![](https://main.qcloudimg.com/raw/61ae197d19c522f6ebd1e9c7bf4b4d88.png)
执行以下命令，将云硬盘上的**所有分区**都解挂。
```
umount <挂载点>
```
本文以挂载点以 `/data` 为例，则执行：
```
umount /data
```
 - 返回结果如下所示，则无已挂载分区，请执行下一步。
![](https://main.qcloudimg.com/raw/4a6d070830fd0629a336836fd6b4c1fd.png)
3. 执行以下命令，进入 parted 分区工具。
```
parted '<磁盘路径>'
```
本文以磁盘路径以 `/dev/vdc` 为例，则执行：
```
parted '/dev/vdc'
```
4. 执行以下命令，将显示和操纵单位变成 sector（默认为GB）。
```
unit s
```
5. [](id:step5)执行以下命令，查看分区信息，并记录已有分区的 Start 值。
```
print
```
>! 请务必记录 Start 值。删除分区并新建后，Start 值必须保持不变，否则将会引起数据丢失。
>
![](https://main.qcloudimg.com/raw/a4b3b6710d2d03549c26b8efd7d844db.png)
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
![](https://main.qcloudimg.com/raw/fbac9760d06da56e3f3be3a61309cc10.png)
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
![](https://main.qcloudimg.com/raw/823646dcfd0e42ece63a37338e0d4e16.png)
10. 执行以下命令，退出 parted 工具。
```
quit
```
11. 执行以下命令，检查扩容后的分区。
```
e2fsck -f <分区路径>
```
本文以新建分区是1（即分区路径是`/dev/vdc1`）为例，则执行：
```
e2fsck -f /dev/vdc1
```
返回如下图所示结果：
![](https://main.qcloudimg.com/raw/12c917c78829014cd784e3f184c01eed.png)
12. 请根据您的实际情况，对新建分区上的文件系统进行扩容操作。
 - **EXT 文件系统**执行以下命令：
```
resize2fs <分区路径>
```
本文以分区路径以 `/dev/vdc1` 为例，则执行：
```
resize2fs /dev/vdc1
```
扩容成功则如下图所示：
![](https://main.qcloudimg.com/raw/7daebff27ce10c66b63c2b35c9712418.png)
 -  **XFS 文件系统**执行以下命令：
```
xfs_growfs <分区路径>
```
本文以分区路径是`/dev/vdc1`为例，则执行：
```
xfs_growfs /dev/vdc1
```
13. 执行以下命令，手动挂载新分区。
```
mount <分区路径> <挂载点>
```
本文以分区路径以`/dev/vdc1`，挂载点 `/data` 为例，则执行：
```
mount /dev/vdc1 /data
```
14. 执行以下命令，查看新分区。
```
df -h
```
返回如下图信息说明挂载成功，即可以查看到数据盘。
![](https://main.qcloudimg.com/raw/476829f5a9cb6aef62f3cace31cb2586.png)

[](id:New)
### 将扩容部分的容量格式化成独立的 GPT 分区
1. 以 root 用户执行以下命令， 确认云硬盘的容量变化。
```
parted <磁盘路径> print
```
本文以磁盘路径是`/dev/vdc`为例，则执行：
```
parted /dev/vdc print
```
若在过程中提示如下图所示信息，请输入 `Fix`。
![](https://main.qcloudimg.com/raw/c69cd8b3741675f1a96715c4679ce6e6.png)
扩容后的云硬盘大小为2147GB，已有分区的大小为2040GB。如下图所示：
![](https://main.qcloudimg.com/raw/8d8e72b1a5716443673453f67c1d798d.png)
2. 执行以下命令，查看该云硬盘是否有已挂载分区。
```
mount | grep '<磁盘路径>' 
```
本文以磁盘路径以 `/dev/vdc` 为例，则执行：
```
mount | grep '/dev/vdc'
```
 - 返回结果如下，则说明云硬盘上有一个分区（vdc1）挂载在 `/data` 上。
![](https://main.qcloudimg.com/raw/1703f6594a1fbff86dd1d1dfb2ab124d.png)
执行以下命令，将云硬盘上的**所有分区**都解挂。
```
umount <挂载点>
```
本文以挂载点以 `/data` 为例，则执行：
```
umount /data
```
 - 返回结果如下所示，则无已挂载分区，请执行下一步。
![](https://main.qcloudimg.com/raw/d10d74c1fff5e8ffdb306d5acb664ae1.png)
3. 执行以下命令，进入 parted 分区工具。
```
parted '<磁盘路径>'
```
本文以磁盘路径以 `/dev/vdc` 为例，则执行：
```
parted '/dev/vdc'
```
4. [](id:Step4)执行以下命令，查看分区信息，并记录已有分区的 End 值，以此值作为下一个分区的起始偏移值。
```
print
```
![](https://main.qcloudimg.com/raw/7f11b89e481035897d525fa8a93cb7e7.png)
5. 执行以下命令，新建一个主分区。此分区将从已有分区的末尾开始，覆盖硬盘所有的新增空间。
```
mkpart primary start end
```
由 [步骤4](#Step4) 可得 End 值，请您根据实际情况填写。本文中 End 值为2040GB， 则执行：
```
mkpart primary 2040GB 100%
```
6. 执行以下命令，查看新分区是否已创建成功。
```
print
```
输出结果如下，则已成功新建分区：
![](https://main.qcloudimg.com/raw/5e1418caaddf22932ac624ff906cf302.png)
7.  执行以下命令，退出 parted 工具。
```
quit
```
8. 执行以下命令，格式化新建的分区。您可以自行选择文件系统的格式，例如 EXT2、EXT3 等。
```
mkfs.<fstype> <分区路径> 
```
本文以 EXT4 为例，则执行： 
```
mkfs.ext4 /dev/vdc2
```
9. 执行以下命令，手动挂载新分区。
```
mount <分区路径> <挂载点>
```
本文以分区路径以 `/dev/vdc2`，挂载点 `/data` 为例，则执行：
```
mount /dev/vdc2 /data
```
10. 执行以下命令，查看新分区。
```
df -h
```
返回如下图信息说明挂载成功，即可以查看到数据盘。
![](https://main.qcloudimg.com/raw/cd9d36d49388882f0cb898c13d565bb0.png)

## 相关文档
[扩展分区及文件系统（Windows）](https://cloud.tencent.com/document/product/362/6737)

## 常见问题
如果您在使用云硬盘过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- [使用相关问题](https://cloud.tencent.com/document/product/362/17819)
- [功能相关问题](https://cloud.tencent.com/document/product/362/17818)


