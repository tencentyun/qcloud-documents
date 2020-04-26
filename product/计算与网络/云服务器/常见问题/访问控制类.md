### 如何创建自定义策略？

若预设策略不能满足您的需求，您可以创建自定义策略。
自定义策略的语法如下：

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "Action"
            ],
            "resource": "Resource",
            "effect": "Effect"
        }
    ]
}
```

- Action 请替换成您要允许或拒绝的操作。
- Resource 请替换成您要授权的具体资源。
- Effect 请替换成允许或拒绝。

### 如何进行 CVM 的只读策略配置？

当您想让用户拥有查询 CVM 实例的权限，但是不具有创建、删除、开关机的权限，您可以对该用户使用名称为：QcloudCVMInnerReadOnlyAccess 的策略。

登录访问管理控制台，在 [策略管理](https://console.cloud.tencent.com/cam/policy) 界面搜索**云服务器**，可快速找到该策略。

策略语法如下：

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:Describe*",
                "name/cvm:Inquiry*"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

以上策略通过**让用户对如下操作具有操作权限**来达到目的：

- CVM 中所有以单词 "Describe" 开头的所有操作。
- CVM 中所有以单词 "Inquiry" 开头的所有操作。

### 如何进行 CVM 相关资源的只读策略配置？

当您想让用户只拥有查询 CVM 实例及相关资源（VPC、CLB）的权限，但不允许该用户拥有创建、删除、开关机等操作的权限，您可以对该用户使用名称为：QcloudCVMReadOnlyAccess 的策略。

登录访问管理控制台，在 [策略管理](https://console.cloud.tencent.com/cam/policy) 界面搜索**云服务器**，可快速找到该策略。

策略语法如下：

```
 {
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:Describe*",
                "name/cvm:Inquiry*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "name/vpc:Describe*",
                "name/vpc:Inquiry*",
                "name/vpc:Get*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "name/clb:Describe*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "effect": "allow",
            "action": "name/monitor:*",
            "resource": "*"
        }
    ]
}
```

以上策略通过**让用户分别对如下操作具有操作权限**来达到目的：

- CVM 中所有以单词 "Describe" 开头的所有操作和所有以单词 "Inquiry" 开头的所有操作。
- VPC 中所有以单词 "Describe" 开头的所有操作、所有以单词 "Inquiry" 开头的所有操作和所有以单词 "Get" 开头的所有操作。
- CLB 中所有以单词 "Describe" 开头的所有操作。
- Monitor 中所有的操作。

