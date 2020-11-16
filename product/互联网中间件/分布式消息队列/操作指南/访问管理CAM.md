## CAM 基本概念

主账号通过给子账号绑定策略实现授权，策略设置可精确到 **[API，资源，用户/用户组，允许/拒绝，条件]** 维度。

#### 账户

- **主账号**：拥有腾讯云所有资源，可以任意访问其任何资源。
- **子账号**：包括子用户和协作者。
- **子用户**： 由主账号创建，完全归属于创建该子用户的主账号。
- **协作者**：本身拥有主账号身份，被添加作为当前主账号的协作者，则为当前主账号的子账号之一，可切换回主账号身份。
- **身份凭证**：包括登录凭证和访问证书两种，**登录凭证** 指用户登录名和密码，**访问证书** 指云 API 密钥（SecretId 和 SecretKey）。

#### 资源与权限

- **资源**：资源是云服务中被操作的对象，在 TDMQ 中，资源有环境、Topic、订阅等。
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

TDMQ 支持资源级授权，您可以指定子账号拥有特定资源的接口权限。

支持资源级授权的接口列表如下：

| API名                         | API描述          | 资源类型 | 资源六段式示例                                               |
| ----------------------------- | ---------------- | -------- | ------------------------------------------------------------ |
| CreateSubscription            | 创建订阅关系     | 订阅相关 | qcs::tdmq:$region:$account:topicName/$environmentId/$topicName |
| CreateTopic                   | 新增主题         | 主题相关 | qcs::tdmq:$region:$account:environmentId/$environmentId      |
| DeleteEnvironments            | 删除环境         | 环境相关 | qcs::tdmq:$region:$account:environmentId/$environmentIds     |
| DeleteSubscriptions           | 删除订阅关系     | 订阅相关 | qcs::tdmq:$region:$account:topicName/$topicSets.environmentId/$topicSets.topicName/$topicSets.subscriptionName |
| DeleteTopics                  | 删除主题         | 主题相关 | qcs::tdmq:$region:$account:topicName/$topicSets.environmentId/$topicSets.topicName |
| DescribeEnvironmentAttributes | 获取环境属性     | 环境相关 | qcs::tdmq:$region:$account:environmentId/$environmentId      |
| DescribeEnvironments          | 获取环境列表     | 环境相关 | qcs::tdmq:$region:$account:environmentId/$environmentId      |
| DescribeProducers             | 生产者列表       | 主题相关 | qcs::tdmq:$region:$account:topicName/$environmentId/$topicName |
| DescribeSubscriptions         | 查询消费订阅列表 | 订阅相关 | qcs::tdmq:$region:$account:topicName/$environmentId/$topicName |
| DescribeTopics                | 查询主题列表     | 主题相关 | qcs::tdmq:$region:$account:topicName/$environmentId/$topicName |
| ModifyEnvironmentAttributes   | 修改环境属性     | 环境相关 | qcs::tdmq:$region:$account:environmentId/$environmentId      |
| ModifyTopic                   | 修改主题         | 主题相关 | qcs::tdmq:$region:$account:topicName/$environmentId/$topicName |
| ResetMsgSubOffsetByTimestamp  | 消息回溯         | 订阅相关 | qcs::tdmq:$region:$account:topicName/$environmentId/$topicName |
| SendMsg                       | 发送消息         | 主题相关 | qcs::tdmq:$region:$account:topicName/$environmentId/$topicName |

## 不支持资源级授权的 API 列表

| API 名            | API 描述 | 资源六段式 |
| ----------------- | -------- |-------- |
| CreateEnvironment | 创建环境 |*|

## 授权方案示例

### TDMQ 全读写策略

授权一个子用户以 TDMQ 服务的完全管理权限（创建、管理等全部操作）。

```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
            "tdmq:*"
      ],
      "resource": "*",
      "effect": "allow"
    }
  ]
}
```

您也可以通过设置系统的 [全读写策略](https://console.cloud.tencent.com/cam/policy/createV2) 支持。

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)。
2. 在左侧菜单栏中，单击【[策略](https://console.cloud.tencent.com/cam/policy)】。
3. 在策略列表中，单击【新建自定义策略】。
4. 在选择创建策略方式的弹窗中，选择【按策略语法创建】。
5. 在模板类型中，搜索“TDMQ”，选择腾讯云消息队列 TDMQ 全读写访问权限【QcloudTDMQFullAccess】，单击【下一步】。
6. 单击【创建策略】。

### TDMQ 实例只读策略

授权单个 Topic 的只读权限。
```
   {
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "tdmq:Describe*"
            ],
            "resource": [
                "qcs::tdmq:$region:$account:topicName/$environmentId/$topicName" 
            ]
        }
    ]
   }
```

您也可以通过设置系统的 [只读策略](https://console.cloud.tencent.com/cam/policy/createV2) 支持。

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)
2. 在左侧菜单栏中，单击【[策略](https://console.cloud.tencent.com/cam/policy)】。
3. 在策略列表中，单击【新建自定义策略】。
4. 在选择创建策略方式的弹窗中，选择【按策略语法创建】。
5. 在模板类型中，搜索“TDMQ”，选择腾讯云消息队列 TDMQ 只读访问策略【QcloudTDMQReadOnlyAccess】，单击【下一步】。
6. 单击【创建策略】。
