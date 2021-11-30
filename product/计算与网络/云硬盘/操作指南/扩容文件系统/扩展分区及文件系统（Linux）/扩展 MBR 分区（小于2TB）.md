## 操作场景
当您的云硬盘在已有 MBR 分区并已创建文件系统的情况下，已扩容至小于2TB。则请根据实际情况，通过以下两种方式扩展分区及文件系统：
- [将扩容部分的容量划分至原有 MBR 分区](#Add)
- [将扩容部分的容量格式化成独立的 MBR 分区](#New)


## 前提条件
fdisk/e2fsck/resize2fs 自动扩容工具适用于 Linux 操作系统，用于将新扩容的云硬盘空间添加到已有的文件系统中，扩容能够成功必须满足以下条件：
- 已确认扩容分区格式，详情请参考 [确认扩展方式](https://cloud.tencent.com/document/product/362/53363)。
- 文件系统是 EXT2/EXT3/EXT4/XFS。
- 当前文件系统不能有错误。
- 扩容后的磁盘大小不超过2TB。
- 文档中使用的扩容工具仅支持 Python 2 版本，不支持 Python 3 版本。



## 操作步骤

[](id:Add)
### 将扩容部分的容量划分至原有 MBR 分区
以 root 用户执行以下命令，查询云硬盘的分区信息。
```
lsblk
```
 - 返回信息如下图所示，则说明仅具备1个分区。您可使用工具进行自动扩容，详情请参见 [使用工具扩容](#AutomaticExpansion)。
 ![](https://main.qcloudimg.com/raw/297d678489b57dd70171a8882c9416f4.png)
 - 返回信息如下图所示，则说明已具备 `vdb1`、`vdb2` 两个分区。如果您具备2个或以上分区时，请参考 [手动扩容](#ManualExpansion) 选择分区进行扩容。
![](https://main.qcloudimg.com/raw/070f2144acc543c84d4ab8ab3db25620.png)

<dx-tabs>
::: 使用工具扩容[](id:AutomaticExpansion)
>?使用工具扩容的方式支持仅1个分区的场景。若存在2个及以上分区，请使用 [手动扩容](#ManualExpansion) 方式。
>
1. 以 root 用户执行以下命令，卸载分区。
``` 
umount <挂载点>
```本文挂载点以 `/data` 为例，则执行：
```
umount /data
```
2. 执行以下命令，下载工具。
```
wget -O /tmp/devresize.py https://tencentcloud.coding.net/p/tencentcloud/d/tencentcloud-cbs-tools/git/raw/master/devresize/devresize.py?download=true
```
3. 执行以下命令，使用扩容工具进行扩容。
```
python /tmp/devresize.py <硬盘路径>
```本文以硬盘路径以 `/dev/vdb` ，文件系统在 `vdb1` 上为例，则执行：
```
python /tmp/devresize.py /dev/vdb
```
 - 若输出 `The filesystem on /dev/vdb1 is now XXXXX blocks long.` 如下图所示，则表示扩容成功，请执行 [步骤4](#step4MBR)。
![](https://main.qcloudimg.com/raw/689209e1d1f8a227274e8e65be07d2ec.png)
 - 若输出 `[ERROR] - e2fsck failed!!`，请执行以下步骤：
   a. 执行以下命令，修复文件系统所在分区。
```
fsck -a <分区路径>
```本文以硬盘路径是`/dev/vdb`且文件系统在 `vdb1` 上为例，则执行：
```
fsck -a /dev/vdb1
```    b. 修复成功后，再次执行以下命令，使用扩容工具进行扩容。
```
python /tmp/devresize.py /dev/vdb
```
4. [](id:step4MBR)执行以下命令，手动挂载扩容后的分区，本文以挂载点以 `/data` 为例。
```
mount <分区路径> <挂载点>
```若扩容前已有分区且以分区路径以 `/dev/vdb1` 为例，则执行：
```
mount /dev/vdb1 /data
```
5. 执行以下命令，查看扩容后的分区容量。
```
df -h
```若返回类似如下图所示的信息，说明挂载成功，即可查看到数据盘：
![](https://main.qcloudimg.com/raw/4f57fd2e0038dc1fba5a4389d01ab7dc.png)
6. 执行以下命令，查看扩容后原分区的数据信息，确认新增加的存储空间是否扩容到文件系统中。
```
ll /data
```
:::
::: 手动扩容[](id:ManualExpansion)
1. 以 root 用户执行以下命令，卸载分区。
```
umount <挂载点>
```本文挂载点以 `/data` 为例，则执行：
```
umount /data
```
2. 执行以下命令，扩容分区 `vdb2`。本文以扩容 `vdb2` 分区为例，您可根据实际情况修改命令。 
```
growpart /dev/vdb 2
```
3. 执行以下命令，扩容分区的文件系统。
```
resize2fs /dev/vdb2
```返回结果如下图所示，则表示已成功扩容。
![](https://main.qcloudimg.com/raw/ba8d2693823a3eb0ccfc4dd097f09ed5.png)
4. [](id:step4MBR)执行以下命令，手动挂载扩容后的分区，本文以挂载点以 `/data` 为例。
```
mount <分区路径> <挂载点>
```若扩容前已有分区且以分区路径以 `/dev/vdb2` 为例，则执行：
```
mount /dev/vdb2 /data
```
5. 执行以下命令，查看扩容后的分区容量。
```
df -h
```若返回类似如下图所示的信息，说明挂载成功，即可查看到数据盘：
![](https://main.qcloudimg.com/raw/92cd4cc0e9b1c08975603f73e922266f.png)
6. 执行以下命令，查看扩容后原分区的数据信息，确认新增加的存储空间是否扩容到文件系统中。
```
ll /data
```
:::
</dx-tabs>


[](id:New)
### 将扩容部分的容量格式化成独立的 MBR 分区
1. 以 root 用户执行以下命令，查看已挂载的数据盘分区信息。
```
df -h
```
已挂载数据盘分区为20GB。如下图所示：
![](https://main.qcloudimg.com/raw/4f57fd2e0038dc1fba5a4389d01ab7dc.png)
2. 执行以下命令，查看数据盘扩容后未分区的信息。
```
fdisk -l
```
数据盘已扩容至30GB。如下图所示：
![](https://main.qcloudimg.com/raw/f21420374b4334a790022c95bac1fe0f.png)
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
4. [](id:Step4MBR)执行以下命令，新建一个新分区。
```
fdisk <硬盘路径>
```
本文以磁盘路径以 `/dev/vdb` 为例，则执行：
```
fdisk /dev/vdb
```
按照界面的提示，依次执行以下步骤：
 1. 输入 **p**：查看现有分区信息，本文已有分区 `/dev/vdb1`。
 2. 输入 **n**：新建分区。
 3. 输入 **p**：新建主分区。
 4. 输入 **2**：新建第2个主分区。
 5. 按2次 **Enter**：分区大小使用默认配置。
 6. 输入 **w**：保存分区表，开始分区。
 如下图所示：
![](https://main.qcloudimg.com/raw/894ba5a11a73d56a0a165ee7cb49e7c6.png)
>? 本文以创建一个分区为例，您可以根据实际需求创建多个分区。
>
5. 执行以下命令，查看新分区。
```
fdisk -l
```
新的分区 `vdb2` 已经创建完成。如下图所示：
![](https://main.qcloudimg.com/raw/d604d00955d0db5f052e964ecd409cc3.png)
6. 执行以下命令，格式化新分区并创建文件系统，您可以自行选择文件系统的格式，例如 EXT2、EXT3 等。
```
mkfs.<fstype> <分区路径> 
```
本文以 EXT4 为例，则执行：
```
mkfs.ext4 /dev/vdb2
```
已成功创建 EXT4 文件系统，如下图所示：
![](https://main.qcloudimg.com/raw/db15ed11252e6db8adb706f61ed14225.png)
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
本文以新分区路径 `/dev/vdb2`，新挂载点 `/data1` 为例，则执行：
```
mount /dev/vdb1 /data2
```
9. 执行以下命令，查看新分区信息。
```
df -h
```
返回如下图所示信息则说明挂载成功，即可以查看到数据盘：
![](https://main.qcloudimg.com/raw/465c988014acc85957078335d776bfc3.png)
>?若您希望云服务器在重启或开机时能自动挂载数据盘，则需要执行 [步骤10](#AddNewPartINFOstep10) 和 [步骤11](#AddNewPartINFOstep11) 添加新分区信息至`/etc/fstab`中。
10. [](id:AddNewPartINFOstep10)执行以下命令，添加信息。
```
echo '/dev/vdb2 /data1 ext4 defaults 0 0' >> /etc/fstab
```
11. [](id:AddNewPartINFOstep11)执行以下命令，查看信息。
```
cat /etc/fstab
```
若返回如下图所示信息，则表示添加分区信息成功。
![](https://main.qcloudimg.com/raw/761a846bafe385b24dfb322a6ad2977f.png)

## 相关文档
[扩展分区及文件系统（Windows）](https://cloud.tencent.com/document/product/362/6737)

## 常见问题
如果您在使用云硬盘过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- [使用相关问题](https://cloud.tencent.com/document/product/362/17819)
- [功能相关问题](https://cloud.tencent.com/document/product/362/17818)
