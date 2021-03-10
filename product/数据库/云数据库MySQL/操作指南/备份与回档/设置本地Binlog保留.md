

本文为您介绍如何通过控制台设置 MySQL 实例的 Binlog 保留周期。

## 操作场景
云数据库 MySQL 实例的 Binlog 会占用存储空间，您可以通过设置 Binlog 保留周期来控制占用空间的比例，本地的 Biniog 也能够加快回档的速度，请根据需要进行合理的配置。

## 操作步骤
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/cdb)，在实例列表页，单击实例名，进入实例管理页面。
2. 在实例管理页面，选择【备份恢复】页，单击【本地Binlog设置】。
3. 在弹出的对话框，填写需要保留的时长以及使用率，确认无误后，单击【确定】。
![](https://main.qcloudimg.com/raw/45137bc240489e3725a33e5abab14ca1.png)

## 热点问题
#### 本地 Binlog 保留设置过小是否会影响数据库恢复？
不影响，产生的 Binlog 会尽快上传至 COS，尚未上传的 Binlog 不会进行清理，本地 Binlog 保留设置过小会影响回档速度，请进行适当配置。



