
### 审计如何收费？
数据库审计按照审计日志存储量进行按量计费。每小时为一个计费周期，不足一小时的按一小时计费。详情参见 [购买指南](https://cloud.tencent.com/document/product/672/45980)。

### 审计开启之后如何关闭？
登录 [MySQL 控制台](https://console.cloud.tencent.com/dls/mysql/policy)、[TDSQL-C MySQL 版控制台](https://console.cloud.tencent.com/dls/cynosdb/instance)、[MongoDB 控制台](https://console.cloud.tencent.com/dls/mongodb)，在审计日志页单击**服务设置**，选择**关闭服务**。
>!服务关闭后，该实例对应的审计策略、日志和文件将被清空，且无法找回，请您事先自行保存对应的日志和文件。

### 审计数据可以保留多久？
审计数据可以保留7天至5年。您可在 [MySQL 控制台](https://console.cloud.tencent.com/dls/mysql/policy)、[TDSQL-C MySQL 版控制台](https://console.cloud.tencent.com/dls/cynosdb/instance)、[MongoDB 控制台](https://console.cloud.tencent.com/dls/mongodb) 开通审计时设定保留时长，也可在开通后在审计日志页单击**服务设置**进行修改。
