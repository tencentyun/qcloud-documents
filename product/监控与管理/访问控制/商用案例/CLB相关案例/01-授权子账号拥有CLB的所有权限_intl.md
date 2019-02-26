### Authorizing a sub-account with all permissions of CLB

A sub-account Developer of the enterprise account CompanyExample (ownerUin is 12345678) requires full management permissions (creating, managing, ordering and paying for CLB) of the CLB service of enterprise account CompanyExample.

Solution A:

The enterprise account CompanyExample directly authorizes the preset policies QcloudCLBFullAccess and QcloudCLBFinanceAccess to the sub-account Developer. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Step 1: Create the following policy using policy syntax
```
{
    "version": "2.0",
    "statement":[
         {
             "effect": "allow",
             "action": "clb:*",
             "resource": "*"
         },
         {
                "effect": "allow",
                "action": "finance:*",
                "resource": "qcs::clb:::*"
         }
    ]
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).


