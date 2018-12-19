A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678) requires full management permissions (creating, managing, and accessing COS buckets or objects) of the COS service under the enterprise account CompanyExample.

Solution A:

The enterprise account CompanyExample directly authorizes the preset policy QcloudCOSFullAccess to the sub-account Developer. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Step 1: Create the following policy using policy syntax
```
 {
    "version": "2.0",
    "statement":
     {
         "effect": "allow",
         "action": "cos:*",
         "resource": "*"
     }
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

