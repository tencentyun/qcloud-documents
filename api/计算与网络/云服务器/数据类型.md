>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

### Placement

>? 描述了实例的抽象位置，包括其所在的可用区，所属的项目，宿主机等（仅CDH产品可用）

| 名称      |    类型 |  是否必选 | 描述|
|---------|---------|---------|---------|
|Zone|String|是|实例所属的 [可用区](https://cloud.tencent.com/document/product/213/15753#ZoneInfo) ID。该参数也可以通过调用  [DescribeZones](https://cloud.tencent.com/document/product/213/9455) 的返回值中的 Zone 字段来获取。|
|ProjectId|Integer|否|实例所属项目ID。该参数可以通过调用 [DescribeProject](/document/api/378/4400) 的返回值中的 projectId 字段来获取。不填为默认项目。|
|HostIds.N|array of Strings|否|实例所属的专用宿主机ID列表。如果您有购买专用宿主机并且指定了该参数，则您购买的实例就会随机的部署在这些专用宿主机上。当前暂不支持。|

### SystemDisk

>? 描述了操作系统所在块设备即系统盘的信息

| 名称      |    类型 |  是否必选 |描述|
|---------|---------|---------|---------|
|DiskType|String|否|系统盘类型。系统盘类型限制详见 [CVM 实例配置](https://cloud.tencent.com/document/product/213/11518)。取值范围：</br><li>LOCAL_BASIC：本地硬盘</br><li>LOCAL_SSD：本地SSD硬盘<br><li>CLOUD_BASIC：普通云硬盘</br><li>CLOUD_SSD：SSD云硬盘</br></br>默认取值：LOCAL_BASIC。|
|DiskId|String|否|系统盘ID。LOCAL_BASIC 和 LOCAL_SSD 类型没有ID。暂时不支持该参数。|
|DiskSize|Integer|否|系统盘大小，单位：GB。默认值为 50|


### DataDisk

>? 描述了数据盘的信息

| 名称      |    类型 |  是否必选 | 描述|
|---------|---------|---------|---------|
|DiskType|String|否|数据盘类型。数据盘类型限制详见 [CVM 实例配置](https://cloud.tencent.com/document/product/213/11518)。取值范围：</br><li>LOCAL_BASIC：本地硬盘</br><li>LOCAL_SSD：本地SSD硬盘</br><li>CLOUD_BASIC：普通云硬盘</br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_SSD：SSD云硬盘</br></br>默认取值：LOCAL_BASIC。</br></br>该参数对`ResizeInstanceDisk`接口无效。|
|DiskId|String|否|数据盘 ID。LOCAL_BASIC 和 LOCAL_SSD 类型没有ID。暂时不支持该参数。|
|DiskSize|Integer|是|数据盘大小，单位：GB。最小调整步长为10G，不同数据盘类型取值范围不同，具体限制详见：[CVM 实例配置](https://cloud.tencent.com/document/product/213/11518)。默认值为0，表示不购买数据盘。更多限制详见产品文档。|

### VirtualPrivateCloud

>? 描述了 VPC 相关信息，包括子网，IP信息等

| 名称      |    类型 |  是否必选 | 描述|
|---------|---------|---------|---------|
|VpcId|String|是|私有网络ID，形如`vpc-xxx`。有效的VpcId可通过登录 [控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1) 查询；也可以调用接口 [DescribeVpcEx](/document/api/215/1372) ，从接口返回中的`unVpcId`字段获取。|
|SubnetId|String|是|私有网络子网ID，形如`subnet-xxx`。有效的私有网络子网ID可通过登录 [控制台](https://console.cloud.tencent.com/vpc/subnet?rid=1) 查询；也可以调用接口  [DescribeSubnetEx](/document/api/215/1371) ，从接口返回中的`unSubnetId`字段获取。|
|AsVpcGateway|Boolean|否|是否用作公网网关。公网网关只有在实例拥有公网IP以及处于私有网络下时才能正常使用。取值范围：</br><li>TRUE：表示用作公网网关</br><li>FALSE：表示不用作公网网关</br></br>默认取值：FALSE。|
|PrivateIpAddresses.N|array of Strings|否|私有子网ip数组，目前只支持一个ip。在创建实例、修改实例vpc属性操作中可使用此参数。|


### InternetAccessible

>? 描述了实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等

| 名称      |    类型 |  是否必选 | 描述|
|---------|---------|---------|---------|
|InternetChargeType|String|否|网络计费类型。取值范围：</br><li>BANDWIDTH_PREPAID：预付费按带宽结算</br><li>TRAFFIC_POSTPAID_BY_HOUR：流量按小时后付费</br><li>BANDWIDTH_POSTPAID_BY_HOUR：带宽按小时后付费</br><li>BANDWIDTH_PACKAGE：带宽包用户</br>默认取值：TRAFFIC_POSTPAID_BY_HOUR。|
|InternetMaxBandwidthOut|Integer|否|公网出带宽上限，单位：Mbps。默认值：0Mbps。不同机型带宽上限范围不一致，具体限制详见 [购买网络带宽](https://cloud.tencent.com/document/product/213/10578)。|
|PublicIpAssigned|Boolean|否|是否分配公网IP。取值范围：</br><li>TRUE：表示分配公网IP</br><li>FALSE：表示不分配公网IP</br></br>当公网带宽大于0Mbps时，可自由选择开通与否，默认开通公网IP；当公网带宽为0，则不允许分配公网IP。|

### InstanceChargePrepaid

>? 描述了实例的计费模式

| 名称      |    类型 |  是否必选 |描述|
|---------|---------|---------|---------|
|Period|Integer|是|购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。|
|RenewFlag|String|否|自动续费标识。取值范围：</br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费</br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费</br></br>默认取值：NOTIFY_AND_AUTO_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。|


### LoginSettings

>? 描述了实例登录相关配置与信息

| 名称      |    类型 |  是否必选 |描述|
|---------|---------|---------|---------|
|Password|String|否|实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：</br><li>Linux实例密码必须8到16位，至少包括两项[a-z，A-Z]、[0-9] 和 [( ) &#96; ~ ! @ # $ % ^ & * - + = &#124; { } [ ] : ; ' , . ? / ]中的特殊符号。</br><li>Windows实例密码必须12到16位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) &#96; ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]中的特殊符号。</br></br>若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。|
|KeyIds.N|array of Strings|否|密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口DescribeKeyPairs获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。当前仅支持购买的时候指定一个密钥。|
|KeepImageLogin|String|否|保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为TRUE。取值范围：</br><li>TRUE：表示保持镜像的登录设置</br><li>FALSE：表示不保持镜像的登录设置</br></br>默认取值：FALSE。|


### RunSecurityServiceEnabled

>? 描述了 “云安全” 服务相关的信息

| 名称      |    类型 |  是否必选 |描述|
|---------|---------|---------|---------|
|Enabled|Boolean|否|是否开启 [云安全](/document/product/296) 服务。取值范围：</br><li>TRUE：表示开启云安全服务</br><li>FALSE：表示不开启云安全服务</br></br>默认取值：TRUE。|

### RunMonitorServiceEnabled

>? 描述了 “云监控” 服务相关的信息

| 名称      |    类型 |  是否必选 |描述|
|---------|---------|---------|---------|
|Enabled|Boolean|否|是否开启 [云监控](/document/product/248) 服务。取值范围：</br><li>TRUE：表示开启云监控服务</br><li>FALSE：表示不开启云监控服务</br></br>默认取值：TRUE。|

### EnhancedService

>? 描述了实例的增强服务启用情况与其设置，如云安全，云监控等实例 Agent

| 名称      |    类型 |  是否必选 |描述|
|---------|---------|---------|---------|
|SecurityService| [RunSecurityServiceEnabled](#runsecurityserviceenabled) object|否|开启云安全服务。若不指定该参数，则默认开启云安全服务。|
|MonitorService|[RunMonitorServiceEnabled](#runmonitorserviceenabled) object|否|开启云安全服务。若不指定该参数，则默认开启云监控服务。|

### ItemPrice

>? 描述了单项的价格信息

| 名称      |    类型 |  是否必选 |描述|
|---------|---------|---------|---------|
|UnitPrice|Float|否|后续单价，单位：元。|
|ChargeUnit|String|否|后续计价单元，可取值范围： </br><li>HOUR：表示计价单元是按每小时来计算。当前涉及该计价单元的场景有：实例按小时后付费（POSTPAID_BY_HOUR）、带宽按小时后付费（BANDWIDTH_POSTPAID_BY_HOUR）。</br><li>GB：表示计价单元是按每GB来计算。当前涉及该计价单元的场景有：流量按小时后付费（TRAFFIC_POSTPAID_BY_HOUR）。|
|OriginalPrice|Float|否|预支费用的原价，单位：元。|
|DiscountPrice|Float|否|预支费用的折扣价，单位：元。|

### Price

>? 价格

| 名称      |    类型 |  是否必选 |描述|
|---------|---------|---------|---------|
|InstancePrice|[ItemPrice](#itemprice) object|否|描述了实例价格。
|BandwidthPrice|[ItemPrice](#itemprice) object|否|描述了网络价格。

### Filter

>? 描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
> * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
> * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
>
> 以 [DescribeInstances](/document/api/213/9388) 接口的`Filter`为例。若我们需要查询可用区（`zone`）为广州一区**并且**实例计费模式（`instance-charge-type`）为包年包月**或者**按量计费的实例时，可如下实现：
```
Filters.1.Name=zone
&Filters.1.Values.1=ap-guangzhou-1
&Filters.2.Name=instance-charge-type
&Filters.2.Values.1=PREPAID
&Filters.2.Values.2=POSTPAID_BY_HOUR
```

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|-----|
| Name| String| 否| 过滤键的名称。|
| Values.N| array of Strings| 否| 一个或者多个过滤值。|

### InstanceStatus

>? 描述实例的状态。状态类型详见 [实例状态表](https://cloud.tencent.com/document/product/213/15753#InstanceStatus)

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|-----|
| InstanceId| String| 否| 实例`ID`。|
| InstanceState| String| 否| [实例状态](https://cloud.tencent.com/document/product/213/15753#InstanceStatus)。|

### Instance

>? 描述实例的信息

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|-----|
| Placement| [Placement](#placement)| 否| 实例所在的位置。|
| InstanceId| String| 否| 实例`ID`。|
| InstanceType| String| 否| 实例机型。|
| CPU| Integer| 否| 实例的CPU核数，单位：核。|
| Memory| Integer| 否| 实例内存容量，单位：`GB`。|
| RestrictState| String| 否| 实例业务状态。取值范围：</br><li>NORMAL：表示正常状态的实例</br><li>EXPIRED：表示过期的实例</br><li>PROTECTIVELY_ISOLATED：表示被安全隔离的实例。|
| InstanceName| String| 否| 实例名称。|
| InstanceChargeType| String| 否| 实例计费模式。取值范围：</br><li>`PREPAID`：表示预付费，即包年包月</br><li>`POSTPAID_BY_HOUR`：表示后付费，即按量计费</br><li>`CDHPAID`：`CDH`付费，即只对`CDH`计费，不对`CDH`上的实例计费。|
| SystemDisk| [SystemDisk](#systemdisk)| 否| 实例系统盘信息。|
| DataDisks| array of [DataDisk](#datadisk) objects| 否| 实例数据盘信息。只包含随实例购买的数据盘。|
| PrivateIpAddresses| array of Strings| 否| 实例主网卡的内网`IP`列表。|
| PublicIpAddresses| array of Strings| 否| 实例主网卡的公网`IP`列表。|
| InternetAccessible| [InternetAccessible](#internetaccessible)| 否| 实例带宽信息。|
| VirtualPrivateCloud| [VirtualPrivateCloud](#virtualprivatecloud)| 否| 实例所属虚拟私有网络信息。|
| ImageId| String| 否| 生产实例所使用的镜像`ID`。|
| RenewFlag| String| 否| 自动续费标识。取值范围：</br><li>`NOTIFY_AND_MANUAL_RENEW`：表示通知即将过期，但不自动续费</br><li>`NOTIFY_AND_AUTO_RENEW`：表示通知即将过期，而且自动续费</br><li>`DISABLE_NOTIFY_AND_MANUAL_RENEW`：表示不通知即将过期，也不自动续费。|
| CreatedTime| Timestamp| 否| 创建时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。|
| ExpiredTime| Timestamp| 否| 到期时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。|


### InstanceTypeConfig

>? 描述实例机型配置信息

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|-----|
| Zone| String| 否| 可用区。|
| InstanceType| String| 否| 实例机型。|
| InstanceFamily| String| 否| 实例机型系列。|
| CPU| Integer| 否| CPU核数，单位：核。|
| GPU| Integer| 否| GPU核数，单位：核。|
| FPGA| Integer| 否| FPGA核数，单位：核。|
| Memory| Integer| 否| 内存容量，单位：`GB`。|


### ImageSharedAccount

>? 描述了指定的账号能够使用该共享镜像

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|-----|
|ImageId|String|否|镜像ID
|AccountId|String|否|账户ID


### Quota

>? 描述了配额信息

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|-----|
|QuotaId|String|否|配额名称，取值范围：</br><li>`TOTAL_EIP_QUOTA`：用户当前地域下EIP的配额数；</br><li>`DAILY_EIP_APPLY`：用户当前地域下今日申购次数；</br><li>`DAILY_PUBLIC_IP_ASSIGN`：用户当前地域下，重新分配公网 IP次数。
|QuotaCurrent|Integer|否|当前数量
|QuotaLimit|Integer|否|配额数量


### Image

>? 描述了一个镜像

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|-----|
|ImageId|String|否|镜像ID
|OsName| String|否|操作系统名称
|ImageSize|String|否|操作系统容量（GiB）
|ImageType|Integer|否|镜像类型
|CreatedTime|String|否|创建时间
|ImageState|String|否|镜像状态
|ImageName|String|否| 镜像名称
|ImageDescription|String|否|镜像详细描述
|ImageSource|String| 否 |镜像来源。
|ImageCreator|String|否|镜像创建者

### AvailabilityZone

>? 描述可用区信息。

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|------|
| RegionId| String| 否| 地域ID。|
| Zone| String| 否| 可用区ID。|
| ZoneName| String| 否| 可用区名称。|
| ZoneState| String| 否| 可用区状态。|


### KeyPair

>? 描述密钥对信息

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|------|
| KeyId| String | 否| 密钥对的`ID`，是密钥对的唯一标识。 |
| KeyName| String | 否| 密钥对名称。 |
| ProjectId| String | 否| 密钥对所属的项目`ID`。 |
| Description| String | 否| 密钥对描述信息。 |
| PublicKey| String | 否| 密钥对的纯文本公钥。 |
| PrivateKey| String | 否| 密钥对的纯文本私钥。腾讯云不会保管私钥，请用户自行妥善保存。 |
| AssociatedInstanceIds| array of Strings| 否| 密钥关联的实例`ID`列表。|
| CreatedTime| Timestamp| 否| 创建时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。|


### KeyPairInstancesinternetaccessible

>? 描述密钥对和实例的关联关系

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|------|
| KeyId| String | 否| 密钥对的`ID`，是密钥对的唯一标识。|
| AssociatedInstanceIdSet| array of Strings | 否| 密钥对关联的实例`ID`列表。|


### Address

>? 描述 EIP 信息

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|------|
| AddressId| String | 否| `EIP`的`ID`，是`EIP`的唯一标识。 |
| AddressName| String | 否| `EIP`名称。 |
| AddressState| String | 否| `EIP`状态。 |
| AddressIp|String |否| 弹性外网IP
| BindedResourceId| String | 否| 绑定的资源实例`ID`。可能是一个`CVM`，`NAT`，或是弹性网卡。
| CreatedTime| Timestamp| 否| 创建时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。|

### InstanceChargeTypeConfig

>? 描述了实例计费

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|------|
| InstanceChargeType| String | 否| 实例计费模式。 |
| Description| String | 否| 实例计费模式描述信息。 |


### InternetChargeTypeConfig

>? 描述了网络计费

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|------|
| InternetChargeType| String | 否| 网络计费模式。 |
| Description| String | 否| 网络计费模式描述信息。 |


### InternetBandwidthConfig

>? 描述了按带宽计费的相关信息

| 名称| 类型| 是否必选 | 描述|
|----|-----|---------|------|
| StartTime| Timestamp | 否| 开始时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。 |
| EndTime| Timestamp | 否| 结束时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。 |
| InternetAccessible| [InternetAccessible](#internetaccessible)| 否| 实例带宽信息。|
