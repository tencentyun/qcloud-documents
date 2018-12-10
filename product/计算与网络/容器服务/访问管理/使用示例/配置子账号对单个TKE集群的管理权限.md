## 配置子账号对单个TKE集群的管理权限
您可以通过使用 CAM （Cloud Access Management，访问管理）策略让用户拥有在 TKE （Tencent Kubernetes Engine，容器服务）控制台中查看和使用特定资源的权限。该部分的示例能够使用户使用控制台的单个集群的策略。

### 配置对单个集群全读写权限
若您想为您的子账号仅拥有指定集群的全读写权限，您可以进入策略管理界面，通过策略语法的方式新建自定义策略，将以下策略绑定到指定的子用户。
```json
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "ccs:*"
            ],
            "resource": [
                "qcs::ccs:sh::cluster/cls-XXXXXXX", ## 替换成您想赋予权限的指定地域下的集群
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
                "cam:GetGroup"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
>注意：请替换成您想赋予权限的指定地域下的指定的集群ID。
如您需允许子账号进行集群的扩缩容，需要配置子账号用户支付权限。

### 配置对单个集群只读权限
若您想为您的子账号仅拥有指定集群的只读权限，您可以进入策略管理界面，通过策略语法的方式新建自定义策略，将以下策略绑定到指定的子用户。
```json
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "ccs:Describe*",
                "ccs:Check*"
            ],
            "resource": "qcs::ccs:gz::cluster/cls-1xxxxxx", ## 替换成您想赋予权限的指定地域下的集群
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
                "cam:GetGroup"
            ],
            "resource": "*"
        }
    ]
}
```


>注意：请替换成您想赋予权限的指定地域下的指定的集群ID。
