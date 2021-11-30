### Authorizing a sub-account with operation permissions of elastic IP

A sub-account Developer under the enterprise account CompanyExample (ownerUin is 12345678) requires permissions of viewing and using elastic IP in CVM console of CVM services under the enterprise account CompanyExample.

Step 1: Create the following policy using policy syntax
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cvm:AllocateAddresses",
                "cvm:AssociateAddress",
                "cvm:DescribeAddresses",
                "cvm:DisassociateAddress",
                "cvm:ModifyAddressAttribute",
                "cvm:ReleaseAddresses"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

The following policy allows the sub-account to view the elastic IP, and assign and associate it with an instance. The sub-account can modify the properties of the elastic IP, unbind the association between elastic IP and instance, or release the elastic IP.

Step 1: Create the following policy using policy syntax
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cvm:DescribeAddresses",
                "cvm:AllocateAddresses",
                "cvm:AssociateAddress"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).


