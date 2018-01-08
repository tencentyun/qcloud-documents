### Authorizing a sub-account with all permissions of CVM

A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678) requires full management permissions (creating, managing, ordering and paying for CVM) of the CVM service under the enterprise account CompanyExample.

Solution A:

The enterprise account CompanyExample directly authorizes the preset policies QcloudCVMFullAccess and QcloudCVMFinanceAccess to the sub-account Developer. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Step 1: Create the following policy using policy syntax
```
{
    "version": "2.0",
    "statement":[
         {
             "effect": "allow",
             "action": "cvm:*",
             "resource": "*"
         },
         {
                "effect": "allow",
                "action": "finance:*",
                "resource": "qcs::cvm:::*"
         }
    ]
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).


