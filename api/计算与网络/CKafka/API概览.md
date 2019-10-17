## 主题相关接口
| 接口功能 | Action ID | 功能描述|
|---------|---------|---------|
| [创建主题](https://cloud.tencent.com/document/product/597/10096) | CreateTopic| 用于在消息队列 CKafka 实例下创建主题。|
| [修改主题属性](https://cloud.tencent.com/document/product/597/10098)  | SetTopicAttributes| 用于在消息队列 CKafka 实例下修改主题属性。|
| [删除主题](https://cloud.tencent.com/document/product/597/10099) | DeleteTopic | 用于在消息队列 CKafka 实例下删除主题。|
| [增加分区](https://cloud.tencent.com/document/product/597/10100) | AddPartition | 用于用户增加主题中的分区。|
| [获取主题列表](https://cloud.tencent.com/document/product/597/10101) | ListTopic | 用于用户获取消息队列 CKafka 实例的主题列表。|
| [获取主题属性](https://cloud.tencent.com/document/product/597/10102) | GetTopicAttributes | 用于获取消息队列 CKafka 实例的主题属性。|
| [设置消息转发](https://cloud.tencent.com/document/product/597/17451) | SetForward | 用于给消息队列 CKafka 主题配置转发规则。|


## 实例相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| [获取实例列表](https://cloud.tencent.com/document/product/597/10093) | ListInstance | 用于在用户账户下获取消息队列 CKafka 实例列表。|
| [获取实例属性](https://cloud.tencent.com/document/product/597/10094)  | GetInstanceAttributes|用于获取某个已创建实例属性。|
| [设置实例属性](https://cloud.tencent.com/document/product/597/10095) | SetInstanceAttributes|用于设置消息队列 CKafka 实例属性。|
| [查询消费分组信息](https://cloud.tencent.com/document/product/597/18339) | ListConsumerGroup| 用于在用户账户下获取消息队列 CKafka 消费分组信息。|
| [查询消费分组信息（精简版）](https://cloud.tencent.com/document/product/597/30028)| ListGroup | 用于在用户账户下获取消息队列 CKafka 消费分组信息，该接口为精简版接口，返回消费分组信息较少，可以调用 GetGroupInfo 查询消费分组详细信息。|
| [获取消费分组信息](https://cloud.tencent.com/document/product/597/30029) | GetGroupInfo | 用于在用户账户下获取消息队列 CKafka 消费分组详细信息。|
| [获取消费分组 offset](https://cloud.tencent.com/document/product/597/30030) | GetGroupOffsets | 用于在用户账户下获取消息队列 CKafka 消息分组 offset。|
| [设置消费分组 offset](https://cloud.tencent.com/document/product/597/30058) | SetGroupOffsets| 用于在用户账户下设置消息队列 CKafka 实例某个消费分组 offset。|


## 访问控制相关接口
| 接口功能 | Action ID | 功能描述|
|---------|---------|---------|
| [增加主题白名单](https://cloud.tencent.com/document/product/597/10103) | AddTopicIpwhitelist | 用于增加主题中的 IP 白名单。|
| [删除主题白名单](https://cloud.tencent.com/document/product/597/10104) | DeleteTopicIpwhitelist | 用于删除主题中的 IP 白名单。|

## ACL 策略相关接口
>?ACL 策略目前处于灰度测试阶段，如需要在控制台试用，请通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 的方式开通白名单。

| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| [添加用户](https://cloud.tencent.com/document/product/597/32983) | AddUser | 用于为实例添加用户。|
| [删除用户](https://cloud.tencent.com/document/product/597/32984) | DeleteUser | 用于为实例删除用户。|
| [修改密码](https://cloud.tencent.com/document/product/597/32985) | ModifyPassword | 用于为用户修改密码。|
| [枚举用户信息](https://cloud.tencent.com/document/product/597/32986) | ListUser | 用于枚举出所有的用户信息。|
| [添加 ACL 策略](https://cloud.tencent.com/document/product/597/32987) | AddAcl | 用于为实例的用户添加 ACL 策略。|
| [删除 ACL 策略](https://cloud.tencent.com/document/product/597/32988) | DeleteAcl | 用于为实例的用户删除 ACL 策略。
| [枚举 ACL 策略](https://cloud.tencent.com/document/product/597/32989) | ListAcl | 用于为实例的用户删除 ACL 策略。|




