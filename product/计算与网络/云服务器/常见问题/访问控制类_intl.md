### How to create custom policy?

If preset policies cannot meet your requirements, you can create custom policies.
The syntax of custom policies is as follows:

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "Action"
            ],
            "resource": "Resource",
            "effect": "Effect"
        }
    ]
}
```

- Replace "Action" with the operation to be allowed or denied.
- Replace "Resource" with the resources that you want to authorize users to work with.
- Replace "Effect" with Allow or Deny.

### How to configure read-only policy for CVMs?

To allow a user to only query CVM instances, without granting him/her the permissions to create, delete, start/shut down the instances, implement the policy named QcloudCVMInnerReadOnlyAccess.

Log in to the CAM console, and find the policy quickly by searching for **CVM** on the [Policy Management](https://console.cloud.tencent.com/cam/policy) page.

The policy syntax is as follows:

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:Describe*",
                "name/cvm:Inquiry*"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

The above policy is designed to **grant users the permissions to perform the following operations**:

- All operations starting with "Describe" in CVM.
- All operations starting with "Inquiry" in CVM.

### How to configure read-only policy for CVM-related resources?

To allow a user to only query CVM instances and relevant resources (VPC, CLB), without granting him/her the permissions to create, delete, start/shut down the instances, implement the policy named QcloudCVMReadOnlyAccess.

Log in to the CAM console, and find the policy quickly by searching for **CVM** on the [Policy Management](https://console.cloud.tencent.com/cam/policy) page.

The policy syntax is as follows:

```
 {
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:Describe*",
                "name/cvm:Inquiry*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "name/vpc:Describe*",
                "name/vpc:Inquiry*",
                "name/vpc:Get*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "name/clb:Describe*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "effect": "allow",
            "action": "name/monitor:*",
            "resource": "*"
        }
    ]
}
```

The above policy is designed to **grant users the permissions to perform the following operations**:

- All operations starting with "Describe" and "Inquiry" in CVM.
- All operations starting with "Describe", "Inquiry" and "Get" in VPC.
- All operations starting with "Describe" in Load Balance.
- All operations in Monitor.


