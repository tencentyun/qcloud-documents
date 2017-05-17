您的安全凭证使腾讯云中的服务可以识别您，并授予您对 腾讯云 资源 (例如您的 腾讯云 VPC、子网等 资源) 的无限制使用权限。利用 腾讯云 CAM 服务可在不共享您的安全凭证的情况下允许其他用户、服务和应用程序使用您的腾讯云VPC 资源。您可以通过向用户授予使用特定 腾讯云 EC2 API 操作的权限，选择允许完全使用或有限使用您的资源。有些 API 操作支持资源级权限，这些权限使您可以控制用户可以创建或修改的特定资源。

#### VPC 的全读写策略
以下策略允许用户创建和管理 VPC。可向一组网络管理员附加此策略。Action 元素指定所有VPC相关API。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/vpc:*"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
#### VPC 的只读策略
以下策略允许用户查询您的 VPC 及相关资源。但用户无法创建、更新或删除它们。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/vpc:Describe*",
                "name/vpc:Inquiry*",
                "name/vpc:Get*"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

#### 允许用户管理VPC,但是不允许用户操作路由表

以下策略允许用户读写VPC及其相关资源，但是不允许用户对路由表进行相关操作。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/vpc:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "name/vpc:AssociateRouteTable",
                "name/vpc:CreateRoute",
                "name/vpc:CreateRouteTable",
                "name/vpc:DeleteRoute",
                "name/vpc:DeleteRouteTable",
                "name/vpc:ModifyRouteTableAttribute"
            ],
            "resource": "*",
            "effect":"deny"
        }

    ]
}
```

#### 允许用户管理VPN资源
该策略允许用户查看所有VPC资源，但只允许其对VPN进行增、删、改、查操作。

```
{
    "version": "2.0",
    "statement": [
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
                "name/vpc:*Vpn*",
            ],
            "resource": "*",
            "effect": "allow"
        }

    ]
}
```
