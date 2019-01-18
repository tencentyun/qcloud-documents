## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (InquiryPriceRunInstances) is used to inquire the prices of created instances. With this API, you can only inquire the prices of the instance configuration within the purchase limits. For more information, please see [Create Instances](https://cloud.tencent.com/document/api/213/15730).

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: InquiryPriceRunInstances |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Placement | Yes | [Placement](/document/api/213/##Placement) | Location of the instance. This parameter is used to specify the availability zone and project to which the instance belongs. |
| ImageId | Yes |  String | Specify a valid [Image](https://cloud.tencent.com/document/product/213/4940) ID, in the format of `img-xxx`. There are four types of images: <br/><li>Public image</li><li>Custom image</li><li>Shared image</li><li>Marketplace image</li><br/> You can obtain the available image IDs by either of the following ways: <br/><li>Query the image ID of a `public image`, `custom image` or `shared image` by logging in to the [Console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE); query the image ID of a `marketplace image` via [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li> Call the API [DescribeImages](https://cloud.tencent.com/document/api/213/15715) to obtain the `ImageId` field value in the returned result. </li> |
| InstanceChargeType | No | String | Instance [billing type](https://cloud.tencent.com/document/product/213/2180).<br><li> PREPAID: prepaid (by year/month) <br><li>POSTPAID_BY_HOUR: postpaid by hour <br>Default: POSTPAID_BY_HOUR. |
| InstanceChargePrepaid | No | [InstanceChargePrepaid](/document/api/213/##InstanceChargePrepaid) | Indicates the relevant parameter setting for the prepaid mode. This parameter can specify the usage period, whether to set automatic renewal and other attributes of the instance purchased on a prepaid basis. This parameter is required if the billing method for the specified instance is prepaid. |
| InstanceType | No | String | Instance model. Different instance models specify different resource specifications. Specific values can be found in the latest specifications by calling the API [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749) or in [CVM Instance Configuration](https://cloud.tencent.com/document/product/213/2177) If this parameter is not specified, the default model is S1.SMALL1. |
| SystemDisk | No | [SystemDisk](/document/api/213/##SystemDisk) | Configuration information of the system disk in the instance. If this parameter is not specified, the default value is assigned to it. |
| DataDisks.N | No | Array of [DataDisk](/document/api/213/##DataDisk) | Configuration information of the instance data disk. If this parameter is not specified, no data disk will be purchased by default. You can specify only one data disk when purchasing it. |
| VirtualPrivateCloud | No | [VirtualPrivateCloud](/document/api/213/##VirtualPrivateCloud) |Configuration information of VPC. This parameter is used to specify the ID of VPC and subnet, etc. If this parameter is not specified, the basic network is used by default. If a VPC IP is specified in this parameter, the parameter InstanceCount can only be 1. |
| InternetAccessible | No | [InternetAccessible](/document/api/213/##InternetAccessible) | Configuration information of public network bandwidth. If this parameter is not specified, the public network bandwidth is set to 0 Mbps by default. |
| InstanceCount | No | Integer | Number of instances to be purchased. Value range: [1, 100]. Default: 1. The number of instances to be purchased cannot exceed the remaining quota allowed for the user. For more information on quota restrictions, please see [Restrictions on CVM Instance Purchase](https://cloud.tencent.com/document/product/213/2664). |
| InstanceName | No | String | The display name of the instance.<br><li> If it is not specified, "Not named" is displayed by default.</li><li> If you purchase multiple instances and the pattern string `{R:x}` is specified, display names will be generated based on `[x, x+n-1]`, where `n` is the number of instances purchased. For example, when `server_{R:3}` is specified, the display name will be `server_3` if one instance is purchased, or `server_3` and `server_4` if two instances are purchased. You can specify multiple pattern strings `{R:x}`.</li><li> If you purchase multiple instances and the name pattern string is not specified, the suffix `1, 2...n` is appended to the display names, where `n` is the number of instances purchased. For example, when `server_` is specified, the display name will be `server_1` and `server_2` if two instances are purchased. |
| LoginSettings | No | [LoginSettings](/document/api/213/##LoginSettings) | Login settings of an instance. This parameter is used to set the instance login method, password and key, or to keep the original login settings of image. By default, a password is generated randomly and notified to the user via internal message. |
| SecurityGroupIds.N | No | Array of String | The security group to which an instance belongs. This parameter can be obtained from the sgId field in the returned values of [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808). If this parameter is not specified, the security group is not bound by default. |
| EnhancedService | No |  [EnhancedService](/document/api/213/##EnhancedService) | Enables enhanced services. This parameter is used to specify whether to enable Cloud Security, Cloud Monitor and other services. If this parameter is not specified, Cloud Monitor and Cloud Security services are enabled by default. |
| ClientToken | No |  String | A string to ensure the idempotency of the request, which is generated by the client. Each request shall have a unique string with a maximum of 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be ensured.<br> For more information, please see How to Ensure Idempotency. |
| HostName | No | String | Server name of CVM.<br><li> Period (.) and hyphen (-) cannot be used as the first and the last character of HostName, and multiple consecutive hyphens (-) or periods (.) are not allowed.<br><li> Windows instance: The name should be a combination of 2 to 15 characters comprised of letters (case insensitive), numbers, and hyphens (-). Period (.) is not supported, and the name cannot be a string of pure numbers.<br><li> Other types (such as Linux) of instances: The name should be a combination of 2 to 30 characters, supporting multiple periods (.). The piece between two periods is composed of letters (case insensitive), numbers, and hyphens (-). |
| TagSpecification.N | No | Array of [TagSpecification](/document/api/213/##TagSpecification) | Tag description list. This parameter is used to bind a tag to a resource instance. A tag can only be bound to CVM instances. |
| InstanceMarketOptions | No|  [InstanceMarketOptionsRequest](/document/api/213/##InstanceMarketOptionsRequest) | Market-related options for instances, such as parameters related to spot instances |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| Price | [Price](/document/api/213/##Price) | Indicates the price of the instance with specified configuration. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| AccountQualificationRestrictions | The request account failed to pass the eligibility verification. |
| InstancesQuotaLimitExceeded | The number of created instances exceeds the remaining quota allowed for the account. |
| InvalidClientToken.TooLong | The specified ClientToken exceeds the maximum length of 64 bytes. |
| InvalidHostId.NotFound | The specified HostId does not exist, or does not belong to the request account. |
| InvalidInstanceName.TooLong | The specified InstanceName exceeds the maximum length of 60 bytes. |
| InvalidInstanceType.Malformed | The format of the specified parameter InstanceType is invalid. |
| InvalidParameterCombination | Indicates that the parameter combination is incorrect. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.Range | Invalid parameter value. The parameter value range is invalid. |
| InvalidPassword | Invalid password. The specified password does not conform to the rule of password complexity. For example, the password length does not meet the requirement. |
| InvalidPeriod | Invalid period. Supported period values are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36 (in month). |
| InvalidPermission | The operation is not supported for the account. |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Price inquiry for the purchase with simple parameters

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=InquiryPriceRunInstances
&Placement.Zone=ap-guangzhou-2
&ImageId=img-pmqg1cw8
&<Common request parameters>
```

#### Output example

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

### Example 2 Price inquiry for the purchase of instances on a prepaid basis

#### Input example

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

#### Output example

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

### Example 3: Price inquiry for the purchase of instances on an hourly and postpaid basis

#### Input example

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

#### Output example

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


