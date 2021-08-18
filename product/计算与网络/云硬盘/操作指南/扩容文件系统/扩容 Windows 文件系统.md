## 操作场景

在通过控制台 [扩容云硬盘](https://cloud.tencent.com/document/product/362/5747) 后，需要将扩容部分的容量划分至已有分区内，或者将扩容部分的容量格式化成一个独立的新分区。
- 若您在云硬盘连接在云服务器上并且该云服务为正常运行状态时执行了硬盘扩容操作，需要先执行 [重新扫描磁盘](#Scaning) 操作来识别扩容后的硬盘空间。
- 若您在硬盘待挂载状态/硬盘挂载但服务器已经关机执行了扩容操作，扩容后的硬盘空间将自动识别。

>!
>- 扩容文件系统操作不慎可能影响已有数据，因此强烈建议您在操作前手动 [创建快照](https://cloud.tencent.com/document/product/362/5755) 备份数据。
>- 扩容文件系统需要 [重启实例](https://cloud.tencent.com/document/product/213/4928) 或重新扫描磁盘，将导致一定时间的业务中断，建议您选择合适的时间谨慎操作。
>- 完成扩容操作后，强烈建议您按照 [重新扫描磁盘](#Scaning) 识别扩容后的容量。执行“刷新”等其他操作不能确保系统可识别扩容容量。
>


## 前提条件
- 已通过控制台 [扩容云硬盘](https://cloud.tencent.com/document/product/362/5747)。
- 该云硬盘已通过控制台挂载到 Windows 云服务器并已创建文件系统。详情请参见 [挂载云硬盘](https://cloud.tencent.com/document/product/362/5745)。
- 已登录待扩展分区及文件系统的 Windows 云服务器。详情请参见 [使用 RDP 登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/5435)。
>?本文以 Windows Server 2012 R2 操作系统的云服务器为例，不同操作系统的扩容操作可能略有不同，本文仅供参考。
>

## 操作步骤
>!
>- 如通过控制台 [扩容云硬盘](https://cloud.tencent.com/document/product/362/5747) 时，挂载该盘的云服务器正处于正常运行状态，则需要 [重新扫描磁盘](#Scaning) 待识别扩容后的云硬盘空间后再 [扩容原有分区的文件系统或新建分区](#Extending)。
>- 如通过控制台 [扩容云硬盘](https://cloud.tencent.com/document/product/362/5747) 时，该盘处于待挂载状态或者挂载该盘的云服务器正处于关机状态，直接 [扩容原有分区的文件系统或新建分区](#Extending) 即可。
>- 如果云服务器的存储控制器的 Virtio 驱动版本低于58003，则请 [重启实例](https://cloud.tencent.com/document/product/213/4928) 后再进行以下操作。可参考 [查看 Virtio 驱动版本](#VirtioVersion)，确定正在使用的 Virtio 驱动版本。 


### 重新扫描磁盘[](id:Scaning)
1. 右键单击<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px">，并选择【计算机管理】。
2. 在“计算机管理”窗口的左侧导航栏中，选择【存储】>【磁盘管理】。
3. 右键单击 【磁盘管理】，选择 【重新扫描磁盘】。如下图所示：
![](https://main.qcloudimg.com/raw/e86a6974b7a49108a4d12a300ffc4c87.png)
4. 扫描完成后，查看数据盘是否已经变为扩容后的大小（本例中执行扫描操作后识别到硬盘由原来的10GB扩容到了50GB）。如下图所示：
![](https://main.qcloudimg.com/raw/9612c8f95826b401d3a7c111fe632b05.png)


### 扩容原有分区的文件系统或新建分区[](id:Extending)
您可根据实际需求，参考以下步骤扩容数据盘原有分区的文件系统，或创建新分区：
<dx-tabs>
::: 扩容原有分区的文件系统
1. 右键单击磁盘空间的任一空白处，选择【扩展卷】。如下图所示：
![](https://main.qcloudimg.com/raw/6b19804749d997c9aa008dfa1d37b5cd.png)
2. 根据扩展卷向导的指引完成扩展卷操作。
完成后新增的数据盘空间将会合入原有卷中。
:::
::: 创建新分区
1. 右键单击磁盘未分配空白处，选择【新建简单卷】。如下图所示：
![](https://main.qcloudimg.com/raw/bf0c7eb05e2658d5b426e85112bbaf0a.png)
2. 根据新建简单卷向导的默认设置完成简单卷操作。
完成后新增的数据盘空间会新建一个分区。
:::
</dx-tabs>


## 相关操作
### 查看 Virtio 驱动版本[](id:VirtioVersion)
1. 右键单击<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px">，并选择【设备管理器】。
2. 在“设备管理器”窗口中，展开【存储控制器】项，并双击【Tencent VirtIO SCSI controller】。
3. 在 “Tencent VirtIO SCSI controller 属性”窗口中，选择【驱动程序】，查看当前版本。如下图所示，当前版本为58005。
![](https://main.qcloudimg.com/raw/d6df197dfc47a719edc42a9b7ed0d4f2.png)


## 相关文档
- [扩容云硬盘](https://cloud.tencent.com/document/product/362/5747)
- [扩展分区及文件系统（Linux）](https://cloud.tencent.com/document/product/362/6738)


