## VPC 的全读写策略
以下策略允许用户创建和管理 VPC。可向一组网络管理员关联此策略。Action 元素指定所有 VPC 相关 API。
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
## VPC 的只读策略
以下策略允许用户查询您的 VPC 及相关资源。但用户无法创建、更新或删除它们。
在控制台，操作一个资源的前提是可以查看该资源，所以建议您为用户开通 VPC 只读权限。

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

## 只允许子账号管理单个 VPC
以下策略允许用户看到所有 VPC，但只能操作 VPC A（假设 A 的 ID 是 vpc-d08sl2zr）及 A 下的网络资源（如子网、路由表等，不包括云服务器、数据库等），但不允许该用户管理其它 VPC。
该版本不支持**只让用户看到 A**，后续版本会支持。

```
{
    "version": "2.0",
    "statement": [
        {
            "action": "name/vpc:*",
            "resource": "*",
            "effect": "allow",
            "condition": {
                "string_equal_if_exist": {  //请按照条件判断，只允许管理符合条件的VPC
                    "vpc:vpc": [
                    "vpc-d08sl2zr"
                    ],
                    "vpc:accepter_vpc": [
                     "vpc-d08sl2zr"
                    ],
                     "vpc:requester_vpc": [
                     "vpc-d08sl2zr"
                    ]
                }
            }
        }
    ]
}
```

## 允许用户管理 VPC，但不允许操作路由表
以下策略允许用户读写 VPC 及其相关资源，但是不允许用户对路由表进行相关操作。
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
            "effect": "deny"
        }
    ]
}
```

## 允许用户管理 VPN 资源
该策略允许用户查看所有 VPC 资源，但只允许其对 VPN 进行增、删、改、查操作。

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
                "name/vpc:*UserGw*"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
