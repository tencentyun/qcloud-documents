### Authorizing a sub-account with operation permissions of specific VPC and resources within it

A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678) requires operation permissions of the specific VPC (ID is vpc-id1) and relevant resources (such as subnets, routing tables, but CVM and database are excluded) of the VPC service under the enterprise account CompanyExample.

Step 1: Create the following policy using policy syntax
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

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).
