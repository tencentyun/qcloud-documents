The enterprise account CompanyGranter (ownerUin is 12345678 and appId is 8000001) has an object Object1 located in the directory dir1 of the Bucket1 in Guangzhou region. And the sub-account of another enterprise account CompanyGrantee (ownerUin is 87654321) requires the read/write permission of Object1 above.

Here involves permission propagation.

Step 1: Enterprise account CompanyGrantee creates the following policy using policy syntax
```
 {
    "version": "2.0",
    "statement":
     {
         "effect": "allow",
         "action": "cos:*",
         "resource": "qcs::gz:cvm:uid/8000001:prefix//8000001/Bucket1/dir1/Object1"
     }
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Step 3: Enterprise account CompanyGranter authorizes Object1 to enterprise account CompanyGrantee by configuring Policy and ACL via the COS console. For more information, please see COS documentation.

