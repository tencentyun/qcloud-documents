## 操作场景
通过添加 AAAA 记录可将域名指向一个 IPv6 地址。本文档指导您如何添加 AAAA 记录。

## 前提条件
已创建对应的私有域。

## 操作步骤
1. 登录 [Private DNS 控制台](https://console.cloud.tencent.com/privatedns)，并单击左侧导航栏的【私有域解析】，即可进入私有域列表。
2. 在 “私有域列表” 中，单击您需要添加 AAAA 记录的私有域名称或【解析】。如下图所示：
![](https://main.qcloudimg.com/raw/965b35507b9de90112d57608a95d6405.png)
3. 在【解析记录】页签中，单击【添加记录】并填写相关记录值信息。如下图所示：
![](https://main.qcloudimg.com/raw/60d905296d366c72d2dbc5913c96b6e5.png)
 - **主机记录**：填写子域名。例如，添加 `www.dnspod.cn` 的解析，您在 “主机记录” 处选择 “www” 即可。如果只是想添加 `dnspod.cn` 的解析，您在 “主机记录” 处选择 “@” 即可。
 - **记录类型**：选择 “AAAA”。
 - **记录值**：填写 IP 地址，只可以填写 IPv6 地址。例如 `::0101:0101`。
 - **MX 优先级**：不需要填写。
 - **TTL**：为缓存时间，数值越小，修改记录各地生效时间越快，默认为600秒。
4. 单击【保存】，完成添加。

>?操作过程中如果出现问题，请您 [联系我们](https://cloud.tencent.com/act/event/connect-service)。



