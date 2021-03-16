
本文为您介绍如何通过控制台设置 MySQL 实例的 Binlog 保留周期。

## Binlog 说明
云数据库 MySQL 实例在执行大事务或大量 DML 时会产生较多的 Binlog，Binlog 写满 256MB 会进行一次切割，切割后的 binlog 文件会被上传至对象存储 COS，然后控制台的日志列表会显示上传到 COS 的 binlog 文件。
![](https://main.qcloudimg.com/raw/631ad0a24ba889e7a08e1c20665d7fa1.png)

## 操作场景
Binlog 在上传至 COS 前，会暂存于实例磁盘，从而导致磁盘使用空间增加。您可以通过控制台设置 Binlog 保留周期来控制占用空间的比例，也可以扩容磁盘，建议磁盘使用率不超过80%，其次建议您及时清理无用数据。
- Binlog 是 MySQL 同步数据，确保高可用性、可恢复性的基础，不可关闭。
- 生成的 Binlog 会先通过系统的 [自动备份功能](https://cloud.tencent.com/document/product/236/35172#.E8.87.AA.E5.8A.A8.E5.A4.87.E4.BB.BD-mysql-.E6.95.B0.E6.8D.AE) 备份到 COS，备份后的 Binlog 会根据设置的本地 Binlog 保留策略进行删除，当前正在使用当 Binlog 无法被清理，防止异常。因此，清理的过程有一定的延迟，设置后请耐心等待一段时间。

## 操作步骤
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/cdb)，在实例列表页，单击实例名，进入实例管理页面。
2. 在实例管理页面，选择【备份恢复】页，单击【本地Binlog设置】。
3. 在弹出的对话框，填写需要保留的时长以及空间使用率，确认无误后，单击【确定】。
>?开启可用空间保护后，超过80%或剩余空间不足5GB时，会强制清理 Binlog。从最早的开始清理，直到总空间使用率降到80%以下且剩余空间大于5GB。
>
![](https://main.qcloudimg.com/raw/45137bc240489e3725a33e5abab14ca1.png)

## 热点问题
#### 本地 Binlog 保留设置过小是否会影响数据库恢复？
不影响，产生的 Binlog 会通过自动备份功能尽快上传至 COS，尚未上传的 Binlog 不会进行清理，本地 Binlog 保留设置过小会影响回档速度，请进行适当配置。

#### 

