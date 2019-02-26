手动挂载云硬盘后，云硬盘作为云服务器的数据盘使用，默认为脱机状态。您需要对数据盘进行格式化、分区及创建文件系统等初始化操作。 常用的磁盘分区形式有主启动记录分区（Main Boot Record，MBR）和全局分区表（Guid Partition Table，GPT），磁盘投入使用后再切换磁盘分区形式，**磁盘上的原有数据将会清除**，因此请根据实际需求合理选择分区形式。
两种分区形式的简介如下表所示。

| 分区形式 | 支持最大磁盘容量 | 支持分区数量 | 分区工具 |
|---------|---------|---------|---------|
|MBR | 2TB |<li>4个主分区</li><li>3个主分区和1个扩展分区</li>|Windows 操作系统：磁盘管理</br>Linux 操作系统：<ul><li>fdisk 工具</li><li>parted 工具</li></ul> |
|GPT | 18EB</br>目前云硬盘支持的最大容量为16TB | 不限制分区数量|Windows 操作系统：磁盘管理</br>Linux 操作系统：parted 工具|

请根据磁盘容量大小、云服务器操作系统类型选择合适的操作指引：
- 磁盘容量小于2TB时：
 - [初始化云硬盘（Windows）](https://cloud.tencent.com/document/product/362/6734#Windows2008)
 - [初始化云硬盘（Linux）](https://cloud.tencent.com/document/product/362/6734#Linux)
- 磁盘容量大于等于2TB时：
 - [初始化云硬盘（Windows）](https://cloud.tencent.com/document/product/362/6735#2TBWindows2012)
 - [初始化云硬盘（Linux）](https://cloud.tencent.com/document/product/362/6735#2TBLinux)
