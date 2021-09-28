## 操作场景

Serverless 架构的入湖方案是通过云函数触发器拉起数据调用后，通过云函数捕获并记录批次数据信息，在函数内闭环相关的结构转换和数据格式转换，数据压缩等能力。在本文档示例中，我们用到了云函数 SCF、对象存储 COS 对 TDMQ 消息进行备份。

## 操作步骤

### 创建 COS 储存桶

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 选择左侧“存储桶列表”，单击**创建存储桶**，新建源 COS Bucket。
3. 设置 COS Bucket 的名称，例如 “`scf-data-lake`”，地域为“广州” ，设置访问权限为默认值“私有读写” ，单击**确定**完成创建。

### 创建消息队列 TDMQ

1. 通过 TDMQ 控制台创建集群和 Topic 等资源，详情可参见 [TDMQ 资源创建与准备](https://cloud.tencent.com/document/product/1179/44814)。
2. TDMQ 集群需接入 VPC，详情可参见 [VPC 接入](https://cloud.tencent.com/document/product/1179/46240)。

### 通过 COS 应用集成进行函数配置 

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 选择左侧“应用集成”，在“数据迁移与备份”中选择“TDMQ消息备份”。如下图所示：
![](https://main.qcloudimg.com/raw/673f44c32c0870e1ca64e57ca87df9ef.png)
3. 在 “TDMQ消息备份”页中，选择已创建的 COS Bucket 所在的地域，并单击**添加函数**。 
4. 在“创建TDMQ消息备份函数”弹窗中，进行函数基础配置。输入函数名称，例如 `data-lake`，并关联已创建的 Bucket `scf-data-lake`，勾选**授权SCF服务**后单击**下一步**。
5. 单击**下一步**，进行 TDMQ 配置，配置项说明如下：
   - **集群选择**：选择消息来源的 TDMQ 集群，仅支持同地域的 TDMQ 集群。
   - **命名空间**：选择集群中的命名空间。
   - **主题选择**：选择消息来源的主题。
   - **订阅选择**：选择对应的主题订阅，如现有的订阅不满足需求，可前往 TDMQ 控制台的 [消费管理](https://console.cloud.tencent.com/tdmq/topic-subscription?rid=1&clusterId=pulsar-5rqmwvrxv8&env=default&topic=zetest) 新建订阅。
   - **起始位置**：历史消息的起始位置。
   - **角色选择**：选择 TDMQ 角色。TDMQ 的“角色”是 TDMQ 内专有的概念，区别于腾讯云的“角色”，是用户自行在 TDMQ 内部做权限划分的最小单位，用户可以添加多个角色并为其赋予不同命名空间下的生产和消费权限。
   - **角色密钥**：选择 TDMQ 的角色密钥。TDMQ 的“密钥”是一种鉴权工具，用户可以通过在客户端中添加密钥来访问 TDMQ 进行消息的生产消费。密钥和角色一一对应，每种角色都有其对应的唯一密钥。
   - **访问地址**：必须为 VPC 内网访问地址。
<dx-alert infotype="notice" title="">
对应的 VPC 子网中必须有可用的 IP，且必须支持 DHCP。
</dx-alert>
6. 单击**下一步**，进行投递配置，配置项说明如下：
   - **投递的路径**：备份文件的投递路径前缀，不填写则默认保存在存储桶根路径，指定前缀必须以斜杠`/`为结尾。
7. 添加配置后，单击**确认**，即可看到函数已添加完成。如下图所示：
![](https://main.qcloudimg.com/raw/01131a9e6a8acb9492151a438803631b.png)
您可以对新创建的函数进行如下操作：
   - 单击**查看日志**，查看 TDMQ 消息备份的历史运行情况。当备份出现报错时，您还可以通过单击**查看日志**，快速跳转到云函数控制台查看日志错误详情。
   - 单击**编辑**，修改 TDMQ 消息备份规则。
   - 单击**删除**，删除不使用的 TDMQ 消息备份规则。



### 测试云函数 
1. 登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)。
2. 选择左侧“Topic管理”，选择地域、当前集群和命名空间。
3. 在“Topic管理”列表页，单击已关联的 Topic 主题右侧的**发送消息**。如下图所示：
![](https://main.qcloudimg.com/raw/c08f7fead0ca443e4be332f6cd2a5963.png)
4. 在弹出的对话框中输入消息内容。消息长度不超过64KB。
5. 单击**提交**，完成消息的发送。
6. 进入 COS 已关联桶详情页，例如 `scf-data-lake` 中已定义的**投递的路径**，查看是否有文件被创建。如有，则 TDMQ 消息备份成功。
