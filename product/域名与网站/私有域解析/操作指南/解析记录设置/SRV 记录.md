## 操作场景
SRV 记录用来标识某台服务器使用了某个服务，常见于微软系统的目录管理。本文档指导您如何添加 SRV 记录。

## 前提条件
已创建对应的私有域。详情请查看 [创建私有域](https://cloud.tencent.com/document/product/1338/50532)。

## 操作步骤
1. 登录私有域解析 [Private DNS 管理控制台](https://console.cloud.tencent.com/privatedns/)，并单击左侧导航栏的**私有域列表**，即可进入私有域列表。
2. 在 “私有域列表” 中，单击您需要添加 SRV 记录的私有域名称或**解析**。如下图所示：
![](https://main.qcloudimg.com/raw/965b35507b9de90112d57608a95d6405.png)
3. 在**解析记录**页签中，单击**添加记录**并填写相关记录值信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2fd974a599442354bee407a8a1b19fe8.png)
 - **主机记录**：服务的名字.协议的类型。例如，设置为 `_sip._tcp`。
 - **记录类型**：选择 “SRV”。
 - **记录值**：优先级 权重 端口 主机名。记录生成后会自动在域名后面补一个 “.”。
例如，设置为 `0 5 5060 sipserver.dnspod.cn`。
 - **权重**：不需要填写。 
 - **MX 优先级**：不需要填写。 
 - **TTL**：为缓存时间，数值越小，修改记录生效时间越快，默认设置为300，支持自定义1 - 86400区间的整数。
4. 单击**保存**，完成添加。

>?操作过程中如果出现问题，请您 [联系我们](https://cloud.tencent.com/act/event/connect-service)。




