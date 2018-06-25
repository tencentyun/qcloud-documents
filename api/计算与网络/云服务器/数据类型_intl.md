### Placement

> The location of an instance is described, including the availability zone, project, host, etc. (CDH products only)

| Name | Type | Required | Description |
|---------|---------|---------|---------|
| Zone | String | Yes | ID of the [availability zone](/document/product/213/9452#zone) to which the instance belongs. This parameter can be obtained by calling the Zone field in the returned value of [DescribeZones](https://cloud.tencent.com/document/api/213/9455). |
| ProjectId | Integer | No | ID of the project to which the instance belongs. This parameter can be obtained by calling the projectId field in the returned value of [DescribeProject](https://cloud.tencent.com/document/api/378/4400). If this is left empty, default project is used. |
| HostIds.N | array of Strings | No | The list of IDs of CDHs to which the instance belongs. If you have purchased CDHs and have specified this parameter, the instance you purchased will be randomly deployed on these CDHs. Currently, it is not supported. |

### SystemDisk

> The system disk where the operating system is located is described.

| Name | Type | Required | Description |
|---------|---------|---------|---------|
| DiskType | String | No | System disk type. For information on limits of system disk type, please see [CVM Instance Configuration](https://cloud.tencent.com/document/product/213/2177). Value range: <br><li>LOCAL_BASIC: local HDD<br><li>LOCAL_SSD: local SSD disk<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_SSD: SSD cloud disk<br><br>Default value: LOCAL_BASIC. |
| DiskId | String | No | System disk ID. LOCAL_BASIC and LOCAL_SSD do not have an ID. This parameter is not supported currently. |
| DiskSize | Integer | No | System disk size, in GB. Default is 50 |

### DataDisk

> The data disk is described.

| Name | Type | Required | Description |
|---------|---------|---------|---------|
| DiskType | String | No | Data disk type. For information on limits of data disk type, please see [CVM Instance Configuration](https://cloud.tencent.com/document/product/213/2177). Value range: <br><li>LOCAL_BASIC: local HDD<br><li>LOCAL_SSD: local SSD disk<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_PREMIUM: premium cloud disk<br><li>CLOUD_SSD: SSD cloud disk<br><br>Default value: LOCAL_BASIC. <br><br>This parameter is invalid for the API `ResizeInstanceDisk`. |
| DiskId | String | No | System disk ID. LOCAL_BASIC and LOCAL_SSD do not have an ID. This parameter is not supported currently. |
| DiskSize | Integer | No | Data disk size, in GB. The minimum adjustment increment is 10 GB. Different types of data disks have different value ranges. For information on limits, please see [CVM Instance Configuration](https://cloud.tencent.com/document/product/213/2177). Default is 0, indicating that no data disk is purchased. For more information on limit, please see the product documentation. |

### VirtualPrivateCloud

> VPC-related information is described, including subnet and IP information.

| Name | Type | Required | Description |
|---------|---------|---------|---------|
| VpcId | String | Yes | VPC ID. This parameter can be obtained by calling the unVpcId field in the returned value of [DescribeVpcEx](https://cloud.tencent.com/document/api/215/1372). |
| SubnetId | String | Yes | VPC Subnet ID. This parameter can be obtained by calling the unSubnetId field in the returned value of [DescribeSubnetEx](https://cloud.tencent.com/document/api/215/1371). |
| AsVpcGateway | Boolean | No | Whether used as a public gateway. The public gateway can be used only when the instance has a Public IP and is in VPC. Value range:<br><li>TRUE: used as public gateway<br><li>FALSE: not used as public gateway<br><br>Default: FALSE. |
| PrivateIpAddresses.N | array of Strings | No | VPC subnet IP array. Currently only one IP is supported. This parameter can be used to create instances and modify VPC properties for instances. |


### InternetAccessible

> The accessibility, billing method and maximum bandwidth for an instance to use public network are described.

| Name | Type | Required | Description |
|---------|---------|---------|---------|
| InternetChargeType | String | No | Network billing type. Value range:<br><li>BANDWIDTH_PREPAID: Prepaid by bandwidth<br><li>TRAFFIC_POSTPAID_BY_HOUR: Traffic postpaid by hour<br><li>BANDWIDTH_POSTPAID_BY_HOUR: Bandwidth postpaid by hour<br><li>BANDWIDTH_PACKAGE: Bandwidth package<br>Default: TRAFFIC_POSTPAID_BY_HOUR. |
| InternetMaxBandwidthOut | Integer | No | Upper limit of Outbound bandwidth of Public network, in Mbps. Default: 0 Mbps. Upper limit of bandwidth varies among different models. For details, please see [Purchase Network Bandwidth](https://cloud.tencent.com/document/product/213/509). |
| PublicIpAssigned | Boolean | No | Whether to assign public IPs. Value range:<br><li>TRUE: assign public IPs<br><li>FALSE: not assign public IPs<br><br>If the public network bandwidth is greater than 0 MB, you're free to choose whether to enable the public IP ("Enable" by default). If the public network bandwidth is 0 MB, the public IP will not be assigned. |

### InstanceChargePrepaid

> The billing method of an instance is described.

| Name | Type | Required | Description |
|---------|---------|---------|---------|
| Period | Integer | Yes | Purchasable usage period of instance, in month. Value range: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36. |
| RenewFlag | String | No | Automatic renewal flag. Value range:<br><li>NOTIFY_AND_AUTO_RENEW: notify expiry and renew automatically<br><li>NOTIFY_AND_MANUAL_RENEW: notify expiry but not renew automatically<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify expiry nor renew automatically<br><br>Default: NOTIFY_AND_AUTO_RENEW. If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis when the account balance is sufficient. |


### LoginSettings

> Instance login related configuration and information are described.

| Name | Type | Required | Description |
|---------|---------|---------|---------|
| Password | String | No | Instance Login Password. Password complexity requirements vary among different types of operating systems, as shown below: <br><li>Password of the instance on Linux should have a length of 8 to 16 characters comprised of at least two of the following types: [a-z, A-Z], number [0-9], and special symbols [( ) &#96; ~ ! @ # $ % ^ & * - + = &#124; { } [ ] : ; ' , . ? / ]. <br><li>Password of the instance on Windows should be a combination of 12-16 characters comprised of at least three of the following types: lowercase letters [a-z], uppercase letters [A-Z], numbers [0-9] and special symbols [( ) &#96; ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]. <br><br>If this parameter is not specified, a random password will be generated and notified to the user via the internal message. |
| KeyIds.N | array of Strings | No | The list of key IDs. After the key is associated, the instance can be accessed using the corresponding private key. KeyId can be obtained via API DescribeKeyPairs. The key and password cannot be specified at the same time, while the Windows does not support the specified key. You can specify only one key when purchasing the instance. |
| KeepImageLogin | String | No | Keep the original settings of the image. This parameter cannot be specified with Password or KeyIds.N. You can specify this parameter to TRUE only if you create a instance using a custom image, shared image, or image imported from external resources. Value range:<br><li>TRUE: keep the login settings of the image<br><li>FALSE: not keep the login settings of the image<br><br>Default: FALSE. |


### RunSecurityServiceEnabled

> Information about the Cloud Security service is described.

| Name | Type | Required | Description |
|---------|---------|---------|---------|
| Enabled | Boolean | No | Whether to enable [Cloud Security](https://cloud.tencent.com/document/product/296) service. Value range: <br><li>TRUE: enable Cloud Security<br><li>FALSE: not enable Cloud Security<br><br>Default: TRUE. |

### RunMonitorServiceEnabled

> Information about the Cloud Monitoring service is described.

| Name | Type | Required | Description |
|---------|---------|---------|---------|
| Enabled | Boolean | No | Whether to enable [Cloud Monitoring](https://cloud.tencent.com/document/product/296) service. Value range: <br><li>TRUE: enable Cloud Monitoring<br><li>FALSE: not enable Cloud Monitoring<br><br>Default: TRUE. |

### EnhancedService

> The enabling conditions and settings of the instance's enhanced services are described, such as Cloud Security, Cloud Monitoring and other instance Agents.

| Name | Type | Required | Description |
|---------|---------|---------|---------|
| SecurityService | [RunSecurityServiceEnabled](#runsecurityserviceenabled) object | No | Enable the Cloud Security service. If this parameter is not specified, the Cloud Security service is enabled by default. |
| MonitorService | [RunMonitorServiceEnabled](#runmonitorserviceenabled) object | No | Enable the Cloud Monitoring service. If this parameter is not specified, the Cloud Monitoring service is enabled by default. |

### ItemPrice

> The price of each item is described.

| Name | Type | Required | Description |
|---------|---------|---------|---------|
| UnitPrice | Float | No | Subsequent unit price, in CNY. |
| ChargeUnit | String | No | Subsequent billing unit. Value Range: <br><li>HOUR: bill by hour. Scenarios using this billing unit include: instance postpaid by hour (POSTPAID_BY_HOUR), bandwidth postpaid by hour (BANDWIDTH_POSTPAID_BY_HOUR): <br><li>GB: the billing unit is calculated in GB. The scenario using this billing unit is: traffic postpaid by hour (TRAFFIC_POSTPAID_BY_HOUR). |
| OriginalPrice | Float | No | Original price of advance expenses, in RMB. |
DiscountPrice | Float | No | Discount price of advance expenses, in RMB. |

### Price

> Price

| Name | Type | Required | Description |
|---------|---------|---------|---------|
| InstancePrice | [ItemPrice](#itemprice) object | No | Describes the instance price.
| BandwidthPrice | [ItemPrice](#itemprice) object | No | Describes the network price.

### Filter

> Key-value pair filters for conditional filtering queries are described, such as filtering ID, name, status, etc.
> * If more than one `Filter` exist, these `Filter` are in an `AND` relation.
> * If multiple `Values` exist in a `Filter`, these `Values`under the `Filter` are in an `OR` relation.
>
> Take the `Filter` of the API [DescribeInstances](/document/api/213/9388) as an example. To query an instance located in Guangzhong Zone 1 (`zone`) ***and*** billed on a postpaid ***or*** postpaid basis (`instance-charge-type`), do as follows:
```
Filters.1.Name=zone
&Filters.1.Values.1=ap-guangzhou-1
&Filters.2.Name=instance-charge-type
&Filters.2.Values.1=PREPAID
&Filters.3.Values.2=POSTPAID_BY_HOUR
```

| Name | Type | Required | Description |
|----|-----|---------|-----|
| Name | String | No | The name of the filter key. |
| Values.N | array of Strings | No | One or more filter values. |

### InstanceStatus

> The status of the instance is described. Status type can be found in [Table of Instance Status](/document/api/213/9452#INSTANCE_STATE)

| Name | Type | Required | Description |
|----|-----|---------|-----|
| InstanceId | String | No | Instance `ID`. |
| InstanceState | String | No | [Instance Status](/document/api/213/9452#INSTANCE_STATE). |

### Instance

> Information of the instance is described.

| Name | Type | Required | Description |
|----|-----|---------|-----|
| Placement | [Placement](#placement) | No | Location of the instance. |
| InstanceId | String | No | Instance `ID`. |
| InstanceType | String | No | Instance model. |
| CPU | Integer | No | Number of cores of CPU in the instance, in core. |
| Memory | Integer | No | Instance memory capacity, in `GB`. |
| RestrictState | String | No | Instance state. Value range:<br><li>NORMAL: normal instances<br><li>EXPIRED: expired instances<br><li>PROTECTIVELY_ISOLATED: protectively isolated instances. |
| InstanceName | String | No | Instance name. |
| InstanceChargeType | String | No | Instance billing method. Value range: <br><li>`PREPAID`: prepaid (by year/month) <br><li>`POSTPAID_BY_HOUR`: postpaid (by traffic) <br><li>`CDHPAID`:` CDH` paid, i.e., only pay for `CDH`, excluding instances on the` CDH`. |
| SystemDisk | [SystemDisk](#systemdisk) | No | Information of the system disk in the instance. |
DataDisks | array of [DataDisk](#diskdisk) objects | No | Information of the data disk in the instance, only including the data disks purchased with the instance. |
| PrivateIpAddresses | array of Strings | No | The list of private `IP` of the instance primary ENI. |
| PublicIpAddresses | array of Strings | No | The list of public `IP` of the instance primary ENI. |
| InternetAccessible | [InternetAccessible](#internetaccessible) | No | Instance bandwidth information. |
| VirtualPrivateCloud | [VirtualPrivateCloud](#virtualprivatecloud) | No | Information of the VPC to which the instance belongs. |
| ImageId | String | No | `ID` of the image used by the production instance. |
| RenewFlag | String | No | Automatic renewal flag. Value range: <br><li>`NOTIFY_AND_MANUAL_RENEW`:notify expiry but not renew automatically<br><li>`NOTIFY_AND_AUTO_RENEW`: notify expiry and renew automatically<br><li>`DISABLE_NOTIFY_AND_MANUAL_RENEW`: neither notify expiry nor renew automatically. |
| CreatedTime | Timestamp | No | Creation time. In accordance with the `ISO8601` standard, and use the` UTC` time, such as `YYYY-MM-DDThh: mm: ssZ`. |
ExpiredTime | Timestamp | No | Expiry time. In accordance with the `ISO8601` standard, and use the` UTC` time, such as `YYYY-MM-DDThh: mm: ssZ`. |


### InstanceTypeConfig

> The configuration information of the instance model is described.

| Name | Type | Required | Description |
|----|-----|---------|-----|
| Zone | String | No | Availability zone. |
| InstanceType | String | No | Instance model. |
| InstanceFamily | String | No | Instance model series. |
| GPU | Integer | No | Number of cores of GPU, in core. |
| CPU | Integer | No | Number of cores of CPU, in core. |
| Memory | Integer | No | Memory capacity, in `GB`. |
| CbsSupport | String | No | Whether the Cloud Block Storage is supported. Value range: <br><li>`TRUE`: supported;<br><li>`FALSE`: not supported. |
| InstanceTypeState | String | No | Model Status. Value range: <br><li>`AVAILABLE`: available; <br><li>` UNAVAILABLE`: not available. |


### ImageSharedAccount

> That the specified account is able to use the shared image is described.

| Name | Type | Required | Description |
|----|-----|---------|-----|
| ImageId | String | No | Image ID
| AccountId | String | No | Account ID


### Quota

> Information of quota is described.

| Name | Type | Required | Description |
|----|-----|---------|-----|
| QuotaId | String | No | Quota name. Value range: <br><li>`TOTAL_EIP_QUOTA`: The EIP quota for the user in the current region;<br><li>`DAILY_EIP_APPLY`: The number of requests for the user in the current region today;<br><li>`DAILY_PUBLIC_IP_ASSIGN`: The number of public IPs re-assigned for the user in the current region.
| QuotaCurrent | Integer | No | Current number of quotas
| QuotaLimit | Integer | No | Upper limit of the number of quotas


### Image

> An image is described.

| Name | Type | Required | Description |
|----|-----|---------|-----|
| ImageId | String | No | Image ID
| OsName | String | No | Operating system name.
| ImageSize | String | No | Operating system capacity (GIB)
| ImageType | Integer | No | Image type
| CreatedTime | String | No | Creation time
| ImageState | String | No | Image status
| imageName | String | No | Image name
| ImageDescription | String | No | Image description
| ImageSource | String | No | [Image Source](IMAGE_SOURCE).
| ImageCreator | String | No | Image creator

### AvailabilityZone

> Availability zone is described.

| Name | Type | Required | Description |
|----|-----|---------|------|
| RegionId | String | No | Region ID. |
| Zone | String | No | Availability zone ID. |
| ZoneName | String | No | Availability zone name. |
| ZoneState | String | No | Availability zone status. |


### KeyPair

> Information of key pair is described.

| Name | Type | Required | Description |
|----|-----|---------|------|
| KeyId | String | No | Key pair `ID`, the unique ID of the key pair. |
| KeyName | String | No | Key pair name. |
| ProjectId | String | No | `ID` of the project to which the key pair belongs. |
| Description | String | No | Key pair description. |
| PublicKey | String | No | The public key (in plain text) of the key pair. |
| PrivateKey | String | No | The private key (in plain text) of the key pair. Tencent Cloud will not retain user's private key. Please keep it well. |
| AssociatedInstanceIds | array of Strings | No | The list of `IDs` of instances associated with the key. |
| CreatedTime | Timestamp | No | Creation time. In accordance with the `ISO8601` standard, and use the` UTC` time, such as `YYYY-MM-DDThh: mm: ssZ`. |


### KeyPairInstancesinternetaccessible

> Relation between the key pair and the instance is described.

| Name | Type | Required | Description |
|----|-----|---------|------|
| KeyId | String | No | Key pair `ID`, the unique ID of the key pair. |
| AssociatedInstanceIdSet | array of Strings | No | The list of `IDs` of instances associated with the key pair. |


### Address

> EIP is described.

| Name | Type | Required | Description |
|----|-----|---------|------|
| AddressId | String | No | `EIP` `ID`, the unique ID of `EIP`. |
| AddressName | String | No | `EIP` name. |
| AddressState | String | No | `EIP` status. |
| AddressIp | String | No | Elastic public IP
| BindedResourceId | String | No | `ID` of the bound resource instance, such as a `CVM`, `NAT`, or ENI.
| CreatedTime | Timestamp | No | Creation time. In accordance with the `ISO8601` standard, and use the` UTC` time, such as `YYYY-MM-DDThh: mm: ssZ`. |

### InstanceChargeTypeConfig

> Instance billing is described.

| Name | Type | Required | Description |
|----|-----|---------|------|
| InstanceChargeType | String | No | Instance billing method. |
| Description | String | No | Description of instance billing method. |


### InternetChargeTypeConfig

> Network billing is described.

| Name | Type | Required | Description |
|----|-----|---------|------|
| InternetChargeType | String | No | Network billing method. |
| Description | String | No | Description of network billing method. |


### InternetBandwidthConfig

> Bandwidth billing is described.

| Name | Type | Required | Description |
|----|-----|---------|------|
| StartTime | Timestamp | No | Start time. In accordance with the `ISO8601` standard, and use the` UTC` time, such as `YYYY-MM-DDThh: mm: ssZ`. |
| EndTime | Timestamp | No | End Time. In accordance with the `ISO8601` standard, and use the` UTC` time, such as `YYYY-MM-DDThh: mm: ssZ`. |
| InternetAccessible | [InternetAccessible](#internetaccessible) | No | Instance bandwidth information. |

