### Authorizing a sub-account with operation permissions of VPN

A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678) requires view permission of all VPC resources in the VPC service under the enterprise account CompanyExample. But the sub-account is only allowed to add, delete, modify and view VPN.

Step 1: Create the following policy using policy syntax
```
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

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).


