### Authorizing a sub-account with all the permissions of the COS resources

A sub-account Developer under the enterprise account CompanyExample requires all the permissions of the COS resources under this enterprise account.

Solution A:

The enterprise account CompanyExample directly authorizes the preset policy QcloudCOSFullAccess to the sub-account Developer. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Step 1: Create the following policy through policy syntax.

```
{
    "version": "2.0",
    "statement":
     {
         "effect": "allow",
         "action": "name/cos:*"
         "resource": "*"
     }
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

### Cross-account access permission and public read/write permissions

For more information, please see COS documentation.
