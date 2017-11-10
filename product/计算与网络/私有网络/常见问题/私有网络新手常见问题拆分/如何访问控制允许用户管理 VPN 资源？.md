您好，该策略允许用户查看所有 VPC 资源，但只允许其对 VPN 进行增、删、改、查操作。详情查看 [操作指南](https://cloud.tencent.com/document/product/215/4956#.E6.93.8D.E4.BD.9C.E6.8C.87.E5.8D.97)。
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
