## 操作场景

您可以通过使用访问管理（Cloud Access Management，CAM）策略让用户拥有在容器服务（Tencent Kubernetes Engine，TKE）控制台中查看和使用特定资源的权限。本文档中的示例指导您在控制台中配置单个集群的策略。

## 操作步骤

### 配置对单个集群全读写权限

1. 登录 [CAM 控制台](https://console.cloud.tencent.com/cam/overview)。
2. 在左侧导航栏中，单击 [策略](https://console.cloud.tencent.com/cam/policy)，进入策略管理页面。
3. 单击**新建自定义策略**，选择 “[按策略语法创建](https://console.cloud.tencent.com/cam/policy/createV2)” 方式。
4. 选择 “空白模板” 类型，单击**下一步**。
5. 自定义策略名称，将 “编辑策略内容” 替换为以下内容。
```json
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "tke:*"
            ],
            "resource": [
                "qcs::tke:sh::cluster/cls-XXXXXXX",
                "qcs::cvm:sh::instance/*"
            ],
            "effect": "allow"
        },
        {
            "action": [
                "cvm:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "vpc:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "clb:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "monitor:*",
                "cam:ListUsersForGroup",
                "cam:ListGroups",
                "cam:GetGroup",
                "cam:GetRole"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

6. 在 “编辑策略内容” 中，将 `qcs::tke:sh::cluster/cls-XXXXXXX` 修改为您想赋予权限的指定地域下的集群。
例如，您需要为广州地域的 cls-69z7ek9l 集群赋予全读写的权限，将 `qcs::tke:sh::cluster/cls-XXXXXXX` 修改为 `"qcs::tke:gz::cluster/cls-69z7ek9l"`。
<dx-alert infotype="notice" title="">
请替换成您想赋予权限的指定地域下的集群 ID。如果您需要允许子账号进行集群的扩缩容，还需要配置子账号用户支付权限。
</dx-alert>
7. 单击**创建策略**，即可完成对单个集群全读写权限的配置。


### 配置对单个集群只读权限

1. 登录 [CAM 控制台](https://console.cloud.tencent.com/cam/overview)。
2. 在左侧导航栏中，单击 [策略](https://console.cloud.tencent.com/cam/policy)，进入策略管理页面。
3. 单击**新建自定义策略**，选择 “[按策略语法创建](https://console.cloud.tencent.com/cam/policy/createV2)” 方式。
4. 选择 “空白模板” 类型，单击**下一步**。
5. 自定义策略名称，将 “编辑策略内容” 替换为以下内容。
```json
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "tke:Describe*",
                "tke:Check*"
            ],
            "resource": "qcs::tke:gz::cluster/cls-1xxxxxx",
            "effect": "allow"
        },
        {
            "action": [
                "cvm:Describe*",
                "cvm:Inquiry*"
            ],
            "resource": "*",
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
                "clb:Describe*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "effect": "allow",
            "action": [
                "monitor:*",
                "cam:ListUsersForGroup",
                "cam:ListGroups",
                "cam:GetGroup",
                "cam:GetRole"
            ],
            "resource": "*"
        }
    ]
}
```

6. 在 “编辑策略内容” 中，将 `qcs::tke:gz::cluster/cls-1xxxxxx` 修改为您想赋予权限的指定地域下的集群。例如，您需要为北京地域的 cls-19a7dz9c 集群赋予只读的权限，将 `qcs::tke:gz::cluster/cls-1xxxxxx` 修改为 `qcs::tke:bj::cluster/cls-19a7dz9c`。
7. 单击**创建策略**，即可完成对单个集群只读权限的配置。




