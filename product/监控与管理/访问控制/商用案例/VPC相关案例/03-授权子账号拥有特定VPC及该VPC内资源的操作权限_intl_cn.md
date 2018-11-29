### 授权子账号拥有特定VPC及该VPC内资源的操作权限

企业帐号CompanyExample（ownerUin为12345678）下有一个子账号Developer，该子账号需要拥有对企业帐号CompanyExample的VPC服务的特定VPC（id是vpc-id1）及该VPC下的网络资源（如子网、路由表等，不包括云主机、数据库等）的操作权限。

step1：通过策略语法方式创建以下策略
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
step2：将该策略授权给子账号。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。