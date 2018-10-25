### Authorizing a sub-account with operation permissions of security groups

A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678) requires permissions of viewing and using security groups in CVM console under the enterprise account CompanyExample.

The following policy allows the sub-account to create and delete security groups in the CVM console.

Step 1: Create the following policy using policy syntax
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cvm:DeleteSecurityGroup",
                "cvm:CreateSecurityGroup"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

The following policy allows the sub-account to create, delete and modify security group policies in the CVM console.

Step 1: Create the following policy using policy syntax
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cvm:ModifySecurityGroupPolicy",
                "cvm:CreateSecurityGroupPolicy",
                "cvm:DeleteSecurityGroupPolicy"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

