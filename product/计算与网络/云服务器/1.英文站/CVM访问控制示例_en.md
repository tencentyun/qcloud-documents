## Examples of Access Management Policies for CVM

You can authorize users to view and use specific resources in the CVM (Cloud Virtual Machine) console by using CAM (Cloud Access Management) policies. The examples here allow users to use specific policies in the console.
### Full Read-Write Policy for CVM
To authorize users to create and manage CVM instances, you can implement the policy named QcloudCVMFullAccess on them.
Go to [Policy Management Interface](https://console.cloud.tencent.com/cam/policy), select "CVM" in all services at the right side, and the policy can be found as shown in the following figure.

![Alt text](https://mc.qcloudimg.com/static/img/ac676b0e8f27c0759ad602c5fe383d3c/1500033749808.png)
The policy syntax is as follows:

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "name/vpc:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "name/clb:*"
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
The policy above is designed to authorize users to work with the resources in CVM, VPC (Virtual Private Cloud), CLB (Cloud Load Balance) and MONITOIOR.

### Read-only Policy for CVM
To allow a user to query CVM instances, without granting him/her the permission to create, delete, start/shut down these instances, you can implement the policy named QcloudCVMInnerReadOnlyAccess on the user.

>Advice: Configure the read-only policy of CVM.</font>

Go to [Policy Management Interface](https://console.cloud.tencent.com/cam/policy), select "CVM" in all services at the right side, and the policy can be found as shown in the following figure.
![Alt text](https://mc.qcloudimg.com/static/img/c3a3537c24dde34054a590c3fe7eccc8/1500033727016.png)

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
The policy above is designed to grant users the access to all operations starting with "Describe" and "Inquiry" in CVM.

### Read-only Policy for CVM-related Resources
To allow a user to query CVM instances and relevant resources (VPC, CLB), without granting him/her the permission to create, delete, start/shut down these instances, you can implement the policy named QcloudCVMReadOnlyAccess on the user.
Go to [Policy Management Interface](https://console.cloud.tencent.com/cam/policy), select "CVM" in all services at the right side, and the policy can be found as shown in the following figure.
![Alt text](https://mc.qcloudimg.com/static/img/17c3e2be396ea544b7d4ca425e5049c5/1500033915369.png)
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
The policy above is designed to grant users the access to the following operations:
- All operations starting with "Describe" and "Inquiry" in CVM.
- All operations starting with "Describe", "Inquiry" and "Get" in VPC.
- All operations starting with "Describe" in CLB.
- All operations in Monitor.

### Policy for Elastic Cloud Disk

To allow a user to view, create and use cloud disks in the CVM console, you can add the following operations to your policy and associate the policy to the user.

- **CreateCbsStorages:** Create a cloud disk.
- **AttachCbsStorages:** Mount the specified elastic cloud disk onto the specified CVM.
- **DetachCbsStorages:** Unmount the specified elastic cloud disk.
- **ModifyCbsStorageAttributes:** Modify the name or the project ID of the specified cloud disk.
- **DescribeCbsStorages:** Query the details of a cloud disk.
- **DescribeInstancesCbsNum:** Query the number of elastic cloud disks that have been mounted to the CVM and the total number of elastic cloud disks that are allowed to be mounted to the CVM.
- **RenewCbsStorage:** Renew the specified elastic cloud disk.
- **ResizeCbsStorage:** Expand the specified elastic cloud disk.

The following policy does not allow users to modify the attributes of cloud disks.
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:ModifyCbsStorageAttributes",
            ],
            "resource": [
                "qcs::cvm::uin/1410643447:*"
            ],
            "effect": "deny"
        }
    ]
}

```
### Policy for Security Group

To allow a user to view and use security groups in the CVM console, you can add the following operations to your policy and associate the policy to the user.

- **DeleteSecurityGroup:** Delete a security group.
- **ModifySecurityGroupPolicys:** Replace all the policies of a security group.
- **ModifySingleSecurityGroupPolicy:** Modify a single policy of a security group.
- **CreateSecurityGroupPolicy:** Create a security group policy.
- **DeleteSecurityGroupPolicy:** Delete a security group policy.
- **ModifySecurityGroupAttributes:** Modify the attributes of a security group.

The following policy allows users to create, delete security groups in the CVM console.
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:DeleteSecurityGroup",
                "name/cvm:CreateSecurityGroup"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
The following policy allows users to create, delete and modify security group policies in the CVM console.
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:ModifySecurityGroupPolicys",
                "name/cvm:ModifySingleSecurityGroupPolicy",
                "name/cvm:CreateSecurityGroupPolicy",
                "name/cvm:DeleteSecurityGroupPolicy"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

### Policy for EIP

To allow a user to view and use EIPs in the CVM console, you can add the following operations to your policy and associate the policy to the user.

- **AllocateAddresses:** Assign an EIP to VPC or CVM.
- **AssociateAddress:** Associate an EIP to an instance or a network interface.
- **DescribeAddresses:** View EIPs in the CVM console.
- **DisassociateAddress:** Disassociate an EIP from an instance or a network interface.
- **ModifyAddressAttribute:** Modify the attributes of an EIP.
- **ReleaseAddresses:** Release an EIP.

The following policy allows users to view an EIP, assign it to and associate it with an instance. Users cannot modify the attributes of the EIP, disassociate it from an instance, or release the EIP.
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:DescribeAddresses",
                "name/cvm:AllocateAddresses",
                "name/cvm:AssociateAddress"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
### Policy for Authorizing Users to Perform Operations on a Specified CVM
To authorize a user to perform operations on a specific CVM, you can associate the following policy to the user.
The following policy authorizes users to work with a CVM instance (ID: ins-1) in Guangzhou region.

```
{
    "version": "2.0",
    "statement": [
        {
            "action": "cvm:*",
            "resource": "qcs::cvm:gz::instance/ins-1",
            "effect": "allow"
        }
    ]
}
```


### Policy for Authorizing Users to Perform Operations on the CVMs in a Specific Region
To authorize a user to perform operations on the CVMs in a specific region, you can associate the following policy to the user.
The following policy authorizes users to work with CVM instances in Guangzhou region.

```
{
    "version": "2.0",
    "statement": [
        {
            "action": "cvm:*",
            "resource": "qcs::cvm:gz::*",
            "effect": "allow"
        }
    ]
}
```
### Custom Policy

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
Replace Action with the operation to be allowed or rejected.
Replace Resource with the specific resource you want to authorize the access to.
Replace Effect with Allow or Reject.



