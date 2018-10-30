## 操作场景

完成 [扩容云硬盘](https://cloud.tencent.com/document/product/362/5747) 操作后，虽然已经扩大了实体存储空间，但对于已经创建了文件系统的实例来说，还需要扩容文件系统来识别新扩容的空间。本文档为 Windows 系统下扩容文件系统的指引。

## 注意事项

- 扩容文件系统操作不慎可能影响已有数据，因此强烈建议您在操作前手动 [创建快照](https://cloud.tencent.com/document/product/362/5755) 以备份数据。
- 云硬盘扩容需要 [重启实例](https://cloud.tencent.com/document/product/213/4928) 或重新扫描磁盘后才能识别，这将导致您的业务有一定时间的中断，请您谨慎操作。

## 前提条件

- 已完成 [扩容实体云硬盘](https://cloud.tencent.com/document/product/362/5747) 。
- 确保该云硬盘已经 [连接到 Windows 云服务器](https://cloud.tencent.com/document/product/362/5745) 上。
- 若此云硬盘上没有经过格式化和创建文件系统，直接在原有空白云硬盘基础上增加了容量，可以参考 [Windows 系统分区、格式化及创建文件系统](https://cloud.tencent.com/document/product/362/6734) 进行操作。

## 重新扫描磁盘

重新扫描磁盘需满足以下其中一条条件：
- 当硬盘为 **未挂载** 或者 **已挂载且服务器已关机** 的状态时，执行了扩容操作，那么您可以直接进行【执行扩展卷】操作。

- 当云硬盘已连接在云服务器中，并且该云服务器在正常运行状态时执行了硬盘扩容操作，需要先执行【重新扫描磁盘】操作来识别扩容后的硬盘空间。

- 进入【服务器管理】-【磁盘管理】页面，右键单击【磁盘管理】，选择【重新扫描磁盘】。扫描完成后，可看到数据盘已经为扩容后的大小（本例中执行扫描操作后识别到硬盘由原来的 10GB 扩容到了 50GB）。
![](https://main.qcloudimg.com/raw/fd48a45d1454cabdbf04418120fb0ce6.png)
![](https://main.qcloudimg.com/raw/c83aa73f0ce8ed140aa0bc4d3b35391a.png)

## 执行扩展卷操作
右键单击磁盘空间的任一空白处，选择【扩展卷】，根据扩展卷向导的指引完成扩展卷操作。完成后新增的数据盘空间将会合入原有卷中。
![](https://main.qcloudimg.com/raw/f2be002e959f6b309ff3b674dee9078f.png)

至此您已完成扩容硬盘后的扩容 Windows 文件系统操作。
