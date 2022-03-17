## 简介

Ckafka 消息备份是腾讯云对象存储（Cloud Object Storage，COS）基于 [云函数（Serverless Cloud Function，SCF）](https://cloud.tencent.com/document/product/583) 为用户提供的 Ckafka 消息转存至 COS 的功能，可以协助用户将 Ckafka 消息进行转存以便于对数据进行分析与下载等操作。

Ckafka 是基于开源 Apache Kafka 消息队列引擎，提供高吞吐性能、高可扩展性的消息队列服务，详情请参见 [Ckafka 产品概述](https://cloud.tencent.com/document/product/597/10066)。

用户在指定存储桶配置了备份函数规则后，当 CKafka 实例产生消息时，云函数会按照一定的时间粒度获取消息并转存至 COS 存储桶中。

## 注意事项

- 若您此前在对象存储控制台上为存储桶添加了 Ckafka 消息备份规则，可以在 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default) 上看到您所创建的 Ckafka 消息备份函数，请**不要**删除该函数，否则可能导致您的规则不生效。
- 已上线云函数的地域均已支持 Ckafka 消息备份至 COS，包括有广州、上海、香港、北京、成都、新加坡、孟买、多伦多、硅谷等，更多支持地域可查看 [云函数产品文档](https://cloud.tencent.com/document/product/583)。

## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 在左侧导航中，单击**应用集成**，找到**Ckafka 消息备份**。
3. 单击**配置备份规则**，进入规则配置页面。
4. 单击**添加函数**。
>! 如果您尚未开通云函数服务，请前往 [云函数控制台](https://console.cloud.tencent.com/scf) 开通云函数服务，按照提示完成服务授权即可。
>
5. 在弹出的窗口中，配置如下信息：
<img src="https://main.qcloudimg.com/raw/34e835fb19db799b33dd3df34920db30.png" width="600px"></br>
 - **函数名称**：作为函数的唯一标识名称，创建后不可修改。您可以在 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default) 上查看该函数。
 - **关联存储桶**：存放 Ckafka 消息的 COS 存储桶。
 - **时间粒度**：根据消息量的大小，选取汇聚消息的时间间隔，时间间隔为5 - 15分钟不等。为保证转存性能，聚合文件数量与 Partition 数量、partition_max 设置数值有关。有关 Partition 的说明，请参见 [分区](https://cloud.tencent.com/document/product/597/32544#F)。
 - **SCF 授权**：CKafka 消息备份需要授权云函数从您的 Ckafka 服务中读取相关实例消息，并将消息转存至您指定的存储桶中。因此需要添加此授权。
6. 单击**下一步**，进行 Ckafka 配置，配置项说明如下：
<img src="https://main.qcloudimg.com/raw/1a12ef90b05a3166a2cb7bae0dcb29f5.png" width="600px"></br>
 - **实例选择**：选择消息来源的 Ckafka 实例，仅支持同地域的 Ckafka 实例。
 - **主题选择**：选择消息来源的主题。
 - **起始位置**：消息转储备份时历史消息的处理方式，topic offset 设置。
 - **访问地址**：必须为 VPC 内网访问地址，基础网络的 CKafka 实例请添加路由策略，具体请参考 [添加路由策略](https://cloud.tencent.com/document/product/597/36348)。
>! 对应的 VPC 子网中必须有可用的 IP，且必须支持 DHCP。
>
7. 单击**下一步**，进行投递配置，配置项说明如下：
<img src="https://main.qcloudimg.com/raw/95aa9a1bdc4204ebbe38ef5c7670712b.png" width="600px"></br>
**投递的路径**：备份文件的投递路径前缀，不填写则默认保存在存储桶根路径，指定前缀必须以斜杠 / 为结尾。
8. 添加配置后，单击**确认**，即可看到函数已添加完成。
![](https://main.qcloudimg.com/raw/49b63186d615972604f007afb80c731f.png)
您可以对新创建的函数进行如下操作：
 - 单击**查看日志**，查看 Ckafka 消息备份的历史运行情况。当备份出现报错时，您还可以通过单击**查看日志**，快速跳转到云函数控制台查看日志错误详情。
 - 单击**编辑**，修改 Ckafka 消息备份规则。
 - 单击**删除**，删除不使用的 Ckafka 消息备份规则。

