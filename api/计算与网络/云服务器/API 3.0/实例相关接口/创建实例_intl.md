
## 1. API Description

This API (RunInstances) is used to create one or more instances with specified configuration.

* After the instance is created successfully, it will start on boot and the [instance status](/document/api/213/9452#instance_state) will become "running".
* For an instance purchased on a prepaid basis, the required amount for the purchased instance will be pre-deducted; for an instance purchased on an hourly and postpaid basis, an amount equal to an hourly rate of the instance will be pre-frozen. Make sure your account balance is sufficient before calling this API.
* The instances allowed to be purchased by this API are subject to the number limit described in the [Restrictions on CVM Instance Purchase](https://cloud.tencent.com/document/product/213/2664), and share the quota with the instances created by the official website entry.
* This API is an asynchronous API. An instance `ID` list will be returned when the creation request is issued successfully, but the instance is not created immediately. During this period, the status of the instance is "Pending". You can call API [DescribeInstancesStatus](https://cloud.tencent.com/document/api/213/15738) to query the status of the instance to check whether it is created. If the status changes from "Pending" to "Running", the instance is created successfully.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: RunInstances |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceChargeType | No | String | Instance [billing type](https://cloud.tencent.com/document/product/213/2180).<li>PREPAID: prepaid (by year/month)</li><li>POSTPAID_BY_HOUR: postpaid by hour</li><li>CDHPAID: exclusive parent host billing (based on the creation of CDH, and CDH resources are free of charge)</li>Default value: POSTPAID_BY_HOUR. |
| InstanceChargePrepaid | No | [InstanceChargePrepaid](/document/api/213/15753#InstanceChargePrepaid) | Prepaid mode, which is the relevant parameter setting for prepaid mode. This parameter can specify the purchased usage period, whether to set automatic renewal and other attributes of the instance purchased on a prepaid basis. This parameter is mandatory if the billing method for the specified instance is prepaid. |
| Placement | Yes | [Placement](/document/api/213/15753#Placement) | Location of the instance. This parameter is used to specify the availability zone, the project to which the instance belongs, and the CDH (the creation of sub-machine for the exclusive parent host billing mode), etc. |
| InstanceType | No | String | Instance model. Different instance models specify different resource specifications.<br><br><li>For the creation of sub-machine on the PREPAID or POSTPAID_BY_HOUR basis, specific values can be found in the latest specifications by calling the API [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749) or in [Instance Type](https://cloud.tencent.com/document/product/213/11518). If this parameter is not specified, the default model is S1.SMALL1.</li><li>For the creation of sub-machine on the CDHPAID basis, the prefix of the parameter value is "CDH_". The parameter value is in the format of CDH_XCXG based on the CPU and memory configuration. For example, if a sub-machine of CDH is created with a single-core CPU and 1 GB memory, its value should be CDH_1C1G</li> |
| ImageId | Yes | String | Valid [image](https://cloud.tencent.com/document/product/213/4940) ID, such as `img-xxx`. There are four types of images:<li>Public Images</li><li>Custom Images</li><li>Shared Images</li><li>Marketplace Images</li><br>You can obtain the available image IDs by the following ways:<li>For `public images`, `custom images` and `shared images`, log in to [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the image IDs; for `marketplace images`, query the image IDs through [Cloud Marketplace](https://market.cloud.tencent.com/list).</li><li>This value can be obtained from the `ImageId` field in the returned values of API [DescribeImages](https://cloud.tencent.com/document/api/213/15715).</li> |
| SystemDisk | No | [SystemDisk](/document/api/213/15753#SystemDisk) | Configuration information of instance's system disk. If the parameter is not specified, the default value is assigned to it. |
| DataDisks.N | No | Array of [DataDisk](/document/api/213/15753#DataDisk) | Configuration information of the instance data disk. If the parameter is not specified, no data disk will be purchased by default. You can specify only one data disk when purchasing it. |
| VirtualPrivateCloud | No | [VirtualPrivateCloud](/document/api/213/15753#VirtualPrivateCloud) | Configuration information of VPC. This parameter is used to specify VPC ID and subnet ID, etc. If this parameter is not specified, the basic network is used by default. If a VPC IP is specified in this parameter, it indicates the primary ENI IP of each instance and the value of parameter InstanceCount must be same as the number of VPC IPs. |
| InternetAccessible | No | [InternetAccessible](/document/api/213/15753#InternetAccessible) | Configuration information of public network bandwidth. If this parameter is not specified, the default public network bandwidth is 0 Mbps. |
| InstanceCount | No | Integer | Number of instances to be purchased. Value range: [1, 100]. Default value: 1. The specified number of instances to be purchased cannot exceed the remaining quota allowed for the user, For more information about quota restrictions, please see [Restrictions on CVM Instance Purchase](https://cloud.tencent.com/document/product/213/2664). |
| InstanceName | No | String | The display name of the instance. If this name of instance is not specified, the name of instance is displayed by default. |
| LoginSettings | No | [LoginSettings](/document/api/213/15753#LoginSettings) | Login settings of the instance. This parameter is used to set the login password and key for the instance, or to keep the original login settings for the image. By default, a random password is generated and notified to the user via the internal message. |
| SecurityGroupIds.N | No | Array of String | The security group to which the instance belongs. This parameter can be obtained by calling the sgld field in the returned value of [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808). If this parameter is not specified, the security group is not bound by default. |
| EnhancedService | No | [EnhancedService](/document/api/213/15753#EnhancedService) | Enhanced service. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, the Cloud Monitoring and Cloud Security are enabled by default. |
| ClientToken | No | String | A string to ensure the idempotency of the request, which is generated by the client. Each request shall have a unique string with a maximum of 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be ensured. For more information, please see How to Ensure Idempotency. |
| HostName | No | String | Server name of CVM.<li>Period (.) and hyphen (-) cannot be used as the first and the last character of HostName, and multiple consecutive hyphens (-) or periods (.) are not allowed.</li><li>Windows instance: The string length of the server name of CVM is [2, 15], and letters (case insensitive), digits, and hyphens (-) are allowed in the name, but period (.) is not supported and the name cannot be all digits.</li><li>Other types (such as Linux) of instances: The string length is [2, 30], supporting multiple periods (.). The piece between two periods is composed of letters (case insensitive), digits, and hyphens (-). |
| ActionTimer | No | [ActionTimer](/document/api/213/15753#ActionTimer) | Timed task. This parameter is used to specify the timed task for instance. Only the timed termination is supported. |
| TagSpecification.N | No | Array of [TagSpecification](/document/api/213/15753#TagSpecification) | Tag description list. This parameter is used to bind a tag to a resource instance. A tag can only be bound to CVM instance. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| InstanceIdSet | Array of String | This parameter is returned when an instance is created via this API, representing one or more instance `IDs`. The return of the instance `ID` list does not mean that the instance is created successfully. You can find out whether the instance is created by querying the status of the instance `ID` in the returned InstancesSet via API [DescribeInstancesStatus](https://cloud.tencent.com/document/api/213/15738). If the status of the instance changes from "pending" to "running", the instance is created successfully. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| AccountQualificationRestrictions | The request account failed to pass the eligibility verification. |
| InstancesQuotaLimitExceeded | Indicates that the number of created instances exceeds the remaining quota allowed for the account. |
| InvalidClientToken.TooLong | The specified ClientToken exceeds the maximum length of 64 bytes. |
| InvalidHostId.NotFound | The specified HostId does not exist, or does not belong to the request account. |
| InvalidInstanceName.TooLong | The specified InstanceName exceeds the maximum length of 60 bytes.|
| InvalidInstanceType.Malformed | Invalid format for the specified parameter InstanceType. |
| InvalidParameter.InvalidIpFormat | Incorrect format for the specified VPC IP. |
| InvalidParameterCombination | Incorrect parameter combination. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.Range | Invalid parameter value. Invalid parameter value range. |
| InvalidPassword | Invalid password. The specified password does not conform to the rule of password complexity. For example, the password length does not meet the requirement. |
| InvalidPeriod | Invalid period. The periods supported are: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] (in month). |
| InvalidPermission | This operation is not supported for the account. |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |
| VpcAddrNotInSubNet | VPC IP is not in the subnet. |
| VpcIpIsUsed | VPC IP is already occupied. |

## 5. Example

## Example 1 Purchase with Simple Parameters

### Scenario description

Input only the required parameter Zone and Image ID, and use default values for other parameters, as shown below: Zone: Guangzhou Zone 2; image ID: img-pmqg1cw7.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=RunInstances
&Placement.Zone=ap-guangzhou-2
&ImageId=img-pmqg1cw7
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "InstanceIdSet": [
      "ins-1vogaxgk"
    ],
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```

## Example 2 Purchase Instances on a Prepaid Basis

### Scenario description

Zone: Guangzhou Zone 2; billing method: prepaid by month and automatic renewal upon expiry; image ID: img-pmqg1cw7; model: standard 1C1G (S1.SMALL1), 50 GB local common system disk with 100 GB local common data disk, basic network; public network billing method: traffic postpaid by hour; upper limit of public network bandwidth: 10 Mbps, assigned with public IP; instance name: QCLOUD-TEST; login password: Qcloud@TestApi123++; installed with Cloud Monitoring and Cloud Security; one instance is purchased.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=RunInstances
&Placement.Zone=ap-guangzhou-2
&InstanceChargeType=PREPAID
&InstanceChargePrepaid.Period=1
&InstanceChargePrepaid.RenewFlag=NOTIFY_AND_AUTO_RENEW
&ImageId=img-pmqg1cw7
&InstanceType=S1.SMALL1
&SystemDisk.DiskType=LOCAL_BASIC
&SystemDisk.DiskSize=50
&DataDisks.0.DiskType=LOCAL_BASIC
&DataDisks.0.DiskSize=100
&InternetAccessible.InternetChargeType=TRAFFIC_POSTPAID_BY_HOUR
&InternetAccessible.InternetMaxBandwidthOut=10
&InternetAccessible.PublicIpAssigned=TRUE
&InstanceName=QCLOUD-TEST
&LoginSettings.Password=Qcloud@TestApi123++
&EnhancedService.SecurityService.Enabled=TRUE
&EnhancedService.MonitorService.Enabled=TRUE
&InstanceCount=1
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "InstanceIdSet": [
      "ins-bfw5zq3y"
    ],
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```

## Example 3 Purchase Instances on an Hourly and Postpaid Basis

### Scenario description

Zone: Guangzhou Zone 2; billing method: postpaid by hour; image ID: img-pmqg1cw7; model: standard 1C1G (S2.SMALL1), 50 GB local common system disk with 100 GB local common data disk, basic network; public network billing method: traffic postpaid by hour; upper limit of public network bandwidth: 10 MB, assigned with public IP; instance name: QCLOUD-TEST; login password: Qcloud@TestApi123++; installed with Cloud Monitoring and Cloud Security; one instance is purchased.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=RunInstances
&Placement.Zone=ap-guangzhou-2
&InstanceChargeType=POSTPAID_BY_HOUR
&ImageId=img-pmqg1cw7
&InstanceType=S2.SMALL1
&SystemDisk.DiskType=LOCAL_BASIC
&SystemDisk.DiskSize=50
&DataDisks.0.DiskType=LOCAL_BASIC
&DataDisks.0.DiskSize=100
&InternetAccessible.InternetChargeType=TRAFFIC_POSTPAID_BY_HOUR
&InternetAccessible.InternetMaxBandwidthOut=10
&InternetAccessible.PublicIpAssigned=TRUE
&InstanceName=QCLOUD-TEST
&LoginSettings.Password=Qcloud@TestApi123++
&EnhancedService.SecurityService.Enabled=TRUE
&EnhancedService.MonitorService.Enabled=TRUE
&InstanceCount=1
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "InstanceIdSet": [
      "ins-32kcaqoa"
    ],
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```

## Example 4 Purchase Sub-machine Instance of Exclusive Parent Host

### Scenario description

Zone: Guangzhou Zone 2; An instance is created on CDH host-q88gab4i; billing method: paid by exclusive parent host; image ID: img-pmqg1cw7; sub-machine configuration: 1C1G, 50 GB local common system disk with 100 GB local common data disk, basic network; public network billing method: traffic postpaid by hour; upper limit of public network bandwidth: 10 Mbps, assigned with public IP; instance name: QCLOUD-TEST; login password: Qcloud@TestApi123++; installed with Cloud Monitoring and Cloud Security; one instance is purchased.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=RunInstances
&Placement.Zone=ap-guangzhou-2
&Placement.HostIds.0=host-q88gab4i
&InstanceChargeType=CDHPAID
&ImageId=img-pmqg1cw7
&InstanceType=CDH_1C1G
&SystemDisk.DiskType=LOCAL_BASIC
&SystemDisk.DiskSize=50
&DataDisks.0.DiskType=LOCAL_BASIC
&DataDisks.0.DiskSize=100
&InternetAccessible.InternetChargeType=TRAFFIC_POSTPAID_BY_HOUR
&InternetAccessible.InternetMaxBandwidthOut=10
&InternetAccessible.PublicIpAssigned=TRUE
&InstanceName=QCLOUD-TEST
&LoginSettings.Password=Qcloud@TestApi123++
&EnhancedService.SecurityService.Enabled=TRUE
&EnhancedService.MonitorService.Enabled=TRUE
&InstanceCount=1
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "InstanceIdSet": [
      "ins-0s7wsh5x"
    ],
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```

## Example 5 Generate Sub-machine with Specified VPC IP

### Scenario description

Zone: Hong Kong Zone 1; billing method: postpaid by hour; image ID: img-dkwyg6sr; model: standard 1C1G (S1.SMALL1); 50 GB local common system disk; VPC; VPC ID: 1urkhbj4; subnet ID: dcs9x3gz; specified VPC ID: 10.0.0.18, 10.0.0.19; two instances are purchased.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=RunInstances
&InstanceType=S1.SMALL2
&SystemDisk.DiskType=CLOUD_BASIC
&SystemDisk.DiskSize=50
&Placement.Zone=ap-hongkong-1
&ImageId=img-dkwyg6sr
&VirtualPrivateCloud.SubnetId=subnet-dcs9x3gz
&VirtualPrivateCloud.VpcId=vpc-1urkhbj4
&VirtualPrivateCloud.PrivateIpAddresses.0=10.0.0.18
&VirtualPrivateCloud.PrivateIpAddresses.1=10.0.0.19
&InstanceCount=2
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "InstanceIdSet": [
      "ins-0s7wsh5x",
      "ins-03lw8hok"
    ],
    "RequestId": "3c14def19-cfes-470e-b241-90787u6jf5uj"
  }
}
```


