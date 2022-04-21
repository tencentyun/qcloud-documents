腾讯云为云数据库 MySQL 提供数据库审计能力，记录对数据库的访问及 SQL 语句执行情况，帮助企业进行风险控制，提高数据安全等级。  

>!数据库审计目前支持：云数据库 MySQL 5.6、5.7 、8.0双节点和三节点，暂不支持云数据库 MySQL 5.5 版本，以及云数据库 MySQL 单节点。

## [创建审计规则](id:cjsjgz)
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/dls/mysql)，在左侧导航选择**数据库审计**页，在上方选择地域后，选择**审计规则**页。
2. 在审计规则页，单击**新建规则**。
![](https://main.qcloudimg.com/raw/10e4dd9ef29998d7f21075b8a131befa.png)
3. 在创建审计规则页，填写规则名称、描述，单击**下一步**。
4. 在参数设置页，选择所需的审计方式和参数，单击**保存**。
>!
>- 规则创建成功后，需关联审计策略才能生效。
>- SQL 审计规则详细使用说明，请参见 [SQL 审计规则](https://cloud.tencent.com/document/product/672/66136)。

## 开通 SQL 审计服务
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/dls/mysql)，在左侧导航选择**数据库审计**页，在上方选择地域后，在**审计实例**页，单击**未开启**过滤未开启审计的实例。
![](https://main.qcloudimg.com/raw/842507119ce4a974f147260ef82018cb.png)
>?或在**审计日志**页的审计实例处，直接搜索未开通的实例进行开通。
>![](https://main.qcloudimg.com/raw/459e229371de8509536efeec77a88833.png)
2. 在**审计实例**页，单击需要开通审计的实例 ID 进入开通页面，勾选同意协议，单击**下一步**。
3. 在 **SQL 审计服务设置**页，选择审计保存时长，单击**下一步**。
>?
>- 审计日志保存时长支持选择7天、30天、6个月、1年、3年、5年。开通完后也可在控制台修改保存时长，请参见 [修改日志保存时长](https://cloud.tencent.com/document/product/672/61305)。
>- 为保证满足安全合规性对 SQL 日志保留时长的要求，建议用户选择180天及以上的保存时长。
4. 在**创建策略**页，设置策略名称，选择已创建的 [审计规则](https://cloud.tencent.com/document/product/672/66136)，单击**创建策略**。

## 创建审计策略
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/dls/mysql)，在左侧导航选择**数据库审计**页，在上方选择地域后，选择**审计策略**页。
2. 在**审计策略**页，单击**新建策略**。
![](https://main.qcloudimg.com/raw/a0abbbeb325272b06d343009abb81bb3.png)
3. 在弹出的对话框，设置策略名称，选择已创建的 [审计规则](https://cloud.tencent.com/document/product/672/66136)，单击**确定**。

## 查看审计日志
开通审计后，可在**审计日志**页查看对应的 SQL 审计日志，请参见 [审计日志](https://cloud.tencent.com/document/product/672/61284)。

