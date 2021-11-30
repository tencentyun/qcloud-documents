
腾讯云 TDSQL-C for MySQL 提供数据库审计能力，记录对数据库的访问及 SQL 语句执行情况，帮助企业进行风险控制，提高数据安全等级。  

## 开通 SQL 审计服务
1. 登录 [TDSQL-C 控制台](https://console.cloud.tencent.com/dls/cynosdb/instance)，在左侧导航选择**数据库审计**页，在上方选择地域后，在**审计实例**页，单击**未开启**过滤未开启审计的实例。
![](https://main.qcloudimg.com/raw/da248852896346436e0669bf289002ec.png)
>?或在**审计日志**页的审计实例处，直接搜索未开通的实例进行开通。
>![](https://main.qcloudimg.com/raw/1ca4ee44a8286b230c55013e5fbc3769.png)
2. 在**审计实例**页，单击需要开通审计的实例 ID 进入开通页面，选择日志保存时长，单击**开通**。
>?
>- 审计日志保存时长支持选择7天、30天、6个月、1年、3年、5年。开通完后也可在控制台修改保存时长，请参见 [修改日志保存时长](https://cloud.tencent.com/document/product/672/61305)。
>- 为保证满足安全合规性对 SQL 日志保留时长的要求，建议用户选择180天及以上的保存时长。

## 查看审计日志
开通审计后，可在**审计日志**页查看对应的 SQL 审计日志，请参见 [审计日志](https://cloud.tencent.com/document/product/672/61284)。
