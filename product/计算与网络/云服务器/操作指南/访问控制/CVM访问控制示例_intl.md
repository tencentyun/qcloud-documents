## Examples of Access Management Policies for CVMs

You can authorize users to view and use specific resources in the CVM (Cloud Virtual Machine) console by using CAM (Cloud Access Management) policies. The following examples show how to allow users to use specific policies in the console.
### Granting Full Access 
To allow a user to create and manage CVM instances, apply the policy QcloudCVMFullAccess.
Go to [Policy Management](https://console.cloud.tencent.com/cam/policy) page, select **CVM** from all services on the right, and then locate the policy as shown in the figure below.

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
The above policy is designed to grant users the permissions to work with all the resources in CVM, VPC, CLB and Cloud Monitoring.

### Granting Read Access
To allow a user to only query CVM instances, without granting him/her the permissions to create, delete, start/shut down the instances, apply the policy QcloudCVMInnerReadOnlyAccess.

>Note: It's recommended to apply the read-only policy for CVMs.</font>

Go to [Policy Management](https://console.cloud.tencent.com/cam/policy) page, select **CVM** from all services on the right, and then locate the policy as shown in the figure below.
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
The above policy is designed to grant users the permissions to perform all actions starting with `Describe` and `Inquiry` in CVM.

### Read-only policy for CVM-related resources
To allow a user to only query CVM instances and relevant resources (VPC, CLB), without granting him/her the permissions to create, delete, start/shut down the instances, apply the policy QcloudCVMReadOnlyAccess.
Go to [Policy Management](https://console.cloud.tencent.com/cam/policy) page, select **CVM** from all services on the right, and then locate the policy as shown in the figure below.
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
The above policy is designed to grant users the permissions to perform the following actions:
- All actions starting with `Describe` and `Inquiry` in CVM.
- All actions starting with `Describe`, `Inquiry` and `Get` in VPC.
- All actions starting with `Describe` in CLB.
- All actions in Monitor.

### Policy for elastic cloud disks

To allow a user to view, create and use cloud disks in the CVM console, add the following actions to your policy and associate the policy to the user.

- **CreateCbsStorages:** Create Cloud Disk.
- **AttachCbsStorages:** Mount the specified elastic cloud disk to the specified CVM.
- **DetachCbsStorages:** Unmount the specified elastic cloud disk.
- **ModifyCbsStorageAttributes:** Modify the name or the project ID of the specified cloud disk.
- **DescribeCbsStorages:** Query the details of a cloud disk.
- **DescribeInstancesCbsNum:** Query the number of elastic cloud disks that have been mounted to a CVM and the maximum number of elastic cloud disks that are allowed to be mounted to the CVM.
- **RenewCbsStorage:** Renew the specified elastic cloud disk.
- **ResizeCbsStorage:** Expand the capacity of the specified elastic cloud disk.

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
### Policy for security groups

To allow a user to view and use security groups in the CVM console, add the following operations to your policy and associate the policy to the user.

- **DeleteSecurityGroup:** Delete a security group.
- **ModifySecurityGroupPolicys:** Replace all the policies of a security group.
- **ModifySingleSecurityGroupPolicy:** Modify single security group policy.
- **CreateSecurityGroupPolicy:** Create a security group.
- **DeleteSecurityGroupPolicy:** Delete a security group policy.
- **ModifySecurityGroupAttributes:** Modify the attributes of security group.

The following policy allows users to create and delete security groups in the CVM console.
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

### Policy for EIPs

To allow a user to view and use EIPs in the CVM console, add the following operations to your policy and associate the policy to the user.

- **AllocateAddresses:** Assign address to VPC or CVM.
- **AssociateAddress :** Associate an EIP to an instance or a network interface.
- **DescribeAddresses:** View the EIPs in the CVM console.
- **DisassociateAddress:** Disassociate an EIP from an instance or a network interface.
- **ModifyAddressAttribute:** Modify the attributes of EIP.
- **ReleaseAddresses:** Terminate the EIP.

The following policy allows users to view EIPs and associate EIPs with instances. Users cannot modify the attributes of EIPs, disassociate EIPs from instances, or release EIPs.
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
### Policy for authorizing users to perform operations on specific CVMs
To authorize a user to perform operations on a specific CVM, associate the following policy to the user.
The following policy authorizes the user to work with a CVM instance (ID: ins-1) in Guangzhou region.

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


### Policy for authorizing users to perform operations on the CVMs in a specific region
To authorize a user to perform operations on the CVMs in a specific region, associate the following policy to the user.
The following policy authorizes the user to work with CVM instances in Guangzhou region.

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
### Custom policies

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
Replace "Action" with the operation to be allowed or denied.
Replace "Resource" with the resources that you want to authorize users to work with.
Replace "Effect" with Allow or Deny.



