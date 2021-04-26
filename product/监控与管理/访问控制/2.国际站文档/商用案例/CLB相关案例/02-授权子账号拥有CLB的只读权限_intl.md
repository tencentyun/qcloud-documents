### Authorizing a sub-account with read-only permission of CLB

A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678) requires read-only permission of CLB service under the enterprise account CompanyExample, but the sub-account is not allowed to create, update, or delete CLBs.

Solution A:

The enterprise account CompanyExample directly authorizes the preset policy QcloudCLBReadOnlyAccess to the sub-account Developer. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Step 1: Create the following policy using policy syntax
```
 {
    "version": "2.0",
    "statement":
     {
         "effect": "allow",
         "action": "clb:Describe*",
         "resource": "*"
     }
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

