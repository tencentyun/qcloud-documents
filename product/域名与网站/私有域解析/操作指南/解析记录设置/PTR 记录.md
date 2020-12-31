## 操作场景
当您想要通过内网 IP 地址反向解析对应的内网域名时，可以通过 PTR 记录类型实现。本文档指导您如何添加 PTR 记录。
>?添加 PTR 记录前需要先配置反向私有域解析。具体操作请参考 [反向解析及 PTR 记录说明](https://cloud.tencent.com/document/product/1338/50546)。

## 前提条件
- 已创建对应的私有域。
- 已配置反向私有域解析。

## 操作步骤
1. 登录私有域解析 [Private DNS 管理控制台](https://console.cloud.tencent.com/privatedn)，并单击左侧导航栏的【私有域列表】，即可进入私有域列表。
2. 在 “私有域列表” 中，单击您需要添加 PTR 记录的私有域名称或【解析】。如下图所示：
![](https://main.qcloudimg.com/raw/965b35507b9de90112d57608a95d6405.png)
3. 在解析记录页签中，单击【添加记录】并填写相关记录值信息。如下图所示：
![](https://main.qcloudimg.com/raw/c6784df532f337d82a9a4e5eb4e364f5.png)
 - **主机记录**：主机记录与创建域名（不含 `in-addr.arpa`）组合为固定 IPV4 格式，每个网段仅限输入0 - 255的整数。
 - **记录类型**：仅支持 “PTR”。
 - **记录值**：填写内网 IP 地址对应的私有域名。
 - **TTL**：为缓存时间，数值越小，修改记录生效时间越快，默认设置为300，支持自定义1 - 86400区间的整数。
4. 单击【保存】，完成添加。

>?操作过程中如果出现问题，请您 [联系我们](https://cloud.tencent.com/act/event/connect-service)。



