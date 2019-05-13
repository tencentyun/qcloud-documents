## ES CAM 简介
访问管理（Cloud Access Management，CAM）是腾讯云提供的 Web 服务，主要用于帮助用户安全管理腾讯云账户下的资源的访问权限。用户可以通过 CAM 创建、管理和销毁用户(组)，并使用身份管理和策略管理控制其他用户使用腾讯云资源的权限，CAM 策略的详细信息及使用请参见 [CAM 策略](https://cloud.tencent.com/document/product/598/10601) 。  

## ES CAM 策略
### 通用权限策略
ES 默认提供了两种通用策略：
- 全读写策略 QcloudElasticsearchServiceFullAccess，可以让用户拥有创建和管理 ES 所有集群实例的权限。 
- 只读策略 QcloudElasticsearchServiceReadOnlyAccess， 可以让用户拥有查看 ES 集群实例的权限，但是不具有创建、更新、删除等操作的权限。  

您可以登录 [策略管理界面](https://console.cloud.tencent.com/cam/policy)，在“服务类型”中选择“Elasticsearch Service”，在列表中会显示默认策略，可对需要授权的账号进行绑定。
![](https://main.qcloudimg.com/raw/8f7edd89a348ea482c3e401b160b9339.png)
如果默认策略不能满足需求，可以单击【新建自定义策略】自定义授权。

### 自定义权限策略

ES 可授权的资源类型如下：

| 资源类型 |资源描述 |
| -------- | -------------- |
| instance | `qcs::es:$region:$account:instance/*` |

各 API 支持资源级权限访问控制详情如下：

| 接口名 | 描述 | 是否关联资源 | 资源描述 |
| ---|---|---|--- |
| 获取集群列表、单个集群信息 | DescribeInstances| 否 |  `*` |
| 创建集群 | CreateInstance| 否 |  `*` |
| 更新集群 | UpdateInstance| 是| `qcs::es:${Region}:uin/${ownerUin}:instance/${instanceId}` |
| 重启集群 | RestartInstance| 是| `qcs::es:${Region}:uin/${ownerUin}:instance/${instanceId}` |
| 删除集群 | DeleteInstance| 是|  `qcs::es:${Region}:uin/${ownerUin}:instance/${instanceId}` |
 
支持区域如下：

| 区域名称 | 区域 ID |
| :-------- | -------------- |
| 广州 | `ap-guangzhou` |

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

- Action：替换成要允许或拒绝的操作。
- Resource：替换成要授权的具体资源。
- Effect：替换成允许或拒绝。

ES 目前支持除了 DescribeInstances 接口之外的其他操作接口来访问控制管理，您可以将账号下某个集群的更新、重启、删除等操作赋予某个子账号进行管理。

#### 自定义权限示例
授予某账号指定集群更新操作权限，策略语法如下：
获取集群列表的接口`DescribeInstances`目前不支持关联资源，需要将该接口中的`resource`配置为`*`。
```
{
    "version": "2.0",
    "statement": [
    	 {
            "action": [
                "es:Describe*"
            ],
            "resource": [
                "*"
            ],
            "effect": "allow"
        },
        {
            "action": [
                "vpc:Describe*",
                "vpc:Inquiry*",
                "vpc:Get*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "monitor:*",
                "cam:ListUsersForGroup",
                "cam:ListGroups",
                "cam:GetGroup"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "es:Update*"
            ],
            "resource": [
                "qcs::es:ap-guangzhou:uin/$uin:instance/$instanceID"
            ],
            "effect": "allow"
        }
    ]
}
```
