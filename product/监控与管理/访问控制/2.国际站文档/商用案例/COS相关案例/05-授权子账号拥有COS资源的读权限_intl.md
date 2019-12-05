A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678) requires read-only permission (accessing COS buckets or objects and object list) of the COS service under the enterprise account CompanyExample.

Solution A:

The enterprise account CompanyExample directly authorizes the preset policy QcloudCOSReadOnlyAccess to the sub-account Developer. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Step 1: Create the following policy using policy syntax
```
 {
    "version": "2.0",
    "statement":
     {
         "effect": "allow",
         "action":  [
                    "cos:List*",
                    "cos:Get*",
                    "cos:Head*",
                    "cos:OptionsObject"
                ],
         "resource": "*"
     }
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

