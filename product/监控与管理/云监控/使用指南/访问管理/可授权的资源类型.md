## 自定义策略可授权资源类型

资源级权限指的是能够指定用户对哪些资源具有执行操作的能力。云监控告警策略、通知模板支持资源级权限，即表示针对支持资源级权限操作，您可以控制何时允许用户执行操作或是允许用户使用特定资源。访问管理 CAM 中可授权的资源类型如下：

| 资源类型           | 授权策略中的资源描述方法                   |
| :----------------- | :----------------------------------------- |
| 告警策略/cm-policy | `qcs::monitor::uin/:cm-policy/${policyId}` |
| 通知模板/cm-notice | `qcs::monitor::uin/:cm-notice/${noticeId}` |

下表将介绍当前支持资源级权限的告警策略、通知模板  API 操作，设置策略时，action 填入  API  操作名称就可以对单独 API 进行控制，设置 action 也可以使用`*`作为通配符。

### 支持资源级授权的 API 列表

| API 操作                   | API 描述              |
| :------------------------- | :-------------------- |
| DeleteAlarmPolicy          | 删除告警2.0策略       |
| ModifyAlarmPolicyCondition | 编辑告警策略触发条件  |
| ModifyAlarmPolicyInfo      | 编辑告警策略基本信息  |
| ModifyAlarmPolicyNotice    | 编辑告警2.0策略的通知 |
| ModifyAlarmPolicyStatus    | 修改告警策略状态      |
| ModifyAlarmPolicyTasks     | 编辑告警策略触发任务  |
| SetDefaultAlarmPolicy      | 设为默认告警策略      |
| DeleteAlarmNotices         | 删除告警通知          |
| ModifyAlarmNotice          | 编辑告警通知          |
| ModifyAlarmPolicyNotice    | 编辑告警2.0策略的通知 |
| DescribeAlarmPolicies      | 告警2.0策略列表       |
| DescribeAlarmPolicyQuota   | 查询告警策略配额      |
| DescribeAlarmNotice        | 获取告警通知详情      |
| DescribeAlarmNotices       | 查询告警通知列表      |

