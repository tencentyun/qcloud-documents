## CAM 基本概念

主账号通过给子账号绑定策略实现授权，策略设置可精确到 **[API，资源，用户/用户组，允许/拒绝，条件]** 维度。

#### 账户

- **主账号**：拥有腾讯云所有资源，可以任意访问其任何资源。
- **子账号**：包括子用户和协作者。
- **子用户**： 由主账号创建，完全归属于创建该子用户的主账号。
- **协作者**：本身拥有主账号身份，被添加作为当前主账号的协作者，则为当前主账号的子账号之一，可切换回主账号身份。
- **身份凭证**：包括登录凭证和访问证书两种，**登录凭证** 指用户登录名和密码，**访问证书** 指云 API 密钥（SecretId 和 SecretKey）。

#### 资源与权限

- **资源**：资源是云服务中被操作的对象，在 TDMQ CMQ 版中，资源有队列、主题等。
- **权限**：权限是指允许或拒绝某些用户执行某些操作。默认情况下，**主账号拥有其名下所有资源的访问权限**，而**子账号没有主账号下任何资源的访问权限**。
- **策略**：策略是定义和描述一条或多条权限的语法规范。**主账号**通过将**策略关联**到用户/用户组完成授权。

[单击查看更多 CAM 文档 >>](https://cloud.tencent.com/document/product/598/10583)

## 相关文档

| 目标                     | 链接                                                         |
| ------------------------ | ------------------------------------------------------------ |
| 了解策略和用户之间关系   | [策略管理](https://cloud.tencent.com/document/product/598/10601) |
| 了解策略的基本结构       | [策略语法](https://cloud.tencent.com/document/product/598/10603) |
| 了解还有哪些产品支持 CAM | [支持 CAM 的产品](https://cloud.tencent.com/document/product/598/10588) |

## 支持资源级授权的 API 列表

TDMQ CMQ 版支持资源级授权，您可以指定子账号拥有特定资源的接口权限。

支持资源级授权的接口列表如下：

| API 名                             | API 描述                 | 资源类型 | 资源六段式示例                                               |
| --------------------------------- | ----------------------- | -------- | ------------------------------------------------------------ |
| ModifyCmqTopicAttribute           | 修改 TDMQ CMQ 版主题属性         | 主题     | qcs::tdmq:${region}:uin/${uin}:topic/${topicName}            |
| CreateCmqSubscribe                | 创建 TDMQ CMQ 版订阅接口         | 主题     | qcs::tdmq:${region}:uin/${uin}:topic/${topicName}            |
| ModifyCmqSubscriptionAttribute    | 修改 TDMQ CMQ 版订阅属性         | 订阅     | qcs::tdmq:${region}:uin/${uin}:subscription/${topicName}/${subscriptionName} |
| RewindCmqQueue                    | 回溯 TDMQ CMQ 版队列             | 队列     | qcs::tdmq:${region}:uin/${uin}:queue/${queueName}            |
| ModifyCmqQueueAttribute           | 修改 TDMQ CMQ 版队列属性         | 队列     | qcs::tdmq:${region}:uin/${uin}:queue/${queueName}            |
| ClearCmqSubscriptionFilterTags    | 清空 TDMQ CMQ 版订阅者消息标签   | 订阅     | qcs::tdmq:${region}:uin/${uin}:subscription/${topicName}/${subscriptionName} |
| ClearCmqQueue                     | 清空 TDMQ CMQ 版消息队列中的消息 | 队列     | qcs::tdmq:${region}:uin/${uin}:queue/${queueName}            |
| DeleteCmqSubscribe                | 删除 TDMQ CMQ 版订阅             | 订阅     | qcs::tdmq:${region}:uin/${uin}:subscription/${topicName}/${subscriptionName} |
| DeleteCmqTopic                    | 删除 TDMQ CMQ 版主题             | 主题     | qcs::tdmq:${region}:uin/${uin}:topic/${topicName}            |
| UnbindCmqDeadLetter               | 解绑 TDMQ CMQ 版死信队列         | 队列     | qcs::tdmq:${region}:uin/${uin}:queue/${sourceQueueName}      |
| DescribeCmqDeadLetterSourceQueues | 枚举 TDMQ CMQ 版死信队列源队列   | 死信队列 | qcs::tdmq:${region}:uin/${uin}:dlq/${sourceQueueName}/${deadLetterQueueName} |
| DescribeCmqTopics                 | 枚举 TDMQ CMQ 版全量主题         | 主题     | qcs::tdmq:${region}:uin/${uin}:topic/${topicName}            |
| DescribeCmqSubscriptionDetail     | 查询 TDMQ CMQ 版订阅详情         | 主题     | qcs::tdmq:${region}:uin/${uin}:topic/${topicName}/${subscriptionName} |
| DescribeCmqQueues                 | 查询 TDMQ CMQ 版全量队列         | 队列     | qcs::tdmq:${region}:uin/${uin}:queue/${queueName}            |
| PublishCmqMsg                     | 发送 TDMQ CMQ 版主题消息         | 主题     | qcs::tdmq:${region}:uin/${uin}:topic/${topicName}            |
| SendCmqMsg                        | 发送 TDMQ CMQ 版消息             | 队列     | qcs::tdmq:${region}:uin/${uin}:queue/${queueName}            |
| DescribeCmqTopicDetail            | 查询 TDMQ CMQ 版主题详情         | 主题     | qcs::tdmq:${region}:uin/${uin}:topic/${topicName}qcs::tdmq:${region}:uin/${uin}:queue/${queueName} |
| DescribeCmqQueueDetail            | 查询 TDMQ CMQ 版队列详情         | 队列     | qcs::tdmq:${region}:uin/${uin}:queue/${queueName}            |
| DeleteCmqQueue                    | 删除 TDMQ CMQ 版队列             | 队列     | qcs::tdmq:${region}:uin/${uin}:queue/${queueName}            |

## 不支持资源级授权的 API 列表

| API 名         | API 描述        | 资源六段式 |
| -------------- | --------------- | ---------- |
| CreateCmqTopic | 创建 TDMQ CMQ 版主题     | *          |
| CreateCmqQueue | 创建 TDMQ CMQ 版队列接口 |   *          |

## 授权方案示例

### 全读写策略

以授权一个子用户以 TDMQ CMQ 版队列服务的完全管理权限（创建、管理等全部操作）为例。

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)。
2. 在左侧菜单栏中，单击**策略**。
3. 在策略列表中，单击**新建自定义策略**。
4. 在选择创建策略方式的弹窗中，选择**按策略生成器创建**。
5. 在编辑策略页面，单击右上角**导入策略语法**。
6. 在导入策略语法页面，搜索“TDMQ”，在搜索结果中勾选 QcloudTDMQFullAccess，单击**确定**。
7. 在编辑策略页面，单击**下一步**，填写策略名称和描述，选择您要关联的用户/用户组。
8. 单击**完成**，完成策略创建与授权。

### 资源只读策略

以授权单个队列服务的只读权限为例。

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)。
2. 在左侧菜单栏中，单击**策略**。
3. 在策略列表中，单击**新建自定义策略**。
4. 在选择创建策略方式的弹窗中，选择**按策略生成器创建**，填写策略信息。


   | 参数              | 说明                                                         |
   | ----------------- | ------------------------------------------------------------ |
   | 效果（Effect）    | 选择**允许**                                                 |
   | 服务（Service）   | 选择**消息队列 TDMQ (tdmq)**                                  |
   | 操作（Action）    | 选择**读操作**                                               |
   | 资源（Resource）  | 选择**特定资源**，单击**添加自定义资源六段式**<li>地域：选择资源所在地域</li><li>账户：系统自动填充</li><li>资源前缀：queue</li><li>填写您要授权的队列服务名称</li> |
   | 条件（Condition） | 仅当请求来自指定 IP 地址范围内时才允许访问指定操作             |

5. 单击**下一步**，填写策略名称和描述，选择您要关联的用户/用户组。
6. 单击**完成**，完成策略创建与授权。

