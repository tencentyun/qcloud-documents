## ActionTimer

Timed task

Used by actions: RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| Externals | [Externals](#Externals) | Yes | Extended data |
| TimerAction | String | No | Timer name. Only "TerminateInstances" is supported. |
| ActionTime | String | No | Execution time, which should be 5 minutes later than the current time. For example: 2018-5-29 11:26:40. |

## ChargePrepaid

Parameters related to Prepaid billing method, including purchased usage period, auto renewal logic, etc.

Used by actions: AllocateHosts, RenewHosts.

| Name | Type | Required | Description |
|------|------|----------|------|
| Period | Integer | Yes | Purchasable usage period of an instance (in month). Value range: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36. |
| RenewFlag | String | No | Auto renewal flag. Value range:<br><li>NOTIFY_AND_AUTO_RENEW: Notify expiry and renew automatically<br><li>NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify expiry nor renew automatically<br><br>Default: NOTIFY_AND_AUTO_RENEW. If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis when the account balance is sufficient. |

## DataDisk

Information on data disk

Used by actions: DescribeInstances, InquiryPriceResizeInstanceDisks, InquiryPriceRunInstances, ResizeInstanceDisks, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| DiskSize | Integer | Yes | Disk size (in GB). The minimum adjustment increment is 10 GB. Value ranges vary depending on different disk types. For more information on limits, please see [CVM Instance Configuration](/document/product/213/2177). Default is 0, indicating that no data disk is purchased. For more information on limits, please see relevant product documentation. |
| DiskType | String | No | Type of data disk. For more information about the limits on data disk types, please see [CVM Instance Configuration](/document/product/213/2177). Value range: <br><li>LOCAL_BASIC: Local disk<br><li>LOCAL_SSD: Local SSD disk<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_PREMIUM: Premium cloud storage<br><li>CLOUD_SSD: SSD cloud disk<br><br>Default value: LOCAL_BASIC.<br><br> This parameter is invalid for the API `ResizeInstanceDisk`. |
| DiskId | String | No | ID of data disk. Neither LOCAL_BASIC nor LOCAL_SSD comes with an ID. This parameter is not supported for now. |

## DisasterRecoverGroup

Information on disaster recovery group

Used by actions: DescribeDisasterRecoverGroups.

| Name | Type | Description |
|------|------|-------|
| DisasterRecoverGroupId | String | ID of a spread placement group. |
| Name | String | Name of a spread placement group with a length of 1-60 characters. |
| Type | String | Type of a spread placement group. Value range: <br><li>HOST: Physical machine<br><li>SW: Exchange<br><li>RACK: Rack |
| CvmQuotaTotal | Integer | Maximum number of CVMs that can be hosted in a spread placement group. |
| CurrentNum | Integer | Number of CVMs hosted in a spread placement group. |
| InstanceIds | Array of String | List of IDs of CVMs in a spread placement group. |
| CreateTime | Timestamp | Creation time of a spread placement group. |

## EnhancedService

The enabling conditions and settings of an instance's enhanced services, such as Cloud Security, Cloud Monitor and other instance agents.

Used by actions: InquiryPriceResetInstance, InquiryPriceRunInstances, ResetInstance, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| SecurityService | [RunSecurityServiceEnabled](#RunSecurityServiceEnabled) | No | Enables Cloud Security. If this parameter is not specified, the Cloud Security service is enabled by default. |
| MonitorService | [RunMonitorServiceEnabled](#RunMonitorServiceEnabled) | No | Enables Cloud Monitor. If this parameter is not specified, the Cloud Monitor service is enabled by default. |

## Externals

Extended data

Used by actions: DescribeZoneInstanceConfigInfos, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| ReleaseAddress | Boolean | No | Release address |
| UnsupportNetworks | Array of String | No | Network types that are not supported |
| StorageBlockAttr | [StorageBlock](#StorageBlock) | No | Attributes of local HDD storage |

## Filter

> Key-value pair filters for conditional filtering queries, such as filter ID, name, status, etc.
> * If more than one `Filter` exists, the relation between these `Filters` is a logical `AND`.
> * If there are multiple `Values` for only one `Filter`, the relation between these `Values` under the same `Filter` is a logical `OR`.
>
> Take the `Filter` in the API [DescribeInstances](https://cloud.tencent.com/document/api/213/9388) as an example. We can use the following filters to query the instance that resides in the availability zone (`zone`) of Guangzhou Zone 1 ***and*** is billed (`instance-charge-type`) on a prepaid basis ***or*** on a postpaid basis:
```
Filters.0.Name=zone
&Filters.0.Values.0=ap-guangzhou-1
&Filters.1.Name=instance-charge-type
&Filters.1.Values.0=PREPAID
&Filters.1.Values.1=POSTPAID_BY_HOUR
```

Used by actions: DescribeHosts, DescribeImages, DescribeInstanceTypeConfigs, DescribeInstances, DescribeKeyPairs, DescribeZoneInstanceConfigInfos.

| Name | Type | Required | Description |
|------|------|----------|------|
| Name | String | Yes | Fields to be filtered. |
| Values | Array of String | Yes | Filter values of the field. |

## HostItem

The details of a CDH instance

Used by actions: DescribeHosts.

| Name | Type | Description |
|------|------|-------|
| Placement | [Placement](#Placement) | Location of the CDH instance. This parameter is used to specify the availability zone and project to which the instance belongs. |
| HostId | String | CDH instance ID |
| HostType | String | CDH instance type |
| HostName | String | CDH instance name |
| HostChargeType | String | Billing type of a CDH instance |
| RenewFlag | String | Auto renewal flag of a CDH instance |
| CreatedTime | Timestamp | Creation time of a CDH instance |
| ExpiredTime | Timestamp | Expiration time of a CDH instance |
| InstanceIds | Array of String | List of IDs of CDH instances on which cloud servers have been created |
| HostState | String | CDH instance status |
| HostIp | String | CDH instance IP |
| HostResource | [HostResource](#HostResource) | The resource information of a CDH instance |

## HostResource

The resource information of a CDH instance

Used by actions: DescribeHosts.

| Name | Type | Description |
|------|------|-------|
| CpuTotal | Integer | Total number of CPU cores in a CDH instance |
| CpuAvailable | Integer | Number of available CPU cores in a CDH instance |
| MemTotal | Float | Total memory size in a CDH instance (in GiB) |
| MemAvailable | Float | Available memory size in a CDH instance (in GiB) |
| DiskTotal | Integer | Total disk size in a CDH instance (in GiB) |
| DiskAvailable | Integer | Available disk size in a CDH instance (in GiB) |

## Image

An array of detailed information of an image, including the main statuses and attributes of the image.

Used by actions: DescribeImages.

| Name | Type | Description |
|------|------|-------|
| CreatedTime | Timestamp | Creation time of an image |
| ImageName | String | Image name |
| ImageDescription | String | Image description |
| ImageSize | Integer | Image size |
| Architecture | String | Image architecture |
| ImageState | String | Image status |
| ImageId | String | Image ID |
| OsName | String | Image's operating system |
| ImageType | String | Image type |
| Platform | String | Image source platform |
| ImageCreator | String | Image creator |
| ImageSource | String | Image source |

## ImageOsList

Supported Windows/Linux operating systems.

Used by actions: DescribeImportImageOs.

| Name | Type | Description |
|------|------|-------|
| Windows | Array of String | Supported Windows operating systems |
| Linux | Array of String | Supported Linux operating systems |

## Instance

The information of an instance

Used by actions: DescribeInstances.

| Name | Type | Description |
|------|------|-------|
| OsName | String | Operating system name |
| SecurityGroupIds | Array of String | The security group to which an instance belongs. This parameter can be obtained from the sgId field in the returned values of [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808). |
| LoginSettings | [LoginSettings](#LoginSettings) | Login settings of an instance. Only the key associated with the instance is returned. |
| InstanceState | String | Instance status. Value range:<br><li>PENDING: Creating<br></li><li>LAUNCH_FAILED: Creation failed<br></li><li>RUNNING: Running<br></li><li>STOPPED: Shut down<br></li><li>STARTING: Starting up<br></li><li>STOPPING: Shutting down<br></li><li>REBOOTING: Restarting<br></li><li>SHUTDOWN: To be terminated<br></li><li>TERMINATING: Terminating<br></li> |
| Placement | [Placement](#Placement) | Location of an instance. |
| InstanceId | String | Instance `ID`. |
| InstanceType | String | Instance model. |
| CPU | Integer | Number of CPU cores in an instance (in core). |
| Memory | Integer | Instance memory capacity (in `GB`). |
| RestrictState | String | Instance business status. Value range:<br><li>NORMAL: Instance is normal<br><li>EXPIRED: Instance has expired<br><li>PROTECTIVELY_ISOLATED: Instance is isolated | |
| InstanceName | String | Instance name. |
| InstanceChargeType | String | Billing method of an instance. Value range: <br><li>`PREPAID`: Prepaid (by year/month) <br><li>`POSTPAID_BY_HOUR`: Postpaid (by traffic) <br><li>`CDHPAID`:` CDH` paid, i.e., only pay for `CDH`, excluding instances on the` CDH`. |
| SystemDisk | [SystemDisk](#SystemDisk) | Information of the instance's system disk. |
| DataDisks | Array of [DataDisk](#DataDisk) | Information of the instance's data disk. Only the data disk purchased with the instance is supported. |
| PrivateIpAddresses | Array of String | The list of private `IPs` of the instance's primary ENI. |
| PublicIpAddresses | Array of String | The list of public `IPs` of the instance's primary ENI. |
| InternetAccessible | [InternetAccessible](#InternetAccessible) | Instance bandwidth information. |
| VirtualPrivateCloud | [VirtualPrivateCloud](#VirtualPrivateCloud) | Information of the VPC to which the instance belongs. |
| ImageId | String | `ID` of the image used by the production instance. |
| RenewFlag | String | Auto renewal flag. Value range:<br><li>`NOTIFY_AND_MANUAL_RENEW`: Notify expiry but not renew automatically<br><li>`NOTIFY_AND_AUTO_RENEW`: Notify expiry and renew automatically<br><li>`DISABLE_NOTIFY_AND_MANUAL_RENEW`: Neither notify expiry nor renew automatically |
| CreatedTime | Timestamp | Creation time, in the format of `YYYY-MM-DDThh: mm: ssZ` according to the `ISO8601` standard. `UTC` time is used. |
| ExpiredTime | Timestamp | Expiration time, in the format of `YYYY-MM-DDThh: mm: ssZ` according to the `ISO8601` standard. `UTC` time is used. |

## InstanceChargePrepaid

The billing method of an instance

Used by actions: InquiryPriceModifyInstancesChargeType, InquiryPriceRenewInstances, InquiryPriceRunInstances, ModifyInstancesChargeType, RenewInstances, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| Period | Integer | Yes | Purchasable usage period of an instance (in month). Value range: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36. |
| RenewFlag | String | No | Auto renewal flag. Value range:<br><li>NOTIFY_AND_AUTO_RENEW: Notify expiry and renew automatically<br><li>NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify expiry nor renew automatically<br><br>Default: NOTIFY_AND_AUTO_RENEW. If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis when the account balance is sufficient. |

## InstanceFamilyConfig

The configuration information of an instance model family,
such as {'InstanceFamilyName': 'Standard S1', 'InstanceFamily': 'S1'}, {'InstanceFamilyName': 'Network Optimized N1', 'InstanceFamily': 'N1'}, {'InstanceFamilyName': 'High IO I1', 'InstanceFamily': 'I1'}, etc.

Used by actions: DescribeInstanceFamilyConfigs.

| Name | Type | Description |
|------|------|-------|
| InstanceFamilyName | String | Full name of a model family |
| InstanceFamily | String | Acronym of a model family |

## InstanceMarketOptionsRequest

Options related to spot requests

Used by actions: InquiryPriceRunInstances, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| MarketType | String | No | Market type. Only "spot" is supported. |
| SpotOptions | [SpotMarketOptions](#SpotMarketOptions) | No | Spot-related options |

## InstanceStatus

The status of an instance. For more information on status types, please see [List of Instance Statuses](/document/api/213/9452#INSTANCE_STATE)

Used by actions: DescribeInstancesStatus.

| Name | Type | Description |
|------|------|-------|
| InstanceId | String | Instance `ID`. |
| InstanceState | String | [Instance Status](/document/api/213/9452#INSTANCE_STATE). |

## InstanceTypeConfig

The configuration information of an instance model

Used by actions: DescribeInstanceTypeConfigs.

| Name | Type | Description |
|------|------|-------|
| Zone | String | Availability zone. |
| InstanceType | String | Instance model. |
| InstanceFamily | String | Instance model series. |
| GPU | Integer | Number of GPU cores (in core). |
| CPU | Integer | Number of CPU cores (in core). |
| Memory | Integer | Memory capacity (in `GB`). |
| CbsSupport | String | Whether the Cloud Block Storage is supported. Value range:<br><li>`TRUE`: Supported<br><li>`FALSE`: Not supported |
| InstanceTypeState | String | Model status. Value range:<br><li>`AVAILABLE`: Available<br><li>`UNAVAILABLE`: Not available |

## InstanceTypeQuotaItem

The quota information of an instance model.

Used by actions: DescribeZoneInstanceConfigInfos.

| Name | Type | Description |
|------|------|-------|
| Zone | String | Availability zone. |
| InstanceType | String | Instance model. |
| InstanceChargeType | String | Billing method of an instance. Value range: <br>*`PREPAID`: Prepaid (by year/month) <br>*`POSTPAID_BY_HOUR`: Postpaid (by traffic) * `CDHPAID`: [CDH](/document/product/416) paid, i.e., only pay for [CDH](/document/product/416), excluding instances on the [CDH](/document/product/416) |
| NetworkCard | Integer | ENI type. For example, 25 represents an ENI of 25 GB.
| Externals | [Externals](#Externals) | Scaled attributes. |
| Cpu | Integer | Number of CPU cores in an instance (in core). |
| Memory | Integer | Instance memory capacity (in `GB`). |
| InstanceFamily | String | Instance model series. |
| TypeName | String | Model name. |
| LocalDiskTypeList | Array of [LocalDiskType](#LocalDiskType) | List of local disk specifications. |
| Status | String | Whether an instance is sold. |
| Price | [ItemPrice](#ItemPrice) | Price of an instance. |

## InternetAccessible

The accessibility, billing method and maximum bandwidth for an instance on the public network

Used by actions: DescribeInstanceInternetBandwidthConfigs, DescribeInstances, InquiryPriceResetInstancesInternetMaxBandwidth, InquiryPriceRunInstances, ResetInstancesInternetMaxBandwidth, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| InternetChargeType | String | No | Network billing type. Value range:<br><li>BANDWIDTH_PREPAID: Prepaid by bandwidth<br><li>TRAFFIC_POSTPAID_BY_HOUR: Postpaid by traffic on an hourly basis<br><li>BANDWIDTH_POSTPAID_BY_HOUR: Postpaid by bandwidth on an hourly basis<br><li>BANDWIDTH_PACKAGE: Bandwidth package<br>Default: TRAFFIC_POSTPAID_BY_HOUR. |
| InternetMaxBandwidthOut | Integer | No | Bandwidth cap of the public network (in Mbps). Default: 0 Mbps. The bandwidth cap varies among different models. For more information, please see [Purchase Network Bandwidth](/document/product/213/509). |
| PublicIpAssigned | Boolean | No | Whether to assign public IP. Value range:<br><li>TRUE: Assign public IP<br><li>FALSE: Do not assign public IP<br><br>If the public network bandwidth is greater than 0 Mbps, you're free to choose whether to enable the public IP (which is enabled by default). If the public network bandwidth is 0 Mbps, the public IP is not assigned. |

## InternetBandwidthConfig

Information of bill-by-bandwidth method

Used by actions: DescribeInstanceInternetBandwidthConfigs.

| Name | Type | Description |
|------|------|-------|
| StartTime | Timestamp | Start time, in the format of `YYYY-MM-DDThh: mm: ssZ` according to the `ISO8601` standard. `UTC` time is used. |
| EndTime | Timestamp | End Time, in the format of `YYYY-MM-DDThh: mm: ssZ` according to the `ISO8601` standard. `UTC` time is used. |
| InternetAccessible | [InternetAccessible](#InternetAccessible) | Instance bandwidth information. |

## InternetChargeTypeConfig

Network billing

Used by actions: DescribeInternetChargeTypeConfigs.

| Name | Type | Required | Description |
|------|------|----------|------|
| InternetChargeType | String | No | Network billing method |
| Description | String | No | Description of network billing method |

## ItemPrice

The price of an item

Used by actions: DescribeZoneInstanceConfigInfos, InquiryPriceModifyInstancesChargeType, InquiryPriceRenewInstances, InquiryPriceResetInstance, InquiryPriceResetInstancesInternetMaxBandwidth, InquiryPriceResetInstancesType, InquiryPriceResizeInstanceDisks, InquiryPriceRunInstances.

| Name | Type | Description |
|------|------|-------|
| UnitPrice | Float | Subsequent unit price (in CNY) |
| ChargeUnit | String | Subsequent billing unit. Value Range: <br><li>HOUR: Bill by hour. Scenarios using this billing unit include: postpaid by hour (POSTPAID_BY_HOUR) and postpaid by bandwidth on an hourly basis (BANDWIDTH_POSTPAID_BY_HOUR).<br><li>GB: The billing unit is calculated in GB. The scenario using this billing unit is: postpaid by traffic on an hourly basis (TRAFFIC_POSTPAID_BY_HOUR). |
| OriginalPrice | Float | Original price of a prepaid instance (in CNY). |
| DiscountPrice | Float | Discount price of a prepaid instance (in CNY). |

## KeyPair

The information of a key pair

Used by actions: CreateKeyPair, DescribeKeyPairs.

| Name | Type | Description |
|------|------|-------|
| KeyId | String | Key pair `ID`, the unique ID of an key pair. |
| KeyName | String | Key pair name. |
| ProjectId | String | `ID` of the project to which a key pair belongs. |
| Description | String | Key pair description. |
| PublicKey | String | The public key (in plain text) of the key pair. |
| PrivateKey | String | The private key (in plain text) of the key pair. Tencent Cloud will not retain user's private key. Please keep it well. |
| AssociatedInstanceIds | Array of String | The list of `IDs` of instances associated with the key. |
| CreatedTime | Timestamp | Creation time, in the format of `YYYY-MM-DDThh: mm: ssZ` according to the `ISO8601` standard. `UTC` time is used. |

## LocalDiskType

Specifications of a local disk

Used by actions: DescribeZoneInstanceConfigInfos.

| Name | Type | Description |
|------|------|-------|
| Type | String | Type of a local disk. |
| PartitionType | String | Attributes of a local disk. |
| MinSize | Integer | Minimum size of a local disk. |
| MaxSize | Integer | Maximum size of a local disk. |

## LoginSettings

The configuration and information related to instance login.

Used by actions: DescribeInstances, InquiryPriceResetInstance, InquiryPriceRunInstances, ResetInstance, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| Password | String | No | Instance login password. Password complexity requirement varies with different operating systems, as shown below:<br><li>Password for a `Linux` instance should be a combination of 8 to 16 characters comprised of at least two of the following types: [a-z,A-Z], [0-9], and [( ) ` ~ ! @ # $ % ^ & * - + = &#124; { } [ ] : ; ' , . ? / ].<br><li> The password for a Windows instance should be a combination of 12-16 characters comprised of at least three of the following types: [a-z], [A-Z], [0-9] and [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /].<br><br> If this parameter is not specified, a password is randomly generated and sent to you via the internal message. |
| KeyIds | Array of String | No | List of key IDs. An instance associated with the key can be accessed using the corresponding private key. KeyId can be obtained via the API DescribeKeyPairs. A key and a password cannot be specified at the same time, and specifying key is not supported in Windows. You can specify only one key when purchasing the instance. |
| KeepImageLogin | String | No | Keep the original settings for an image. This parameter cannot be specified along with Password or KeyIds.N. You can specify this parameter to TRUE only when you create an instance using a custom image, shared image, or image imported from external resources. Value range:<br><li>TRUE: Keep the login settings for the image<br><li>FALSE: Do not keep the login settings for the image<br><br>Default: FALSE. |

## OsVersion

Supported operating system types.

Used by actions: DescribeImportImageOs.

| Name | Type | Description |
|------|------|-------|
| OsName | String | Operating system type |
| OsVersions | Array of String | Supported operating system version |
| Architecture | Array of String | Supported operating system architecture |

## Placement

The abstract location of an instance, including its availability zone, project, and host (CDH products only)

Used by actions: AllocateHosts, DescribeHosts, DescribeInstances, InquiryPriceRunInstances, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| Zone | String | Yes | ID of the [availability zone](/document/product/213/9452#zone) to which the instance belongs. This parameter can also be obtained from the Zone field in the returned values of [DescribeZones](/document/api/213/9455). |
| ProjectId | Integer | No | ID of the project to which the instance belongs. | This parameter can be obtained from the Zone field in the returned values of [DescribeProject](/document/api/378/4400). If this is left empty, default project is used. |
| HostIds | Array of String | No | The list of IDs of CDHs to which your instances belongs. If you have purchased CDHs and specified this parameter, the instances you purchased will be randomly deployed on these CDHs. |

## Price

Price

Used by actions: InquiryPriceModifyInstancesChargeType, InquiryPriceRenewInstances, InquiryPriceResetInstance, InquiryPriceResetInstancesInternetMaxBandwidth, InquiryPriceResetInstancesType, InquiryPriceResizeInstanceDisks, InquiryPriceRunInstances.

| Name | Type | Description |
|------|------|-------|
| InstancePrice | [ItemPrice](#ItemPrice) | Instance price |
| BandwidthPrice | [ItemPrice](#ItemPrice) | Network price |

## RegionInfo

Region information

Used by actions: DescribeRegions.

| Name | Type | Description |
|------|------|-------|
| Region | String | Region name. For example, ap-guangzhou |
| RegionName | String | Region description. For example, South China (Guangzhou) |
| RegionState | String | Whether the region is available |

## RunMonitorServiceEnabled

Information on the Cloud Monitor service

Used by actions: InquiryPriceResetInstance, InquiryPriceRunInstances, ResetInstance, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| Enabled | Boolean | No | Whether to enable [Cloud Monitor](/document/product/248) service. Value range:<br><li>TRUE: Enable<br><li>FALSE: Do not enable<br><br>Default: TRUE. |

## RunSecurityServiceEnabled

Information on the Cloud Security service

Used by actions: InquiryPriceResetInstance, InquiryPriceRunInstances, ResetInstance, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| Enabled | Boolean | No | Whether to enable [Cloud Security](/document/product/296) service. Value range:<br><li>TRUE: Enable<br><li>FALSE: Do not enable<br><br>Default: TRUE. |

## SharePermission

An array of information on image sharing

Used by actions: DescribeImageSharePermission.

| Name | Type | Description |
|------|------|-------|
| CreateTime | Timestamp | The time when the image is shared |
| Account | String | ID of the account to which the image is shared |

## SpotMarketOptions

Spot-related options

Used by actions: InquiryPriceRunInstances, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| MaxPrice | String | Yes | Bid rate |
| SpotInstanceType | String | No | Spot request type. Only "one-time" is supported. |

## StorageBlock

Information of local HDD storage

Used by actions: DescribeZoneInstanceConfigInfos, RunInstances.

| Name | Type | Description |
|------|------|-------|
| Type | String | Type of local HDD storage. Value: LOCAL_PRO. |
| MinSize | Integer | Minimum size of local HDD storage |
| MaxSize | Integer | Maximum size of local HDD storage |

## SystemDisk

Information on the block device (the system disk) where the operating system is located

Used by actions: DescribeInstances, InquiryPriceResetInstance, InquiryPriceRunInstances, ResetInstance, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| DiskType | String | No | Type of system disk. For information about the limits on system disk types, please see [CVM Instance Configuration](/document/product/213/2177). Value range:<br><li>LOCAL_BASIC: Local disk<br><li>LOCAL_SSD: Local SSD disk<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_PREMIUM: Premium cloud storage<br><li>CLOUD_SSD: SSD cloud disk<br><br>Default value: LOCAL_BASIC. |
| DiskId | String | No | System disk ID. Neither LOCAL_BASIC nor LOCAL_SSD comes with an ID. This parameter is not supported for now. |
| DiskSize | Integer | No | System disk size (in GB). Default is 50 |

## Tag

Tag key-value pair

Used by actions: InquiryPriceRunInstances, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| Key | String | Yes | Tag key |
| Value | String | Yes | Tag value |

## TagSpecification

The tag pair bound to a CVM instance that is being created

Used by actions: InquiryPriceRunInstances, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| ResourceType | String | Yes | Type of resource bound to a tag. Only type "instance" is supported |
| Tags | Array of [Tag](#Tag) | Yes | List of tag pairs |

## VirtualPrivateCloud

VPC-related information, including subnet, IP, etc.

Used by actions: DescribeInstances, InquiryPriceRunInstances, RunInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| VpcId | String | Yes | VPC ID, in the format of `vpc-xxx`. A valid VPC ID can be queried through the [console](https://console.cloud.tencent.com/vpc/vpc?rid=1) or obtained from the `unVpcId` field returned by the API [DescribeVpcEx](/document/api/215/1372). |
| SubnetId | String | Yes | VPC subnet ID, in the format of `subnet-xxx`. A valid VPC subnet ID can be queried through the [console](https://console.cloud.tencent.com/vpc/subnet?rid=1) or obtained from the `unSubnetId` field returned by the API [DescribeSubnets](/document/api/215/15784). |
| AsVpcGateway | Boolean | No | Whether used as a public gateway. The public gateway can be used only when the instance has a public IP and resides in a VPC. Value range:<br><li>TRUE: Used as a public gateway<br><li>FALSE: Do not used as a public gateway<br><br>Default: FALSE. |
| PrivateIpAddresses | Array of String | No | Array of VPC subnet IPs. This parameter can be used to create instances and modify VPC attributes for instances. Multiple IPs of a same subnet can be passed only when instances are created in batches. |

## ZoneInfo

The information on an availability zone

Used by actions: DescribeZones.

| Name | Type | Description |
|------|------|-------|
| Zone | String | Availability zone name. For example, ap-guangzhou-3 |
| ZoneName | String | Availability zone description. For example, Guangzhou Zone 3 |
| ZoneId | String | Availability zone ID |
| ZoneState | String | Availability zone status |


