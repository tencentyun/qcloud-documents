
## 策略语法
创建自定义策略流程可参考 CAM 的 [创建自定义策略](https://cloud.tencent.com/document/product/598/37739)。SCF 的策略语法遵循 CAM 的 [语法结构](https://cloud.tencent.com/document/product/598/10604) 和 [资源描述方式](https://cloud.tencent.com/document/product/598/10606)，策略语法以 JSON 格式为基础，所有资源均可采用下述的六段式描述方式，示例如下：

```
qcs::scf:region:uin/uin—id:namespace/namespace-name/function/function-name
```

>! 在配置策略语法时，还需要配合使用 monitor 相关的接口以获得账号下的监控信息，使用方法请参考 [策略示例](#policygen)。

## 策略示例[](id:policygen)
```
{	 
        "version":"2.0", 
        "statement": 
        [ 
           { 
              "effect":"allow", 
              "action":
              [
                "scf:ListFunctions",
                "scf:GetAccountSettings",
                "monitor:*"
              ], 
              "resource":["*"]  
           }, 
          { 
             "effect": "allow",
             "action": 
             [
                "scf:DeleteFunction",
                "scf:CreateFunction",
                "scf:InvokeFunction",
                "scf:UpdateFunction",
                "scf:GetFunctionLogs",
                "scf:SetTrigger",
                "scf:DeleteTrigger",
                "scf:GetFunction",
                "scf:ListVersion"
            ],
            "resource": 
            [
                "qcs::scf:gz:uin/******:namespace/default/function/Test1",
                "qcs::scf:gz:uin/******:namespace/default/function/Test2"
            ]
         }
      ] 
} 
```
- 操作（action）为需要关联资源的操作时，resource 定义为`*`，表示关联所有资源。
- 操作（action）为不需要关联资源的操作时，resource 都需要定义为`*`。
- 该示例可以实现子账号拥有主账号下某些函数的操作权限，resource 中的资源描述为主账号下的某个函数。

## 指定条件
访问策略语言可使您在授予权限时指定条件。例如，限制用户访问来源或限制授权时间等。下面列出了目前支持的条件操作符列表、通用的条件键和示例等信息。

<table>
<thead>
<tr>
<th style="width:20%">条件操作符</th>
<th style="width:15%">含义</th>
<th style="width:15%">条件名</th>
<th style="width:50%">示例</th>
</tr>
</thead>
<tbody><tr>
<td>ip_equal</td>
<td>IP 等于</td>
<td>qcs:ip</td>
<td><code>{"ip_equal":{"qcs:ip ":"10.121.2.0/24"}}</code></td>
</tr>
<tr>
<td>ip_not_equal</td>
<td>IP 不等于</td>
<td>qcs:ip</td>
<td><code>{"ip_not_equal":{"qcs:ip ":["10.121.1.0/24", "10.121.2.0/24"]}}</code></td>
</tr>
<tr>
<td>date_not_equal</td>
<td>时间不等于</td>
<td>qcs:current_time</td>
<td><code>{"date_not_equal":{"qcs:current_time":"2016-06-01T00:01:00Z"}}</code></td>
</tr>
<tr>
<td>date_greater_than</td>
<td>时间大于</td>
<td>qcs:current_time</td>
<td><code>{"date_greater_than":{"qcs:current_time":"2016-06-01T00:01:00Z"}}</code></td>
</tr>
<tr>
<td>date_greater_than_equal</td>
<td>时间大于等于</td>
<td>qcs:current_time</td>
<td><code>{"date_greater_than_equal":{"qcs:current_time":"2016-06-01T00:01:00Z"}}</code></td>
</tr>
<tr>
<td>date_less_than</td>
<td>时间小于</td>
<td>qcs:current_time</td>
<td><code>{"date_less_than":{"qcs:current_time":"2016-06-01T 00:01:00Z"}}</code></td>
</tr>
<tr>
<td>date_less_than_equal</td>
<td>时间小于等于</td>
<td>qcs:current_time</td>
<td><code>{"date_less_than":{"qcs:current_time":"2016-06-01T 00:01:00Z"}}</code></td>
</tr>
<tr>
<td>date_less_than_equal</td>
<td>时间小于等于</td>
<td>qcs:current_time</td>
<td><code>{"date_less_than_equal":{"qcs:current_time":"2016-06-01T00:01:00Z"}}</code></td>
</tr>
</tbody></table>

- 限制来访 IP 为 `10.121.2.0/24` 网段内。如下所示：
```json
"ip_equal":{"qcs:ip ":"10.121.2.0/24"}
```
- 限制来访 IP 为 `101.226.\*\*\*.185` 和 `101.226.\*\*\*.186`。如下所示：
```json
"ip_equal": {
    "qcs:ip": [
      "101.226.***.185",
      "101.226.***.186"
    ]
}
```

## 用户策略更新说明[](id:Strategy)
SCF 于2020年4月完善了预设策略权限，针对预设策略 `QcloudSCFFullAccess` 和 `QcloudSCFReadOnlyAccess` 完成修改，针对配置角色 `SCF_QcsRole` 添加了 `QcloudAccessForScfRole` 策略。详情如下：
- 预设策略 QcloudSCFFullAccess 当前权限如下：

``` json
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "scf:*",
                "tag:*",
                "cam:DescribeRoleList",
                "cam:GetRole",
                "cam:ListAttachedRolePolicies",
                "apigw:DescribeServicesStatus",
                "apigw:DescribeService",
                "apigw:DescribeApisStatus",
                "cmqtopic:ListTopicDetail",
                "cmqqueue:ListQueueDetail",
                "cmqtopic:GetSubscriptionAttributes",
                "cmqtopic:GetTopicAttributes",
                "cos:GetService",
                "cos:HeadBucket",
                "cos:HeadObject",
                "vpc:DescribeVpcEx",
                "vpc:DescribeSubnetEx",
                "cls:getTopic",
                "cls:getLogset",
                "cls:listLogset",
                "cls:listTopic",
                "ckafka:List*",
                "ckafka:Describe*",
                "ckafka:ListInstance",
                "monitor:GetMonitorData",
                "monitor:DescribeBasicAlarmList",
                "monitor:DescribeBaseMetrics",
                "monitor:DescribeSortObjectList",
                "monitor:DescribePolicyConditionList",
                "cdb:DescribeDBInstances"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
- 预设策略 QcloudSCFReadOnlyAccess 当前权限如下：

``` json
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "scf:Get*",
                "scf:List*",
                "ckafka:List*",
                "ckafka:Describe*",
                "monitor:GetMonitorData",
                "monitor:DescribeBasicAlarmList",
                "monitor:DescribeBaseMetrics",
                "monitor:DescribeSortObjectList",
                "cam:GetRole",
                "cam:ListAttachedRolePolicies",
                "vpc:DescribeVpcEx",
                "vpc:DescribeSubnetEx",
                "cls:getLogset",
                "cls:getTopic",
                "cls:listTopic",
                "apigw:DescribeService",
                "cmqtopic:GetTopicAttributes",
                "cmqtopic:GetSubscriptionAttributes",
                "cos:HeadBucket",
                "cos:GetService",
                "cos:GetObject"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
- 预设策略 QcloudAccessForScfRole 当前权限如下：

``` json
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cos:GetBucket*",
                "cos:HeadBucket",
                "cos:PutBucket*",
                "apigw:*",
                "cls:*",
                "cos:List*",
                "cos:Get*",
                "cos:Head*",
                "cos:OptionsObject",
                "cmqqueue:*",
                "cmqtopic:*",
                "ckafka:List*",
                "ckafka:Describe*",
                "ckafka:AddRoute",
                "ckafka:CreateRoute"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
预设策略 QcloudAccessForScfRole 具备以下功能：
 - 配置 COS 对象存储触发器时，向 Bucket 配置中写入触发配置信息。 
 - 读取 COS 对象存储 Bucket 中的触发器配置信息。 
 - 在使用 COS 对象存储更新代码时，从 Bucket 完成代码 zip 包的读取操作。 
 - 配置 API 网关触发器时，完成 API 网关的服务、API 创建以及服务发布等操作。 
 - 配置 Ckafka 触发器时，完成创建消费者操作。 
