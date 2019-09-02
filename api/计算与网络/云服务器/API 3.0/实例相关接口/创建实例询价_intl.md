## 1. API Description

This API (InquiryPriceRunInstances) is used to inquire the price for instance creation. With this API, you can only inquire the price according to the instance configuration within the range of purchase limits. For more information, please see [Create Instance](https://cloud.tencent.com/document/api/213/15730).

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: InquiryPriceRunInstances |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceChargeType | No | String | Instance [billing type](https://cloud.tencent.com/document/product/213/2180).<li>PREPAID: prepaid (by year/month)</li><li>POSTPAID_BY_HOUR: postpaid by hour</li>Default value: POSTPAID_BY_HOUR. |
| InstanceChargePrepaid | No | [InstanceChargePrepaid](/document/api/213/15753#InstanceChargePrepaid) | Prepaid mode, which is the relevant parameter setting for prepaid mode. This parameter can specify the purchased usage period, whether to set automatic renewal and other attributes of the instance purchased on a prepaid basis. This parameter is mandatory if the billing method for the specified instance is prepaid. |
| Placement | Yes | [Placement](/document/api/213/15753#Placement) | Location of the instance. This parameter is used to specify the availability zone and project to which the instance belongs |
| InstanceType | No | String | Instance model. Different instance models specify different resource specifications. Specific values can be found in the latest specifications by calling the API [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749) or in [CVM Instance Configuration](https://cloud.tencent.com/document/product/213/2177). If this parameter is not specified, the default model is S1.SMALL1. |
| ImageId | Yes | String | Valid [image](https://cloud.tencent.com/document/product/213/4940) ID, such as `img-xxx`. There are four types of images:<li>Public Images</li><li>Custom Images</li><li>Shared Images</li><li>Marketplace Images</li>You can obtain the available image IDs by the following ways:<li>For `public images`, `custom images` and `shared images`, log in to [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the image IDs; for `marketplace images`, query the image IDs through [Cloud Marketplace](https://market.cloud.tencent.com/list).</li><li>This value can be obtained from the `ImageId` field in the returned values of API [DescribeImages](https://cloud.tencent.com/document/api/213/15715).</li> |
| SystemDisk | No | [SystemDisk](/document/api/213/15753#SystemDisk) | Configuration information of instance's system disk. If the parameter is not specified, the default value is assigned to it. |
| DataDisks.N | No | Array of [DataDisk](/document/api/213/15753#DataDisk) | Configuration information of the instance data disk. If the parameter is not specified, no data disk will be purchased by default. Currently, you can specify only one data disk when purchasing it. |
| VirtualPrivateCloud | No | [VirtualPrivateCloud](/document/api/213/15753#VirtualPrivateCloud) | Configuration information of VPC. This parameter is used to specify the VPC ID, subnet ID, etc. If this parameter is not specified, the basic network is used by default. If a VPC IP is specified in this parameter, the parameter InstanceCount can only be 1. |
| InternetAccessible | No | [InternetAccessible](/document/api/213/15753#InternetAccessible) | Configuration information of public network bandwidth. If this parameter is not specified, the default public network bandwidth is 0 Mbps. |
| InstanceCount | No | Integer | Number of instances to be purchased. Value range: [1, 100]. Default value: 1. The specified number of instances to be purchased cannot exceed the remaining quota allowed for the user, For more information about quota restrictions, please see [Restrictions on CVM Instance Purchase](https://cloud.tencent.com/document/product/213/2664). |
| InstanceName | No | String | The display name of the instance. If this name of instance is not specified, the name of instance is displayed by default. |
| LoginSettings | No | [LoginSettings](/document/api/213/15753#LoginSettings) | Login settings of the instance. This parameter is used to set the login password and key for the instance, or to keep the original login settings for the image. By default, a random password is generated and notified to the user via the internal message. |
| SecurityGroupIds.N | No | Array of String | The security group to which the instance belongs. This parameter can be obtained by calling the sgld field in the returned value of [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808). If this parameter is not specified, the security group is not bound by default. For more information, please see How to Ensure Idempotency. |
| HostName | No | String | Server name of CVM.<li>Period (.) and hyphen (-) cannot be used as the first and the last character of HostName, and multiple consecutive hyphens (-) or periods (.) are not allowed.</li><li>Windows instance: The string length of the server name of CVM is [2, 15], and letters (case insensitive), digits, and hyphens (-) are allowed in the name, but period (.) is not supported and the name cannot be all digits.</li><li>Other types (such as Linux) of instances: The string length is [2, 30], supporting multiple periods (.). The piece between two periods is composed of letters (case insensitive), digits, and hyphens (-).</li> |
| TagSpecification.N | No | Array of [TagSpecification](/document/api/213/15753#TagSpecification) | Tag description list. This parameter is used to bind a tag to a resource instance. Currently, a tag can only be bound to CVM instance. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| Price | [Price](/document/api/213/15753#Price) | This parameter indicates the price of the corresponding instance configuration. |
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
| InvalidParameterCombination | Incorrect parameter combination. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.Range | Invalid parameter value. Invalid parameter value range. |
| InvalidPassword | Invalid password. The specified password does not conform to the rule of password complexity. For example, the password length does not meet the requirement. |
| InvalidPeriod | Invalid period. The periods supported are: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] (in month). |
| InvalidPermission | This operation is not supported for the account. |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Price Inquiry for the Purchase with Simple Parameters

### Scenario description

Input only the required parameter Zone and Image ID, and use default values for other parameters, as shown below: Zone: Guangzhou Zone 2; image ID: img-pmqg1cw7.


### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=InquiryPriceRunInstances
&Placement.Zone=ap-guangzhou-2
&ImageId=img-pmqg1cw8
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "Price": {
      "InstancePrice": {
        "ChargeUnit": "HOUR",
        "UnitPrice": "0.34"
      }
    },
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```

## Example 2 Price Inquiry for the Purchase of Instances on a Prepaid Basis

### Scenario description

Zone: Guangzhou Zone 2; billing method: prepaid by month and automatic renewal upon expiry; image ID: img-pmqg1cw7; model: standard 1C1G (S1.SMALL1), 50 GB local common system disk with 100 GB local common data disk, basic network; public network billing method: traffic postpaid by hour; upper limit of public network bandwidth: 10 Mbps, assigned with public IP; instance name: QCLOUD-TEST; login password: Qcloud@TestApi123++; installed with Cloud Monitoring and Cloud Security; one instance is purchased.


### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=InquiryPriceRunInstances
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
    "Price": {
      "BandwidthPrice": {
        "ChargeUnit": "GB",
        "UnitPrice": "0.80"
      },
      "InstancePrice": {
        "DiscountPrice": "45.00",
        "OriginalPrice": "45.00"
      }
    },
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```

## Example 3 Price Inquiry for Purchase of Instances on an Hourly and Postpaid Basis

### Scenario description

Zone: Guangzhou Zone 2; billing method: postpaid by hour; image ID: img-pmqg1cw7; model: standard 1C1G (S1.SMALL1), 50 GB local common system disk with 100 GB local common data disk, basic network; public network billing method: traffic postpaid by hour; upper limit of public network bandwidth: 10 Mbps, assigned with public IP; instance name: QCLOUD-TEST; login password: Qcloud@TestApi123++; installed with Cloud Monitoring and Cloud Security; one instance is purchased.


### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=InquiryPriceRunInstances
&Placement.Zone=ap-guangzhou-2
&InstanceChargeType=POSTPAID_BY_HOUR
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
    "Price": {
      "BandwidthPrice": {
        "ChargeUnit": "GB",
        "UnitPrice": "0.80"
      },
      "InstancePrice": {
        "ChargeUnit": "HOUR",
        "UnitPrice": "0.34"
      }
    },
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```


