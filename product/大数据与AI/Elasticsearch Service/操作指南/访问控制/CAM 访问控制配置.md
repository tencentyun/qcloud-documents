## ES CAM 访问管理简介
访问管理（CAM，Cloud Access Management）是腾讯云提供的一套 Web 服务，它主要用于帮助客户安全管理腾讯云账户下的资源的访问权限。通过 CAM，您可以创建、管理和销毁用户(组)，并通过身份管理和策略管理控制哪些人（子账号、协作者账号）可以使用哪些腾讯云资源。有关 CAM 策略的更多相关基本信息及使用，请参见 CAM [策略](https://cloud.tencent.com/document/product/598/10601) 文档。  

## ES CAM 配置示例
### 通用权限策略
腾讯云 ES 默认提供了两种通用策略：
- 全读写策略 QcloudElasticsearchServiceFullAccess，可以让用户拥有创建和管理 ES 所有集群实例的权限； 
- 只读策略 QcloudElasticsearchServiceReadOnlyAccess， 可以以让用户拥有查看 ES 集群实例的权限，但是不具有创建、更新、删除等操作的权限。  

您可以进入 [策略管理界面](https://console.cloud.tencent.com/cam/policy)，并在右边的全部服务中选择【Elasticsearch】，就可以在列表找到默认策略，对需要授权的账号进行绑定。
![进入访问控制](https://main.qcloudimg.com/raw/93b98ca018d0343aa264214a3e166457.png)  
![查找Elasticsearch预置策略](https://main.qcloudimg.com/raw/550cacf74e6af49583e9e6586164c88c.png) 

如果默认策略不能满足需求，可以参考以下步骤，创建自定义策略。
### 自定义权限策略

ES 可授权的资源类型如下：  

| 资源类型 |资源描述 |
| :-------- | -------------- |
| instance | `qcs::es:$region:$account:instance/*` |

下表是各 API 支持资源级权限访问控制详情 

| 接口名 | 描述 | 是否关联资源 | 资源描述 |
| ---|---|---|--- |
| 获取集群列表、单个集群信息 | DescribeInstances| 否 |  `*` |
| 创建集群 | CreateInstance| 否 |  `*` |
| 更新集群 | UpdateInstance| 是| `qcs::es:${Region}:uin/${ownerUin}:instance/${instanceId}` |
| 重启集群 | RestartInstance| 是| `qcs::es:${Region}:uin/${ownerUin}:instance/${instanceId}` |
| 删除集群 | DeleteInstance| 是|  `qcs::es:${Region}:uin/${ownerUin}:instance/${instanceId}` |
 
支持的区域：  

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

- Action 请替换成您要允许或拒绝的操作。
- Resource 请替换成您要授权的具体资源。
- Effect 请替换成允许或拒绝。

腾讯云 ES 目前支持除了 DescribeInstance 接口之外其他操作资源级别的访问控制管理，您可以将账号下某个集群的更新、重启、删除等操作赋予某个子账号进行管理。

#### 授予某账号指定集群更新操作权限

策略语法如下：
获取集群列表的接口 `DescribeInstances` 目前不支持关联资源，需要对该接口在 `resource`的地方配置为 `*`。
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
