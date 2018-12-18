
## 批量回档
### 操作场景

您可以对腾讯云平台中的数据库或表进行回档操作。回档是基于冷备 + binlog，可进行实时数据回档。云数据库回档工具通过定期镜像和实时流水重建，将云数据库或表回档到指定时间，且可以保证所有数据的时间切片一致。期间原有数据库或表的访问不受影响，回档操作会产生新的数据库或表。回档完后，您可以看到原来的数据库或表，以及新建的数据库或表。

>!云数据库不会改动您的任何数据，因个人原因造成的数据损毁可自行回档修复。

### 操作步骤

1. 进入 [云数据库数据控制台](https://console.cloud.tencent.com/cdb)，选中一个或多个需要回档的实例，单击【更多操作】 > 【回档】。
![](https://main.qcloudimg.com/raw/88a14846eb98b00bb371c33269d65ff0.png)
2. 选择回档方式和库表，单击【下一步】。
![](https://main.qcloudimg.com/raw/d724f42f5fedcba64dac08871c19d727.png)

3. 设置库表名和回档时间，单击【批量回档】。
	>!每个实例只能设定一个回档时间。
	
	![](https://main.qcloudimg.com/raw/79446644c75f2cebddc35499e0d4e454.png)
3. 提交成功后会跳转到云数据库任务列表，可查看回档进度。
![](https://main.qcloudimg.com/raw/8ab01277cb89adcefb246b7bc42d0f0d.png)
4. 找到回档实例，单击操作中的【管理】。进入实例页面后，单击【操作日志】，选择【回档日志】，可查看历史回档记录和当前回档进度。
![](https://main.qcloudimg.com/raw/73ce25dc90c9e82868bd32efb66791e7.png)

## 批量SQL操作
### 操作场景
本功能可以在选择的多个实例或数据库上执行 SQL 语句，您可以利用此功能批量创建数据库/表、更改表结构来完成对多个实例的初始化或者变更，使用此功能需要您保证选择的实例的用户名/密码一致。

### 操作步骤

1. 进入 [云数据库数据控制台](https://console.cloud.tencent.com/cdb)，选中一个或多个需要 SQL 操作的实例，单击【更多操作】 > 【SQL操作】。
![](https://main.qcloudimg.com/raw/3765cc1207948449772d509594fa853b.png)
2. 选择需要操作的实例或数据库，单击进入【下一步】。
![](https://main.qcloudimg.com/raw/0ad64ceea6d10ff4fc8d9a2a07121a37.png)
3. 选择 SQL 文件，若未找到需要的 SQL 文件，请单击【新增文件】上传。
![](https://mc.qcloudimg.com/static/img/81a527221f924a30907f21bc79f07993/sql_three.png)
4. 确认需要操作的实例或数据库以及 SQL 文件，确定无误后输入密码，单击【启动】。
![](https://mc.qcloudimg.com/static/img/cbf17bc5623e08a61bcd0235a20cf3d7/sql_four.png)
5. 操作提交后可以在【任务列表】内查看任务信息。
![](https://mc.qcloudimg.com/static/img/1a3e03af04e2c2703a94aef948dede24/sql_five.png)
