Resource-level permissions can be used to specify which resources users can work with. CVM supports part of the resource-level permissions. This means that for some CVM operations, you can control the time when users are allowed to perform operations (condition must be met) or to use specified resources. The following table describes the types of resource that can be authorized in CVM.

The type of resource that can be authorized in CAM:

| Resource type | Resource description method in authorization policy |
| :-------- | -------------- |
| CVM instance related | `qcs::cvm:$region::instance/*` |
| CVM key related | `qcs::cvm:$region::keypair/*` |
| CVM image related | `qcs:t:cvm:$region:$account:image/*` |

The following table describes the API operations of CVM (Cloud Virtual Machine) that support resource-level permissions, and the resources and condition keys supported for each operation. You can use wildcard "*" in the path when specifying resource path.
> **Note**:
> Any CVM API operation not listed here does not support resource-level permission. If any CVM API operation does not support resource-level permission, you can still authorize the permission of this operation to users, but you must specify * for the resource element of policy statement.

#### CVM Instance Related:
| API Operation | Resource Path | Condition Key |
| :-------- | :--------| :------ |
| DescribeInstanceInternetBandwidthConfigs	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| ModifyInstanceInternetChargeType	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| ModifyInstancesAttribute	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| ModifyInstancesProject	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| ModifyInstancesRenewFlag	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| RebootInstances	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| RenewInstances	| `qcs::cvm:$region:$account:instance/* `<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| ResetInstance	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`<br>`qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId`<br>`qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId`<br>`qcs:::cvm:$region:$account:systemdisk/*` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| ResetInstancesInternetMaxBandwidth	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| ResetInstancesPassword	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| ResetInstancesType	| `qcs::cvm:$region:$account:instance/* `<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| ResizeInstanceDisks	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| RunInstances	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId`<br>`qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId`<br>`qcs::cvm:$region:$account:sg/*`<br>`qcs::cvm:$region:$account:sg/$sgId`<br>`qcs::vpc:$region:$account:subnet/* `<br>`qcs::vpc:$region:$account:subnet/$subnetId`<br>`qcs:::cvm:$region:$account:systemdisk/*`<br>`qcs::cvm:$region:$account:datadisk/*`<br>`qcs::vpc:$region:$account:vpc/* `<br>`qcs::vpc:$region:$account:vpc/$vpcId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| StartInstances	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| StopInstances	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |
| TerminateInstances	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` | cvm:region<br>cvm:zone<br>cvm:instance_type |


#### CVM Key Related:
| API Operation | Resource Path | Condition Key |
| :-------- | :--------| :------ |
| AssociateInstancesKeyPairs	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`<br>`qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId` | -|
| CreateKeyPair	| `qcs::cvm:$region:$account:keypair/*` | -|
| DeleteKeyPairs	| `qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId` | -|
| DescribeKeyPairs	| `qcs::cvm:$region:$account:keypair/*` | -|
| DescribeKeyPairsAttribute	| `qcs::cvm:$region:$account:keypair/*`<br>` qcs::cvm:$region:$account:keypair/$keyId` | -|
| DisassociateInstancesKeyPairs	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`<br>`qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId` | -|
| ImportKeyPair	| `qcs::cvm:$region:$account:keypair/*` | -|
| ModifyKeyPairAttribute	| `qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId` | -|

#### CVM Image Related:
| API Operation | Resource Path | Condition Key |
| :-------- | :--------| :------ |
| CreateImage	| `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`<br> `qcs::cvm:$region:$account:image/*` | cvm:region |
| DeleteImages	| `qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId` | cvm:region |
|DescribeImages| `qcs::cvm:$region:$account:image/*`|cvm:region|
| DescribeImagesAttribute	| `qcs::cvm:$region:$account:image/*`<br>` qcs::cvm:$region:$account:image/$imageId` | cvm:region |
| DescribeImageSharePermission	| `qcs::cvm:$region:$account:image/*` | cvm:region |
| ModifyImageAttribute	| `qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId` | cvm:region |
| ModifyImageSharePermission	| `qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId` | cvm:region |
| SyncImages	| `qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId` | cvm:region |








