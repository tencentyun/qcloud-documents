## Examples of Access Management Policies for CDB

You can authorize users to view and use specific resources in the CDB (Cloud DataBase) console by using CAM (Cloud Access Management) policies. The examples here allow users to use specific policies in the console.

### CDB Full Read-write Policy

To authorize users to create and manage CDB instances, you can implement the policy named QcloudCDBFullAccess on them.

Go to [Policy Management](https://console.cloud.tencent.com/cam/policy), click the **Service Type** and select **CDB** in the drop-down list, and the policy can be found in the result as shown below:

![Alt text](https://mc.qcloudimg.com/static/img/8b6da54d897b1b92c86b789a3c36c369/fullPolicy.png)
The policy syntax is as follows:

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cdb:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "vpc:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "cvm:*"
            ],
            "resource": "qcs::cvm:::sg/*",
            "effect": "allow"
        },
        {
            "action": [
                "cos:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "effect": "allow",
            "action": "monitor:*",
            "resource": "*"
        },
        {
            "action": [
                "kms:CreateKey",
                "kms:GenerateDataKey",
                "kms:Decrypt",
                "kms:ListKey"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
The policy above is designed to allow users to apply CAM policy authorization for all the resources in CDB, VPC (Virtual Private Cloud), Security Group, COS (Cloud Object Storage), KMS (Key Management Service) and Monitor.

### CDB Read-only Policy
To allow a user to query CDB instances, without granting him/her the permission to create, delete and modify these instances, you can implement the policy named QcloudCDBInnerReadOnlyAccess on the user.

>Recommand: Configure the read-only policy for CDB.</font>

Go to [Policy Management](https://console.cloud.tencent.com/cam/policy), click the **Service Type** and select **CDB** in the drop-down list, and the policy can be found in the result as shown below:

![Alt text](https://mc.qcloudimg.com/static/img/62adee9ce100660541a072f51f69cbc1/innerReadonlyPolicy.png)

The policy syntax is as follows:

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cdb:Describe*"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
The policy above is designed to allow users to apply CAM policy authorization for all operations starting with " Describe " in CDB.

### Read-only Policy for CDB-related Resources
To allow a user to query CDB instances and relevant resources (VPC, Security Group, COS, Monitor), without granting him/her the permission to create, delete and modify these instances, you can implement the policy named QcloudCDBReadOnlyAccess on the user.

Go to [Policy Management](https://console.cloud.tencent.com/cam/policy), click the **Service Type** and select **CDB** in the drop-down list, and the policy can be found in the result as shown below:

![Alt text](https://mc.qcloudimg.com/static/img/f5538527538ce6ee1feb0ee0f15234fc/readonly.png)

The policy syntax is as follows:

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cdb:Describe*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "vpc:Describe*",
                "vpc:Inquiry*",
                "vpc:Get*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "cvm:DescribeSecurityGroup*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "cos:List*",
                "cos:Get*",
                "cos:Head*",
                "cos:OptionsObject"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "effect": "allow",
            "action": "monitor:*",
            "resource": "*"
        }
    ]
}
```
The policy above is designed to allow users to apply CAM policy authorization for the following operations:

- All operations starting with " Describe " in CDB.
- All operations starting with " Describe ", " Inquiry " and " Get " in VPC.
- All operations starting with " DescribeSecurityGroup " in Security Group.
- All operations starting with " List ", " Get ", " Head " and " OptionsObject " in COS.
- All operations in Monitor.

### Policy for Authorizing Users to Perform Operations on a Specified CDB
If you want to authorize a user to have certain CDB operation permission, the policy below can be associated with the user. The policy below allows a user to have the operation permission of the CDB instance with id of cdb-xxx from the region of Guanzhou.

```
{
    "version": "2.0",
    "statement": [
        {
            "action": "cdb:*",
            "resource": "qcs::cdb:ap-guangzhou::instanceId/cdb-xxx",
            "effect": "allow"
        }
    ]
}
```

### Policy for Authorizing Users to Perform Operations on a batch CDB
If you want to authorize a user to have batch CDB operation permission, the policy below can be associated with the user. The policy below allows a user to have the operation permission of the CDB instance with id of cdb-xxx and cdb-yyy from the region of Guanzhou as well as the CDB instance with id of cdb-zzz from the region of Beijing.

```
{
    "version": "2.0",
    "statement": [
        {
            "action": "cdb:*",
            "resource": ["qcs::cdb:ap-guangzhou::instanceId/cdb-xxx", "qcs::cdb:ap-guangzhou::instanceId/cdb-yyy", "qcs::cdb:ap-beijing::instanceId/cdb-zzz"],
            "effect": "allow"
        }
    ]
}
```

### Policy for Authorizing Users to Perform Operations on the CDBs in a Specific Region
If you want to authorize a user to perform operations on CDBs in a specific region, the following policies can be associated with the user. The following policies authorize users to perform operations on CDBs in Guangzhou.

```
{
    "version": "2.0",
    "statement": [
        {
            "action": "cdb:*",
            "resource": "qcs::cdb:ap-guangzhou::*",
            "effect": "allow"
        }
    ]
}
```
### Custom Policy

If preset policies cannot meet your requirements, you can create custom policies. The syntax of custom policies is as following:

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
