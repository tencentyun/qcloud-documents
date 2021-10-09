
本文为您介绍如何通过控制台设置 MySQL 实例的 binlog 保留周期。

## binlog 说明
云数据库 MySQL 实例在执行大事务或大量 DML 时会产生较多的 binlog，binlog 写满 256MB 会进行一次切割，切割后的 binlog 文件会被上传至对象存储 COS，然后控制台的日志列表会显示上传到 COS 的 binlog 文件。
![](https://main.qcloudimg.com/raw/631ad0a24ba889e7a08e1c20665d7fa1.png)

## 操作场景
binlog 在上传至 COS 前，会暂存于实例磁盘，从而导致磁盘使用空间增加。您可以通过控制台设置 Binlog 保留周期来控制占用空间的比例，也可以扩容磁盘，建议磁盘使用率不超过80%，其次建议您及时清理无用数据。
- binlog 是 MySQL 同步数据的基础，为保障数据库的可恢复性、稳定性、高可用能力，云数据库 MySQL 不支持关闭 binlog。
- 生成的 binlog 会先通过系统的 [自动备份功能](https://cloud.tencent.com/document/product/236/35172#.E8.87.AA.E5.8A.A8.E5.A4.87.E4.BB.BD-mysql-.E6.95.B0.E6.8D.AE) 备份到 COS，备份后的 binlog 会根据设置的本地 binlog 保留策略进行删除，当前正在使用的 binlog 无法被清理，防止异常。因此，清理的过程有一定的延迟，设置后请耐心等待一段时间。
>?清理过期 binlog 日志规则：
>每60秒检查一次本地 binlog 日志，如果检查到 binlog 开始时间或占用空间不符合设定的保留规则时，会加入到待删除队列。删除队列中的 binlog 会按照时间排序，从最早的 binlog 开始逐一删除，直至清空待删除队列。

## 操作步骤
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/cdb)，在实例列表页，单击实例 ID，进入实例管理页面。
2. 在实例管理页面，选择**备份恢复**页，单击**本地Binlog设置**。
3. 在弹出的对话框，填写需要保留的时长以及空间使用率，确认无误后，单击**确定**。
![](https://main.qcloudimg.com/raw/b89530c6ef7975102afd5f3a1072636e.png)

## 热点问题
#### 本地 binlog 保留设置过小是否会影响数据库恢复？
不影响，产生的 binlog 会通过自动备份功能尽快上传至 COS，尚未上传的 binlog 不会进行清理，本地 binlog 保留设置过小会影响回档速度，请进行适当配置。

#### 本地 binlog 保留默认设置是多少？
本地 binlog 默认保留时长：120小时，空间使用率默认不超过30%。

#### binlog 是否会占用实例磁盘空间？
会，生成的 binlog 会先自动备份到 COS，备份后的 binlog 会根据设置保留策略进行删除，期间 binlog 会暂存至实例磁盘。
