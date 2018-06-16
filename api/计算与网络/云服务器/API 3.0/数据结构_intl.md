## ActionTimer

Timed task

| Name | Type | Required | Description |
|------|------|----------|------|
| TimerAction | String | No | Timer |
| ActionTime | String | No | Execution time |
| Externals | Externals | Yes | Extended data |

## ChargePrepaid

Parameters related to Prepaid billing method, including usage period, auto renewal logic, etc.

| Name | Type | Required | Description |
|------|------|----------|------|
| Period | Integer | Yes | Purchased usage period of an instance (in month). Value range: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36. |
| RenewFlag | String | No | Auto renewal flag. Value range:<li>NOTIFY_AND_AUTO_RENEW: Notify expiry and renew automatically</li><li>NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically</li><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify expiry nor renew automatically</li><br>Default: NOTIFY_AND_AUTO_RENEW. If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis when the account balance is sufficient. |

## DataDisk

Information on data disk

| Name | Type | Required | Description |
|------|------|----------|------|
| DiskType | String | No | Type of system disk. For information on limits of data disk type, please see [CVM Instance Configuration](/document/product/213/2177). Value range:<li>LOCAL_BASIC: Local disk</li><li>LOCAL_SSD: Local SSD disk</li><li>CLOUD_BASIC: HHD cloud disk</li><li>CLOUD_PREMIUM: Premium cloud storage</li><li>CLOUD_SSD: SSD cloud disk</li><br>Default: LOCAL_BASIC.<br><br>This parameter is invalid for the API `ResizeInstanceDisk`. |
| DiskId | String | No | System disk ID. LOCAL_BASIC and LOCAL_SSD do not have an ID. This parameter is not supported for now. |
| DiskSize | Integer | Yes | Data disk size (in GB). The minimum increment in which the adjustment is made is 10 GB. Different types of data disks have different value ranges. For information on limits, please see [CVM Instance Configuration](/document/product/213/2177). The default is 0, which means that no data disk is purchased. For more information, please see the product documentation. |

## EnhancedService

The enabling conditions and settings of instance's enhanced services, such as Cloud Security, Cloud Monitor and other instance agents.

| Name | Type | Required | Description |
|------|------|----------|------|
| SecurityService | RunSecurityServiceEnabled | No | Enable the Cloud Security service. If this parameter is not specified, the Cloud Security service is enabled by default. |
| MonitorService | RunMonitorServiceEnabled | No | Enable the Cloud Security service. If this parameter is not specified, the Cloud Monitor service is enabled by default. |

## Externals

Extended data

| Name | Type | Required | Description |
|------|------|----------|------|
| ReleaseAddress | Boolean | No | Release address |

## Filter

>Key-value pair filters for conditional filtering queries, such as filtering ID, name, status, etc.
> * If more than one `Filter` exists, the relation between these `Filters` is a logical `AND`.
> * If there are multiple `Values` for only one `Filter`, the relation between these `Values` under the same `Filter` is a logical `OR`.
>
> Take the `Filter` in the API [DescribeInstances](/document/api/213/9388) as an example. If the instance to be queried resides in the available zone (`zone`) of Guangzhou Zone 1 ***and*** is billed (`instance-charge-type`) on a prepaid basis ***or*** on a postpaid basis, then the query can be implemented as follows:
```
Filters.1.Name=zone
&Filters.1.Values.1=ap-guangzhou-1
&Filters.2.Name=instance-charge-type
&Filters.2.Values.1=PREPAID
&Filters.3.Values.2=POSTPAID_BY_HOUR
```

| Name | Type | Required | Description |
|------|------|----------|------|
| Name | String | Yes | The field needs to be filtered. |
| Values | Array of String | Yes | Filter values of the field. |

## HostItem

The details of a CDH instance

| Name | Type | Required | Description |
|------|------|----------|------|
| Placement | Placement | No | Location of CDH instance. This parameter is used to specify the availability zone, project and other attributes of the instance. |
| HostId | String | No | ID of CDH instance |
| HostType | String | No | Type of CDH instance |
| HostName | String | No | Name of CDH instance |
| HostChargeType | String | No | Billing method of CDH instance |
| RenewFlag | String | No | Auto renewal flag of CDH instance |
| CreatedTime | Timestamp | No | Creation time of CDH instance |
| ExpiredTime | Timestamp | No | Expiration time of CDH instance |
| InstanceIds | String | No | List of instance IDs for the cloud servers that have been created on CDH instance |
| HostState | String | No | Status of CDH instance |
| HostIp | String | No | IP of CDH instance |
| HostResource | HostResource | No | Resource information of CDH instance |

## HostResource

The resource information of a CDH instance

| Name | Type | Required | Description |
|------|------|----------|------|
| CpuTotal | Integer | No | Total number of CPU cores in the CDH instance |
| CpuAvailable | Integer | No | Number of CPU cores available in the CDH instance |
| MemTotal | Float | No | Total memory size in the CDH instance (in GiB) |
| MemAvailable | Float | No | Total memory size available in the CDH instance (in GiB) |
| DiskTotal | Integer | No | Total disk size in the CDH instance (in GiB) |
| DiskAvailable | Integer | No | Total disk size available in the CDH instance (in GiB) |

## Image

An array of the details of an image, including the main statuses and attributes of the image.

| Name | Type | Required | Description |
|------|------|----------|------|
| ImageId | String | No | Image ID |
| OsName | String | No | Image's operating system |
| ImageType | String | No | Image type |
| CreatedTime | Timestamp | Yes | Creation time of image |
| imageName | String | Yes | Image name |
| ImageDescription | String | Yes | Image description |
| ImageSize | Integer | Yes | Image size |
| Architecture | String | Yes | Image architecture |
| ImageState | String | Yes | Image status |
| Platform | String | No | Image source platform |
| ImageCreator | String | No | Image creator |
| ImageSource | String | No | Image source |

## Instance

The information of an instance

| Name | Type | Required | Description |
|------|------|----------|------|
| Placement | Placement | No | Location of the instance. |
| InstanceId | String | No | Instance `ID`. |
| InstanceType | String | No | Instance model. |
| CPU | Integer | No | Number of CPU cores in the instance (in core). |
| Memory | Integer | No | Instance memory capacity (in `GB`). |
| RestrictState | String | No | Instance business status. Value range:<li>NORMAL: Instance is normal</li><li>EXPIRED: Instance expired</li><li>PROTECTIVELY_ISOLATED: Instance is isolated</li> |
| InstanceName | String | No | Instance name. |
| InstanceChargeType | String | No | Instance billing method. Value range:<li>`PREPAID`: Prepaid</li><li>`POSTPAID_BY_HOUR`: Postpaid</li><li>`CDHPAID`: `CDH` paid, i.e., only pay for `CDH`, excluding instances on the `CDH`. |
| SystemDisk | SystemDisk | No | Information of the system disk in the instance. |
| DataDisks | Array of DataDisk | No | Information of the data disk in the instance, only including the data disks purchased along with the instance. |
| PrivateIpAddresses | Array of String | No | The list of private `IPs` of the instance's primary ENI. |
| PublicIpAddresses | Array of String | No | The list of public `IPs` of the instance's primary ENI. |
| InternetAccessible | InternetAccessible | No | Instance bandwidth information. |
| VirtualPrivateCloud | VirtualPrivateCloud | No | Information of the VPC to which the instance belongs. |
| ImageId | String | No | Image `ID` used by the production instance. |
| RenewFlag | String | No | Auto renewal flag. Value range:<li>`NOTIFY_AND_MANUAL_RENEW`: Notify expiry but not renew automatically</li><li>`NOTIFY_AND_AUTO_RENEW`: Notify expiry and renew automatically</li><li>`DISABLE_NOTIFY_AND_MANUAL_RENEW`: Neither notify expiry nor renew automatically. |
| CreatedTime | Timestamp | No | Creation time, in the format of `YYYY-MM-DDThh:mm:ssZ` according to `ISO8601` standard. `UTC` time is used. |
| ExpiredTime | Timestamp | No | Expiration time, in the format of `YYYY-MM-DDThh:mm:ssZ` according to `ISO8601` standard. `UTC` time is used. |

## InstanceChargePrepaid

The billing method of an instance

| Name | Type | Required | Description |
|------|------|----------|------|
| Period | Integer | Yes | Purchased usage period of an instance (in month). Value range: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36. |
| RenewFlag | String | No | Auto renewal flag. Value range:<li>NOTIFY_AND_AUTO_RENEW: Notify expiry and renew automatically</li><li>NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically</li><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify expiry nor renew automatically</li><br>Default: NOTIFY_AND_AUTO_RENEW. If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis when the account balance is sufficient. |

## InstanceFamilyConfig

The configuration information of an instance model family, 
such as {'InstanceFamilyName': 'Standard S1', 'InstanceFamily': 'S1'}, {'InstanceFamilyName': 'Network Optimized N1', 'InstanceFamily': 'N1'}, {'InstanceFamilyName': 'High IO I1', 'InstanceFamily': 'I1'}, etc.

| Name | Type | Required | Description |
|------|------|----------|------|
| InstanceFamilyName | String | Yes | Full name of a model family. |
| InstanceFamily | String | Yes | Acronym of model family. |

## InstanceStatus

The status of an instance. For more information on status types, please see [Table of Instance Statuses](/document/api/213/9452#INSTANCE_STATE).

| Name | Type | Required | Description |
|------|------|----------|------|
| InstanceId | String | No | Instance `ID`. |
| InstanceState | String | No | [Instance Status](/document/api/213/9452#INSTANCE_STATE). |

## InstanceTypeConfig

The configuration information of an instance model

| Name | Type | Required | Description |
|------|------|----------|------|
| Zone | String | No | Availability zone. |
| InstanceType | String | No | Instance model. |
| InstanceFamily | String | No | Instance model series. |
| GPU | Integer | No | Number of GPU cores (in core). |
| CPU | Integer | No | Number of CPU cores (in core). |
| Memory | Integer | No | Memory capacity (in `GB`). |
| CbsSupport | String | No | Whether the Cloud Block Storage is supported. Value range:<li>`TRUE`: Supported.</li><li>`FALSE`: Not supported.</li> |
| InstanceTypeState | String | No | Model status. Value range:<li>`AVAILABLE`: Available.</li><li>`UNAVAILABLE`: Not available.</li> |

## InternetAccessible

The accessibility, billing method and maximum bandwidth for an instance on the public network

| Name | Type | Required | Description |
|------|------|----------|------|
| InternetChargeType | String | No | Network billing type. Value range:<li>BANDWIDTH_PREPAID: Prepaid by bandwidth</li><li>TRAFFIC_POSTPAID_BY_HOUR: Postpaid by traffic on an hourly basis</li><li>BANDWIDTH_POSTPAID_BY_HOUR: Postpaid by bandwidth on an hourly basis</li><li>BANDWIDTH_PACKAGE: Bandwidth package</li>Default: TRAFFIC_POSTPAID_BY_HOUR. |
| InternetMaxBandwidthOut | Integer | No | The maximum outbound bandwidth of the public network (in Mbps). Default is 0 Mbps. The upper limit of bandwidth varies with different models. For more information, please see [Purchase Network Bandwidth](/document/product/213/509). |
| PublicIpAssigned | Boolean | No | Whether to assign public IP. Value range:<li>TRUE: Assign public IP</li><li>FALSE: Not assign public IP</li><br>If the public network bandwidth is greater than 0 Mbps, you are free to choose whether to enable the public IP (which is enabled by default). If the public network bandwidth is 0 Mbps, the public IP is not assigned. |

## InternetBandwidthConfig

The information of bill-by-bandwidth method.

| Name | Type | Required | Description |
|------|------|----------|------|
| StartTime | Timestamp | No | Start time, in the format of `YYYY-MM-DDThh:mm:ssZ` according to the `ISO8601` standard. `UTC` time is used. |
| EndTime | Timestamp | No | End time, in the format of `YYYY-MM-DDThh:mm:ssZ` according to the `ISO8601` standard. `UTC` time is used. |
| InternetAccessible | InternetAccessible | No | Instance bandwidth information. |

## InternetChargeTypeConfig

Network billing

| Name | Type | Required | Description |
|------|------|----------|------|
| InternetChargeType | String | No | Network billing method. |
| Description | String | No | Description of network billing method. |

## ItemPrice

The price of an item

| Name | Type | Required | Description |
|------|------|----------|------|
| UnitPrice | Float | No | Subsequent unit price (in CNY). |
| ChargeUnit | String | No | Subsequent billing unit. Value Range:<li>HOUR: Bill by hour. Scenarios using this billing unit include: postpaid by hour (POSTPAID_BY_HOUR), and postpaid by bandwidth on an hourly basis (BANDWIDTH_POSTPAID_BY_HOUR).</li><li>GB: Bill by traffic (in GB). Scenarios using this billing unit include: postpaid by traffic on an hourly basis (TRAFFIC_POSTPAID_BY_HOUR). |
| OriginalPrice | Float | No | Original price of prepaid expenses (in CNY). |
| DiscountPrice | Float | No | Discount price of prepaid expenses (in CNY). |

## KeyPair

The information of a key pair

| Name | Type | Required | Description |
|------|------|----------|------|
| KeyId | String | No | The unique `ID` of the key pair. |
| KeyName | String | No | The name of the key pair. |
| ProjectId | String | No | `ID` of the project to which the key pair belongs. |
| Description | String | No | The description of the key pair. |
| PublicKey | String | No | The public key (in plain text) of the key pair. |
| PrivateKey | String | No | The private key (in plain text) of the key pair. Tencent Cloud does not retain your private key. Please keep it well. |
| AssociatedInstanceIds | Array of Strings | No | The list of `IDs` of instances associated with the key. |
| CreatedTime | Timestamp | No | Creation time, in the format of `YYYY-MM-DDThh:mm:ssZ` according to `ISO8601` standard. `UTC` time is used. |

## LoginSettings

The configuration and information related to instance login.

| Name | Type | Required | Description |
|------|------|----------|------|
| Password | String | No | Login password of the instance. The rule of password complexity varies with different operating systems:<li>For Linux instances, the password must be a combination of 8-16 characters comprised of at least two of the following types: [a-z, A-Z], [0-9] and [( ) &#39; ~ ! @ # $ % ^ & * - + = &#124; { } [ ] : ; ' , . ? / ].</li><li>For Windows instances, the password must be a combination of 12-16 characters comprised of at least three of the following types: [a-z], [A-Z], [0-9] and [( ) &#39; ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /].</li><br>If this parameter is not specified, a random password is generated and notified to the user via the internal message. |
| KeyIds | Array of String | No | List of key Ids. An instance associated with the key can be accessed using the corresponding private key. KeyId can be obtained via the API DescribeKeyPairs. A key and a password cannot be specified at the same time, and specifying key is not supported in Windows. You can specify only one key when purchasing an instance. |
| KeepImageLogin | String | No | Keep the original settings of the image. This parameter cannot be specified along with Password or KeyIds.N. You can specify this parameter to TRUE only if you create an instance using a custom image, shared image, or image imported from external resources. Value range:<li>TRUE: Keep the original login settings of the image</li><li>FALSE: Not keep the original login settings of the image</li><br>Default: FALSE. |

## Placement

The abstract location of an instance, including its availability zone, project, host, etc. (CDH products only)

| Name | Type | Required | Description |
|------|------|----------|------|
| Zone | String | Yes | ID of the [Availability Zone](/document/product/213/9452#zone) to which the instance belongs. This parameter can be obtained from the Zone field in the returned values of [DescribeZones](/document/api/213/9455). |
| ProjectId | Integer | No | ID of the project to which the instance belongs. This parameter can be obtained from the projectId field in the returned values of [DescribeProject](/document/api/378/4400). If this is left empty, default project is used. |
| HostIds.| Array of String | No | The list of IDs of CDHs to which the instance belongs. If you have purchased CDHs and specified this parameter, the instance you purchased is randomly deployed on these CDHs. It is not supported for now. |

## Price

Price

| Name | Type | Required | Description |
|------|------|----------|------|
| InstancePrice | ItemPrice | No | Instance price. |
| BandwidthPrice | ItemPrice | No | Network price. |

## RegionInfo

Region information

| Name | Type | Required | Description |
|------|------|----------|------|
| Region | String | Yes | Region name, e.g. ap-guangzhou |
| RegionName | String | Yes | Region description, e.g. South China (Guangzhou) |
| RegionState | String | Yes | Whether the region is available |

## RunMonitorServiceEnabled

Information on the Cloud Monitor service

| Name | Type | Required | Description |
|------|------|----------|------|
| Enabled | Boolean | No | Whether to enable [Cloud Monitor](/document/product/248). Value range:<li>TRUE: Enable Cloud Monitor</li><li>FALSE: Not enable Cloud Monitor</li><br>Default: TRUE. |

## RunSecurityServiceEnabled

Information on the Cloud Security service

| Name | Type | Required | Description |
|------|------|----------|------|
| Enabled | Boolean | No | Whether to enable [Cloud Security](/document/product/296). Value range: <li>TRUE: Enable Cloud Security</li><li>FALSE: Not enable Cloud Security</li><br>Default: TRUE. |

## SharePermission

An array of information on image sharing

| Name | Type | Required | Description |
|------|------|----------|------|
| CreateTime | Timestamp | Yes | The time when the image is shared |
| Account | String | Yes | ID of the account to which the image is shared |

## SystemDisk

Information on the block device (the system disk) where the operating system is located

| Name | Type | Required | Description |
|------|------|----------|------|
| DiskType | String | No | System disk type. For information on limits of system disk type, please see [CVM Instance Configuration](https://cloud.tencent.com/document/product/213/2177). Value range:<li>LOCAL_BASIC: Local disk</li><li>LOCAL_SSD: Local SSD disk</li><li>CLOUD_BASIC: HDD cloud disk</li><li>CLOUD_SSD: SSD cloud disk</li><br>Default value: LOCAL_BASIC. |
| DiskId | String | No | System disk ID. LOCAL_BASIC and LOCAL_SSD do not have an ID. This parameter is not supported for now. |
| DiskSize | Integer | No | System disk size (in GB). Default is 50. |

## Tag

Tag key-value pair

| Name | Type | Required | Description |
|------|------|----------|------|
| Key | String | Yes | Tag key |
| Value | String | Yes | Tag value |

## TagSpecification

The tag pair bound to a CVM instance that is being created

| Name | Type | Required | Description |
|------|------|----------|------|
| ResourceType | String | Yes | Type of resource bound to the tag |
| Tags | Array of Tag | Yes | List of tag pairs |

## VirtualPrivateCloud

VPC-related information, including subnet, IP, etc.

| Name | Type | Required | Description |
|------|------|----------|------|
| VpcId | String | Yes | Private network ID, such as `vpc-xxx`. A valid VpcId can be queried by logging in to the [console](https://console.cloud.tencent.com/vpc/vpc?rid=1) or obtained from the `unVpcId` field returned via the API [DescribeVpcEx](/document/api/215/1372). |
| SubnetId | String | Yes | Private network subnet ID, such as `subnet-xxx`. A valid subnet ID can be queried by logging in to the [console](https://console.cloud.tencent.com/vpc/vpc?rid=1) or obtained from the `unSubnetId` field returned via the API [DescribeSubnetEx](/document/api/215/1371). |
| AsVpcGateway | Boolean | No | Whether used as a public gateway. The public gateway can be used only when the instance has a public IP and resides in a VPC. Value range:<li>TRUE: Used as public gateway</li><li>FALSE: Not used as public gateway</li><br>Default: FALSE. |
| PrivateIpAddresses.| Array of String | No | Array of VPC subnet IPs. Only one IP is supported. This parameter can be used to create instances and modify VPC attributes for instances. |

## ZoneInfo

The information on an availability zone

| Name | Type | Required | Description |
|------|------|----------|------|
| Zone | String | Yes | Name of availability zone, e.g. ap-guangzhou-3 |
| ZoneName | String | Yes | Description of availability zone, e.g. Guangzhou Zone 3 |
| ZoneId | String | Yes | Availability zone ID |
| ZoneState | String | Yes | Availability zone status. |

