### Authorizing a sub-account with operation permissions of elastic cloud disk

A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678) requires permissions of creating/using cloud disk and viewing cloud disk information in CVM console under the enterprise account CompanyExample.

Solution A:

The enterprise account CompanyExample directly authorizes the preset policy QcloudCBSFullAccess to the sub-account Developer. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Step 1: Create the following policy using policy syntax
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cvm:CreateCbsStorages",
                "cvm:AttachCbsStorages",
                "cvm:DetachCbsStorages",
                "cvm:ModifyCbsStorageAttributes",
                "cvm:DescribeCbsStorages",
                "cvm:DescribeInstancesCbsNum",
                "cvm:RenewCbsStorage",
                "cvm:ResizeCbsStorage"
                ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Note: If the sub-account is not allowed to modify cloud disk properties, remove "cvm:ModifyCbsStorageAttributes" from the above-mentioned policy syntax.

