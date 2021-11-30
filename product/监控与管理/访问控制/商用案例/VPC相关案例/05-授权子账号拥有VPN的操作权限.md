
企业帐号 CompanyExample（ownerUin 为 12345678）下有一个子账号 Developer，该子账号需要拥有对企业帐号 CompanyExample 的 VPC 服务的查看所有 VPC 资源，但只允许其对 VPN 进行增、删、改、查操作的权限。

步骤1：通过策略语法方式创建以下策略。
```json
{
    "version": "2.0",
    "statement": [
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
                "vpc:*Vpn*",
                "vpc:*UserGw*"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
步骤2：将该策略授权给子账号。授权方式请参考 [授权管理](https://cloud.tencent.com/document/product/378/8961)。



