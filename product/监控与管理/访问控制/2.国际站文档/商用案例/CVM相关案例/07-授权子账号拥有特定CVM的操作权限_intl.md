### Authorizing a sub-account with operation permissions of specific CVM

A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678) requires operation permissions of the specific CVM with ID ins-1 in Guangzhou region under the enterprise account CompanyExample.

Step 1: Create the following policy using policy syntax
```
{
    "version": "2.0",
    "statement": [
        {
            "action": "cvm:*",
            "resource": "qcs::cvm:gz::instance/ins-1",
            "effect": "allow"
        }
    ]
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

