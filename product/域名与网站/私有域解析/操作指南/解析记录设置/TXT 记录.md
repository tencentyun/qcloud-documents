## 操作场景
若您希望对域名进行标识和说明，可以使用 TXT 记录。本文档指导您如何添加 TXT 记录。

## 前提条件
已创建对应的私有域。

## 操作步骤
1. 登录 [ Private DNS 管理控制台](https://console.cloud.tencent.com/privatedns)。
2. 在 “私有域列表” 中，单击您需要添加 TXT 记录的私有域名称或【解析】。如下图所示：
![](https://main.qcloudimg.com/raw/6f6017c3a26261516523e71f242ebe54.png)
3. 在解析记录页签中，单击【添加记录】并填写相关记录值信息。如下图所示：
![](https://main.qcloudimg.com/raw/60d905296d366c72d2dbc5913c96b6e5.png)
 - **主机记录**：填写子域名。例如，添加 www.dnspod.cn 的 TXT 记录，您在 “主机记录” 处选择 “www” 即可。若只想添加 dnspod.cn 的 TXT 记录，您在 “主机记录” 处选择 “@” 即可。
 - **记录类型**：选择 “TXT”。
 - **记录值**：没有固定的格式。
 - **MX 优先级**： 不需要填写。
 - **TTL**：为缓存时间，数值越小，修改记录各地生效时间越快，默认为600秒。
4. 单击【保存】，完成添加。

>?操作过程中如果出现问题，请您 [联系我们](https://cloud.tencent.com/act/event/connect-service)。



