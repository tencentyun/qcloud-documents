### Authorizing a sub-account with operation permissions of CVM in specific region

A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678) requires operation permissions of all CVMs in Guangzhou region under the enterprise account CompanyExample.

Step 1: The enterprise account CompanyExample directly authorizes the preset policy QcloudCVMReadOnlyAccess to the sub-account Developer. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Step 2: Create the following policy using policy syntax
```
{
    "version": "2.0",
    "statement": [
        {
            "action": "cvm:*",
            "resource": "qcs::cvm:gz::*",
            "effect": "allow"
        }
    ]
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

