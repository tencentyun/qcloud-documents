
# CNAME 记录
### 概述

如果需要将域名指向另一个域名，再由另一个域名提供 IP 地址，就需要添加 CNAME 记录。本文档指导您如何添加 CNAME 记录。

### 前提条件

已创建对应的私有域。

###  操作步骤
1.登录 [Private DNS 管理控制台](https://console.cloud.tencent.com/privatedns)。

2. 在Private DNS  管理控制台中，在私有域列表中选择并单击需要创建 A 记录的私有域名称或【解析】。如下图所示：

![](https://main.qcloudimg.com/raw/6f6017c3a26261516523e71f242ebe54.png)

3. 在解析记录页签中，单击【添加记录】并填写相关记录值信息。如下图所示：

![](https://main.qcloudimg.com/raw/60d905296d366c72d2dbc5913c96b6e5.png)


- **主机记录**：填写子域名。例如，添加 www.dnspod.cn 的解析，您在 “主机记录” 处选择 “www” 即可。如果只是想添加 dnspod.cn 的解析，您在 “主机记录” 处选择 “@” 即可。
- **记录类型**：选择 “CNAME”。
- **记录值**：CNAME 指向的域名，只可以填写域名。如：`https://www.dnspod.com`。
- **MX 优先级**：不需要填写。
-  **TTL**：为缓存时间，数值越小，修改记录各地生效时间越快，默认为600秒。
4. 单击【保存】，完成添加。

>?
>
>- 相同主机记录的CNAME记录类型只能添加一条，且不能与其他任何记录共存。
>
>- 操作过程中如果出现问题，请您 [联系我们](https://cloud.tencent.com/act/event/connect-service)。



