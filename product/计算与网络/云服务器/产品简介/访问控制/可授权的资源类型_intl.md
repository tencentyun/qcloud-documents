Resource-level permission refers to the ability to specify what resource the user is allowed to operate. Part of CVM supports resource-level permission, which means that for some of CVM operations, you have the right to specify when the user is allowed to execute operation (based on the conditions that must be met) or use specific resources. The following table is the introduction to the resource types that can be authorized by CVM.

Resource types that can be authorized by CAM:

| Resource Type | Resource Description Method|
| :-------- | -------------- |
| CVM Instance-related |  ` qcs::cvm:$region::instance/* `|
| CVM Key-related |   `qcs::cvm:$region::keypair/*`  |
| CVM Mirror-related |   `qcs:t:cvm:$region:$account:image/*` |

The following table is the introduction to the CVM (Cloud Virtual Machine) API operation that supports resource-level permission，as well as the resource and the condition key supported by each operation. When you specify the resource path, you can use * in the path.
> **Note**：
> If a CVM API action that is not in the following table does not support resource-level permissions, you can grant users permission to use the action, but you have to specify a * for the resource element of your policy statement.

#### CVM Instance-related：
| API Action | Resource Path | Condition Key |
| :-------- | :--------| :------ |
|DescribeInstanceInternetBandwidthConfigs	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`| cvm:region<br>cvm:zone<br>cvm:instance_type|
|ModifyInstanceInternetChargeType	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type|
|ModifyInstancesAttribute	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`  | cvm:region<br>cvm:zone<br>cvm:instance_type|
|ModifyInstancesProject	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type|
|ModifyInstancesRenewFlag	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type|
|RebootInstances	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type|
|RenewInstances	|  `qcs::cvm:$region:$account:instance/* `<br>`qcs::cvm:$region:$account:instance/$instanceId`| cvm:region<br>cvm:zone<br>cvm:instance_type|
|ResetInstance	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`<br>`qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId`<br>`qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId`<br>`qcs:::cvm:$region:$account:systemdisk/*` | cvm:region<br>cvm:zone<br>cvm:instance_type|
|ResetInstancesInternetMaxBandwidth	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type|
|ResetInstancesPassword	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type|
|ResetInstancesType	|  `qcs::cvm:$region:$account:instance/* `<br>`qcs::cvm:$region:$account:instance/$instanceId`| cvm:region<br>cvm:zone<br>cvm:instance_type|
|ResizeInstanceDisks	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type|
|RunInstances	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId`<br>`qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId`<br>`qcs::cvm:$region:$account:sg/*`<br>`qcs::cvm:$region:$account:sg/$sgId`<br>`qcs::vpc:$region:$account:subnet/* `<br>`qcs::vpc:$region:$account:subnet/$subnetId`<br>`qcs:::cvm:$region:$account:systemdisk/*`<br>`qcs::cvm:$region:$account:datadisk/*`<br>`qcs::vpc:$region:$account:vpc/* `<br>`qcs::vpc:$region:$account:vpc/$vpcId` | cvm:region<br>cvm:zone<br>cvm:instance_type|
|StartInstances	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type|
|StopInstances	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type|
|TerminateInstances	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type|


#### CVM Key-related：
| API Action | Resource Path | Condition Key |
| :-------- | :--------| :------ |
|AssociateInstancesKeyPairs	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`<br>`qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId`  | -|
|CreateKeyPair	|  `qcs::cvm:$region:$account:keypair/*` | -|
|DeleteKeyPairs	|  `qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId` | -|
|DescribeKeyPairs	|  `qcs::cvm:$region:$account:keypair/*` | -|
|DescribeKeyPairsAttribute	|  `qcs::cvm:$region:$account:keypair/*`<br>` qcs::cvm:$region:$account:keypair/$keyId` | -|
| DisassociateInstancesKeyPairs	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`<br>`qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId` | -|
|ImportKeyPair	|  `qcs::cvm:$region:$account:keypair/*` | -|
|ModifyKeyPairAttribute	|  `qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId` | -|

#### CVM Mirror-related：
| API Action | Resource Path | Condition Key |
| :-------- | :--------| :------ |
| CreateImage	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`<br> `qcs::cvm:$region:$account:image/*` | cvm:region |
| DeleteImages	|  `qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId` | cvm:region |
|DescribeImages| `qcs::cvm:$region:$account:image/*`|cvm:region|
| DescribeImagesAttribute	|  `qcs::cvm:$region:$account:image/*`<br>` qcs::cvm:$region:$account:image/$imageId` | cvm:region |
| DescribeImageSharePermission	|  `qcs::cvm:$region:$account:image/*` | cvm:region |
| ModifyImageAttribute	|  `qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId` | cvm:region |
| ModifyImageSharePermission	|  `qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId` | cvm:region |
| SyncImages	|  `qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId` | cvm:region |







