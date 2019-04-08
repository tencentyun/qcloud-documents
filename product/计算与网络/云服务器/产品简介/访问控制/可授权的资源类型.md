资源级权限指的是能够指定允许用户对哪些资源具有执行操作的能力。 CVM 部分支持资源级权限，这意味着对于某些 CVM 操作，您可以控制何时允许用户执行操作 (基于必须满足的条件)或是允许用户使用的特定资源。下表将向您介绍  CVM 可授权的资源类型。

CAM 中可授权的资源类型：

| 资源类型 | 授权策略中的资源描述方法 |
| :-------- | -------------- |
| 云服务器实例相关 |  ` qcs::cvm:$region::instance/* `|
| 云服务器密钥相关 |   `qcs::cvm:$region::keypair/*`  |
| 云服务器镜像相关 |   `qcs::cvm:$region:$account:image/*` |

下表将介绍当前支持资源级权限的 CVM （Cloud Virtual Machine,云服务器） API 操作，以及每个操作支持的资源和条件密钥。指定资源路径的时候，您可以在路径中使用 * 通配符。
> **注意**：
> 如果某一个 CVM API 操作在下表中没有列出，则它不支持资源级权限。如果 CVM API 操作不支持资源级权限，那么您还是可以向用户授予使用该操作的权限，但是必须为策略语句的资源元素指定 *  。

#### 云服务器实例相关：
| API 操作 | 资源路径 | 条件密钥 |
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


#### 云服务器密钥相关：
| API 操作 | 资源路径 | 条件密钥 |
| :-------- | :--------| :------ |
|AssociateInstancesKeyPairs	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`<br>`qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId`  | -|
|CreateKeyPair	|  `qcs::cvm:$region:$account:keypair/*` | -|
|DeleteKeyPairs	|  `qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId` | -|
|DescribeKeyPairs	|  `qcs::cvm:$region:$account:keypair/*` | -|
|DescribeKeyPairsAttribute	|  `qcs::cvm:$region:$account:keypair/*`<br>` qcs::cvm:$region:$account:keypair/$keyId` | -|
| DisassociateInstancesKeyPairs	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`<br>`qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId` | -|
|ImportKeyPair	|  `qcs::cvm:$region:$account:keypair/*` | -|
|ModifyKeyPairAttribute	|  `qcs::cvm:$region:$account:keypair/*`<br>`qcs::cvm:$region:$account:keypair/$keyId` | -|

#### 云服务器镜像相关：
| API 操作 | 资源路径 | 条件密钥 |
| :-------- | :--------| :------ |
| CreateImage	|  `qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`<br> `qcs::cvm:$region:$account:image/*` | cvm:region |
| DeleteImages	|  `qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId` | cvm:region |
|DescribeImages| `qcs::cvm:$region:$account:image/*`|cvm:region|
| DescribeImagesAttribute	|  `qcs::cvm:$region:$account:image/*`<br>` qcs::cvm:$region:$account:image/$imageId` | cvm:region |
| DescribeImageSharePermission	|  `qcs::cvm:$region:$account:image/*` | cvm:region |
| ModifyImageAttribute	|  `qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId` | cvm:region |
| ModifyImageSharePermission	|  `qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId` | cvm:region |
| SyncImages	|  `qcs::cvm:$region:$account:image/*`<br>`qcs::cvm:$region:$account:image/$imageId` | cvm:region |







