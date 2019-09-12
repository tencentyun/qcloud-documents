### Authorizing a sub-account with all the permissions of VPC

A sub-account Developer under the enterprise account CompanyExample requires all the read/write permissions of the VPC resources under this enterprise account.

Solution A:

The enterprise account CompanyExample directly authorizes the preset policy QcloudVPCFullAccess to the sub-account Developer. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Step 1: Create the following policy through policy syntax.

```
{
    "version": "2.0",
    "statement":
    {
        "action": "name/vpc:*",
        "resource": "*",
        "effect": "allow"
    }
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

### Authorizing a sub-account with read-only permission of VPC

A sub-account Developer under the enterprise account CompanyExample requires the read-only permission of all the VPC resources under this enterprise account.

Solution A:

The enterprise account CompanyExample directly authorizes the preset policy QcloudVPCReadOnlyAccess to the sub-account Developer. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Step 1: Create the following policy through policy syntax.
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

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

### Authorizing a sub-account to manage VPC rather than working with the routing table

A sub-account Developer under the enterprise account CompanyExample requires to manage all the VPC resources, but not work with the routing table under this enterprise account.

Step 1: Create the following policy through policy syntax.

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

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).
