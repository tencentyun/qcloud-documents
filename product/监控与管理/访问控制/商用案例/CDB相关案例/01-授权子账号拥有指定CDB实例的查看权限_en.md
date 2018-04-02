### Authorizing a Sub-account with View Permission of the Specified CDB Instances

A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678) requires view permission of two CDB instances (instance IDs are cdb-1 and cdb-2 respectively) of the enterprise account CompanyExample.

Step 1: Create the following policy using policy syntax
```
 {
    "version": "2.0",
    "statement":
     {
         "effect": "allow",
         "action": "cdb:*",
         "resource": ["qcs::cdb::uin/12345678:instanceId/cdb-1", "qcs::cdb::uin/12345678:instanceId/cdb-2"]
     }
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Note: The sub-account Developer can only view the resources of instances with ID of cdb-1 and cdb-2 on the CDB query list page.


