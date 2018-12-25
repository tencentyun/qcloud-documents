## 批量续费
1. 进入 [云数据库数据控制台](https://console.cloud.tencent.com/cdb)，选中一个或多个需要续费的实例，单击【续费】操作。
![](https://mc.qcloudimg.com/static/img/83008284f2d39df398d2cce0cc3eb706/check_one.png)
2. 选择续费时长，单击【确定】后进入下一步。
![](https://mc.qcloudimg.com/static/img/2e4a806ce72aeacfc9fd0ca2d4446bfb/check_two.png)
3. 确认订单信息后，单击【确认购买】。
![](https://mc.qcloudimg.com/static/img/6a6ca027e73ae123bef06cbc443bcf9d/check_three.png)
4. 订单支付成功，可继续查看订单，或跳转到管理中心。
![](https://mccdn.qcloud.com/img56825d7c5d5ea.png)

## 批量回档

用户可以对腾讯云平台中的数据库或表进行回档操作。回档是基于冷备 + binlog，可进行实时数据回档。云数据库回档工具通过定期镜像和实时流水重建，将云数据库或表回档到指定时间，且可以保证所有数据的时间切片一致。期间原有数据库或表的访问不受影响，回档操作会产生新的数据库或表。回档完后，用户可以看到原来的数据库或表，以及新建的数据库或表。

>**注意：**  
>云数据库不会改动用户的任何数据，因用户个人原因造成的数据损毁可自行回档修复。

### 批量回档具体操作步骤

1. 进入 [云数据库数据控制台](https://console.cloud.tencent.com/cdb)，选中一个或多个需要回档的实例，单击【更多操作】 > 【回档】。
![](https://mc.qcloudimg.com/static/img/38b5002d8b4d158a5c57c150b50277ad/reback_one.png)
2. 选择回档方式，指定需要回档的库表和回档时间，单击【批量回档】。
>**注意：**  
>每个实例只能设定一个回档时间。</blockquote>
![](https://mc.qcloudimg.com/static/img/7a01be7903fd592133ea40b88b1b399c/reback_two.png)
3. 提交成功后会显示云数据库任务列表，可查看回档进度。
![](https://mc.qcloudimg.com/static/img/0a0cd866d319f103dc452fc39c9e7a54/reback_three.png)
4. 找到回档实例，单击操作中的【管理】。进入实例页面后，单击【操作日志】，选择【回档日志】，可查看历史回档记录和当前回档进度。
![](https://mc.qcloudimg.com/static/img/3faa954178e5e2e1b4a3e99b6597fd89/reback_four.png)

## 批量SQL操作

本功能可以在选择的多个实例或数据库上执行 SQL 语句，您可以利用此功能批量创建数据库/表、更改表结构来完成对多个实例的初始化或者变更，使用此功能需要您保证选择的实例的用户名/密码一致。

### 批量SQL操作操作步骤

1. 进入 [云数据库数据控制台](https://console.cloud.tencent.com/cdb)，选中一个或多个需要 SQL 操作的实例，单击【更多操作】 > 【SQL操作】。
![](https://mc.qcloudimg.com/static/img/e404ae00352e6118163f7a6701edd228/sql_one.png)
2. 选择需要操作的实例或数据库，单击进入【下一步】。
![](https://mc.qcloudimg.com/static/img/2301e2abe6a5486c4764aa1d75227565/sql_two.png)
3. 选择 SQL 文件，若未找到需要的 SQL 文件，请单击【新增文件】上传。
![](https://mc.qcloudimg.com/static/img/81a527221f924a30907f21bc79f07993/sql_three.png)
4. 确认需要操作的实例或数据库以及 SQL 文件，确定无误后输入密码，单击【启动】。
![](https://mc.qcloudimg.com/static/img/cbf17bc5623e08a61bcd0235a20cf3d7/sql_four.png)
5. 操作提交后可以在【任务列表】内查看任务信息。
![](https://mc.qcloudimg.com/static/img/1a3e03af04e2c2703a94aef948dede24/sql_five.png)
