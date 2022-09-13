TDSQL-C MySQL 版提供数据库审计能力，记录对数据库的访问及 SQL 语句执行情况，帮助企业进行风险控制，提高数据安全等级。

## 开通数据库审计
1. 登录 [TDSQL-C MySQL 版控制台](https://console.cloud.tencent.com/dls/cynosdb/instance)，在左侧导航选择**数据库审计**页，在上方选择地域后，在**审计实例**页，单击**未开启**过滤出未开启审计的实例。
![](https://qcloudimg.tencent-cloud.cn/raw/4feac7ced1b7f5519805db9763e9386f.png)
>?或在**审计日志**页的审计实例处，直接搜索未开通的实例进行开通。
>![](https://qcloudimg.tencent-cloud.cn/raw/65481e1c8794548178cd76916d02a6a6.png)
2. 在**审计实例**页，单击需要开通审计的实例 ID 进入开通页面，设置开通范围为当前实例或者整个集群，选择日志保存时长，单击**开通**。
![](https://qcloudimg.tencent-cloud.cn/raw/d43f80895e549e9212b72deb4469c54d.png)
>?
> - 审计日志保存时长支持选择7天、30天、3个月、6个月、1年、3年、5年。开通完后也可在控制台修改保存时长，请参见 [修改日志保存时长]()。
> - 为保证满足安全合规性对 SQL 日志保留时长的要求，建议用户选择180天及以上的保存时长。

## 相关操作
开通数据库审计后，可在审计日志页查看对应的数据库审计日志，或者修改日志保存时长。
- [查看审计日志](https://cloud.tencent.com/document/product/1003/80441)
- [修改日志保存时长](https://cloud.tencent.com/document/product/1003/80442)
