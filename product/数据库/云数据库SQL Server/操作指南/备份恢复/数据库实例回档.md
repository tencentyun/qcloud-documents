## 操作场景
云数据库 SQL Server 提供回档工具可对 SQL Server 实例进行回档操作，通过定期镜像备份和实时流水重建历史数据，将云数据库回档到指定时间，且可以保证所有数据的时间切片一致。云数据库 SQL Server 的全量备份和日志备份保存7天，用户可以回档 SQL Server 实例数据到7天之内的任意时刻。本文为您介绍通过控制台对 SQL Server 实例进行回档的具体操作。

## 操作步骤
1.	登录 [SQL Server 控制台](https://console.cloud.tencent.com/sqlserver)，单击实例名称进入实例实例详情页，在右上角单击【回档】。
![](//mccdn.qcloud.com/static/img/6e9523611eb2bb6574c23bb78f2ed3c3/image.png)
2.	设置需要回档的数据库、回档时间、是否覆盖原库，并单击【下一步】。
![](//mccdn.qcloud.com/static/img/71e6e919e84f6c38e396daed4ea1c7fd/image.png)
3.	确认设置的参数无误后，单击【回档】启动回档任务。
4.	返回实例列表，实例状态变成【任务执行中】，可在任务列表中查看回档进度。
![](//mccdn.qcloud.com/static/img/6745a9fe2877d953d07de00cfaade272/image.png)
5.	回档成功，由于之前选择不覆盖原库，因此可以在数据库管理页看到生成的复制库。
![](//mccdn.qcloud.com/static/img/5e8c765027e5acea83a52f4b7e8203d2/image.png)
>!
>- 回档目前仅支持在本地实例进行，可以选择覆盖原库或生成一份复制库。
>- 如果选择生成一份复制库，则需要注意回档后的磁盘空间不能超过实例可用的磁盘空间，否则会出现回档失败。
