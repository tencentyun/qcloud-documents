
企业帐号 CompanyExample（ownerUin 为 12345678）下有一个子账号 Developer，该子账号需要拥有对企业帐号 CompanyExample 的 VPC 服务的特定 VPC（id 是 vpc-id1）及该 VPC 下的网络资源（如子网、路由表等，不包括云主机、数据库等）的操作权限。

步骤1：通过策略语法方式创建以下策略。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": "vpc:*",
            "resource": "*",
            "effect": "allow",
            "condition": {
                "string_equal_if_exist": {
                    "vpc:vpc": [
                    "vpc-id1"
                    ],
                    "vpc:accepter_vpc": [
                     "vpc-id1"
                    ],
                     "vpc:requester_vpc": [
                     "vpc-id1"
                    ]
                }
            }
        }
    ]
}
```
步骤2：将该策略授权给子账号。授权方式请参考 [授权管理](https://cloud.tencent.com/document/product/378/8961)。
