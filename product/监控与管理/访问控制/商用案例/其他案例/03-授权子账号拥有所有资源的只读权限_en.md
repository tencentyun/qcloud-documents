### Authorizing a sub-account with read-only permission of all resources

A sub-account Developer under the enterprise account CompanyExample requires full access to all resources under this enterprise account.

Solution A:

The enterprise account CompanyExample directly authorizes the preset policy ReadOnlyAccess to the sub-account Developer. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Step 1: Create the following policy using policy syntax
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cvm:Describe*",
                "cvm:Inquiry*",
                "vpc:Describe*",
                "vpc:Inquiry*",
                "vpc:Get*",
                "clb:Describe*",
                "monitor:*",  
                "bm:Describe*",
                "bmeip:Describe*",
                "bmlb:Describe*",
                "bmvpc:Describe*",
                "bm:Get*",
                "bmlb:Get*",
                "cos:List*",
                "cos:Get*",
                "cos:Head*",
                "cos:OptionsObject",
                "cas:Describe*",
                "cas:List*",
                "cas:Get*",
                "kms:List*",
                "kms:Get*"                
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).


