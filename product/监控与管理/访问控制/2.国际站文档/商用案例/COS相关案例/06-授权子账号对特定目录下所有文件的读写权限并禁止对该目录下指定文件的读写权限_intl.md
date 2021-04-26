A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678 and appId is 8000001) requires read/write permission of all objects (excluding Object1) in the Bucket1's directory dir1 of the COS service in Shanghai region under the enterprise account CompanyExample.

Solution A:

Step 1: Create the following policy using policy syntax
```
 {
    "version": "2.0",
    "statement":
    [
     {
         "effect": "allow",
         "action": "cos:*",
         "resource": "qcs::cos:cn-east:uid/8000001:prefix//8000001/Bucket1/dir1/*"
     },
     {
         "effect": "deny",
         "action": "cos:*",
         "resource": "qcs::cos:cn-east:uid/8000001:prefix//8000001/Bucket1/dir1/Object1"
     }     
    ]
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Configure Policy and ACL via the COS console. For more information, please see the COS document.
