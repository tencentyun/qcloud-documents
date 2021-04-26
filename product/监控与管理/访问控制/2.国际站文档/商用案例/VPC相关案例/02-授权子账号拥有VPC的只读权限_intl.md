### Authorizing a sub-account with read-only permission of VPC

A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678) requires read-only permission (querying VPC and relevant resources) of VPC service under the enterprise account CompanyExample, but the sub-account is not allowed to create, update, or delete VPCs.

Solution A:

The enterprise account CompanyExample directly authorizes the preset policy QcloudVPCReadOnlyAccess to the sub-account Developer. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Step 1: Create the following policy using policy syntax
```
{
    "version": "2.0",
    "statement": 
        {
            "action": [
                "vpc:Describe*",
                "vpc:Inquiry*",
                "vpc:Get*"
            ],
            "resource": "*",
            "effect": "allow"
        }
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).


