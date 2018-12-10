## 配置子账号对TKE服务的全读写或只读权限
您可以通过使用 CAM （Cloud Access Management，访问管理）策略让用户拥有在 TKE （Tencent Kubernetes Engine，容器服务）控制台中查看和使用特定资源的权限。该部分的示例能够使用户使用控制台部分权限的策略。

### 配置全读写权限

如果您想让用户拥有创建和管理 TKE 实例的权限，您可以对该用户使用名称为： QcloudCCSFullAccess 的策略。
您可以进入 策略管理界面，并在右边的全部服务中选择【容器服务】，就可以在图中位置找到该策略。
![Alt text][tkefullaccess]
策略如下：
```json
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "ccs:*"
            ],
            "resource": "*",
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
除配置集群的全读写权限外，建议同时配置镜像仓库的全读写权限。如需使用镜像仓库的触发器和自动构建功能，需额外配置容器服务-持续集成（CCB）的相关权限。
![Alt text][ccrfullaccess]
策略如下：
```json
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "ccr:*"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

### 配置只读权限


如果您想让用户拥有创建和管理 TKE 实例的权限，您可以对该用户使用名称为： QcloudCCSReadOnlyAccess 的策略。
您可以进入 策略管理界面，并在右边的全部服务中选择【容器服务】，就可以在图中位置找到该策略。
![Alt text][tkereadaccess]
策略如下：
```json
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "ccs:Describe*",
                "ccs:Check*"
            ],
            "resource": "*",
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
除配置集群的只读权限外，建议同时配置镜像仓库的只读权限。如需使用镜像仓库的触发器和自动构建功能，需额外配置容器服务-持续集成（CCB）的相关权限。
![Alt text][ccrreadaccess]
策略如下：
```json
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "ccr:pull"
            ],
            "resource": "qcs::ccr:::repo/*",
            "effect": "allow"
        },
        {
            "action": "ccr:GetUserRepositoryList",
            "resource": "qcs::ccr:::repo/*",
            "effect": "allow"
        }
    ]
}
```

[tkefullaccess]:https://main.qcloudimg.com/raw/92db8a4505eab7b570283d598b9b601f.png
[ccrfullaccess]:https://main.qcloudimg.com/raw/a4afbb82e7c0fca2db45c8b3fdfb87a1.png
[tkereadaccess]:https://main.qcloudimg.com/raw/111a99df581790d68393cc7930489107.png
[ccrreadaccess]:https://main.qcloudimg.com/raw/df7aeadbbf93bdf15c1b9abd824f0ebc.png
