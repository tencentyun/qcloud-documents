
# PTR 记录
### 概述
当您想要通过内网IP地址反向解析对应的内网域名时，可以通过PTR记录类型实现。本文档指导您如何添加 PTR 记录。

> ？添加 PTR 记录前需要先配置反向私有域解析。请查看： [反向解析及PTR记录说明](1)

### 前提条件

- 已创建对应的私有域。

- 已配置反向私有域解析。

###  操作步骤


1. 登录 [Private DNS 管理控制台](https://console.cloud.tencent.com/privatedn)。

2. 在 Private DNS 管理控制台中，在私有域列表中选择并单击需要添加 PTR 记录的私有域名称或【解析】。如下图所示：

![](https://main.qcloudimg.com/raw/6f6017c3a26261516523e71f242ebe54.png)

3. 在解析记录页签中，单击【添加记录】并填写相关记录值信息。如下图所示：

![](https://main.qcloudimg.com/raw/60d905296d366c72d2dbc5913c96b6e5.png)

- **主机记录**：填写反向解析记录的名称。
- **记录类型**：选择 “PTR”。
- **记录值**：填写内网IP地址对应的内网域名。
- **TTL**：为缓存时间，数值越小，修改记录各地生效时间越快，默认为600秒。

4. 单击【保存】，完成添加。
>?
操作过程中如果出现问题，请您 [联系我们](https://cloud.tencent.com/act/event/connect-service)。



