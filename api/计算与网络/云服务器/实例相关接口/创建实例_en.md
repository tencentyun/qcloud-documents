## 1. API Description

This API (RunInstances) is used to create one or more instances with specified configuration.

Domain name for API request: cvm.api.qcloud.com


* Once created, the instance is started up automatically and the [status](/document/api/213/9452#instance_state) becomes **Running**.
* For prepaid instances, the purchase amount is deducted from your account directly. For pay-per-hours instance, the hourly rate of the instance will be pre-frozen. Make sure your account balance is sufficient before calling this API.
* The amount of instances you can purchase via this API is subject to the limit as stated in the [Restrictions on CVM Instance Purchase](https://cloud.tencent.com/document/product/213/2664), and share the quota with the instances created on the Console.
* With the asynchronous API, an instance `ID` list will be returned when the creation request is issued successfully, but the instance is not created immediately. During this period, the status of the instance is "Creating". You can call API [DescribeInstancesStatus](https://cloud.tencent.com/document/api/213/9389) to query the status of the instance to check whether it is created. If the status changes from "Creating" to "Running", the instance is created successfully.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceChargeType | String | No | Instance [billing type](https://cloud.tencent.com/document/product/213/2180). <br><li>PREPAID: prepaid (by year/month) <br><li>POSTPAID_BY_HOUR: postpaid by hour <br>Default: POSTPAID_BY_HOUR. |
| InstanceChargePrepaid | [InstanceChargePrepaid object](https://cloud.tencent.com/document/api/213/9451#instancechargeprepaid) | No | Prepaid mode, parameter configuration of prepaid by year/month. This parameter can specify the usage period, whether to set automatic renewal and other attributes of the instance purchased on a prepaid basis. This parameter is mandatory if the billing method for the specified instance is prepaid. |
| Placement | [Placement object](https://cloud.tencent.com/document/api/213/9451#placement) | Yes | Location of the instance. This parameter is used to specify the availability zone and project to which the instance belongs, etc. |
| InstanceType | String | No | Instance model. Different instance models specify different resource specifications. Specific values can be found in the latest Specifications by calling the API [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/9391) or in [Instance Type](/document/product/213/11518). If this parameter is not specified, the default model is S1.SMALL1. |
| ImageId | String | Yes | Valid [image](/document/product/213/4940) ID, such as `img-xxx`. There are four types of images: <br/><li>Public Images</li><li>Custom Images</li><li>Shared Images</li><li>Marketplace Images</li><br/>You can obtain the available image IDs by the following ways:<br/><li> For `public images`, `custom images` and `shared images`, log in to [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the image IDs; for `marketplace images`, query the image IDs through [Cloud Marketplace](https://market.cloud.tencent.com/list).</li><li>This value can be obtained from the `ImageId` field in the returned values of API [DescribeImages](/document/api/213/9418).</li>|
| SystemDisk | [SystemDisk object](https://cloud.tencent.com/document/api/213/9451#systemdisk) | No | Configuration information of the system disk in the instance. If this parameter is not specified, the default value is assigned to it. |
| DataDisks.N | [array of DataDisk objects](https://cloud.tencent.com/document/api/213/9451#datadisk) | No | Configuration information of the data disk in the instance. If this parameter is not specified, no data disk will be purchased by default. Currently you can specify only one data disk when purchasing it. |
| VirtualPrivateCloud | [VirtualPrivateCloud object](https://cloud.tencent.com/document/api/213/9451#virtualprivatecloud) | No | Configuration information of VPC. This parameter is used to specify the ID of VPC and subnet, etc. If this parameter is not specified, the basic network is used by default. If a VPC IP is specified in this parameter, parameter InstanceCount can only be 1. |
| InternetAccessible | [InternetAccessible object](https://cloud.tencent.com/document/api/213/9451#internetaccessible) | No | Configuration information of Public network bandwidth. If this parameter is not specified, the default public network bandwidth is 0 Mbps. |
| InstanceCount | Integer | No | Number of instances to be purchased. Value range: [1, 100]. Default: 1. The number of instances to be purchased cannot exceed the remaining quota allowed for the user. For information on quota restrictions, please see [Restrictions on CVM Instance Purchase](https://cloud.tencent.com/document/product/213/2664). |
| InstanceName | String | No | Displayed name of the instance. If this parameter is not specified, "Not named" is displayed by default. The maximum length cannot exceed 60 bytes. |
| LoginSettings | [LoginSettings object](https://cloud.tencent.com/document/api/213/9451#loginsettings) | No | Login settings of the instance. This parameter is used to set the login password and key for the instance, or to keep the original login settings for the image. By default, a random password is generated and notified to the user via the internal message. |
| SecurityGroupIds.N | Array of Strings | No | The security group to which the instance belongs. This parameter can be obtained by calling the sgId field in the returned value of [DescribeSecurityGroups](https://cloud.tencent.com/document/api/213/1232). If this parameter is not specified, the security group is not bound by default. If the security group is not bound, all the ports will be exposed to the public network and private network, and all the businesses (such as port 80, 443) of the instance will be accessible. Such option may cause security risks, so It is recommended to select a new security group as needed. You can specify only one security group when purchasing the instance. |
| EnhancedService | [EnhancedService object](https://cloud.tencent.com/document/api/213/9451#enhancedservice) | No | To enhance the service. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, the Cloud Monitoring and Cloud Security are enabled by default. |
| ClientToken | String | No | A string to ensure the idempotency of the request, which is generated by the client. Each request shall have a unique string with a maximum of 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be ensured. <br>For more information, please see How to Ensure Idempotency. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| InstanceIdSet | array of Strings | This parameter is returned when an instance is created via this API, representing one or more instance `IDs`. The return of the instance `ID` list does not mean that the instance is created successfully. You can find out whether the instance is created by querying the status of the instance `ID` in the returned InstancesSet via API [DescribeInstancesStatus](https://cloud.tencent.com/document/api/213/9389). If the status of the instance changes from "creating" to "running", the instance is created successfully. |
| RequestId | String | Unique request ID. A unique "RequestId" is returned for each request. In case of a failed call to the API, "RequestId" needs to be provided when you contact the developer at backend. |


### Example of the Parameter Returned When the API Performs Normally
<pre>
{
    "Response": {
        "InstanceIdSet": [
            "xxx1",
            "xxx2"
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
</pre>

### Example of the Parameter Returned When the API Performs Abnormally

<pre>
{
  "Response": {
    "Error": {
      "Code": "AuthFailure",
      "Message": "qcloud was not able to validate the provided access credentials"
    },
    "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
  }
}
</pre>

## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.Range | Invalid parameter value range. |
| InvalidParameterCombination | Incorrect parameter combination. |
| MissingParameter | Missing parameter. The required parameter in the request is missing. |
| InvalidPermission | Account permission restriction, cannot perform this action. |
| AccountQualificationRestrictions | The request account failed to pass the eligibility verification. |
| InvalidZone.MismatchRegion | The specified availability zone 'ID' is invalid or does not match the availability zone under the specified region. |
| InvalidHostId.NotFound | The specified HostId does not exist, or does not belong to the request account. |
| InvalidPeriod | The value of the specified purchased usage period does not fall within the reasonable value range. |
| InvalidInstanceType.Malformed | [Invalid format for the specified parameter InstanceType](https://cloud.tencent.com/document/api/213/9451#instance) |
| InstancesQuotaLimitExceeded | Indicates that the number of created instances exceeds the remaining quota allowed for the account. |
| InvalidInstanceName.TooLong | [The specified InstanceName exceeds the maximum length of 60 bytes.](https://cloud.tencent.com/document/api/213/9451#instance) |
| InvalidPassword | Indicates that the complexity of the specified password does not meet the requirements. |
| InvalidClientToken.TooLong | The specified ClientToken exceeds the maximum length of 64 bytes. |
| VpcAddrNotInSubNet | VPC IP is not in the subnet |
| VpcIpIsUsed | VPC IP is already occupied |


## 5. Examples


### Example 1

> **Purchasing with simple parameters:**<br>
> Input only the required parameter Zone and Image ID, and use default values for other parameters, as shown below: Zone: Guangzhou Zone 2; image ID: img-pmqg1cw7.

### Request Parameters
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=RunInstances
  &Version=2017-03-12
  &Placement.Zone=ap-guangzhou-2
  &ImageId=img-pmqg1cw7
  &<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Response Parameters
<pre>
{
    "Response": {
        "InstanceIdSet": [
            "ins-1vogaxgk"
        ],
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
</pre>


### Example 2

> **Purchasing an prepaid instance:**<br>
> Zone: Guangzhou Zone 2; billing method: prepaid by month and automatic renewal upon expiry; image ID: img-pmqg1cw7; model: standard 1C1G (S1.SMALL1), 50 GB local common system disk with 100 GB local common data disk, basic network; public network billing method: traffic postpaid by hour; upper limit of public network bandwidth: 10 Mbps, assigned with public IP; instance name: QCLOUD-TEST; login password: Qcloud@TestApi123++; installed with Cloud Monitoring and Cloud Security; one instance is purchased.

### Request Parameters
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=RunInstances
  &Version=2017-03-12
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
  &<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Response Parameters
<pre>
{
    "Response": {
        "InstanceIdSet": [
            "ins-bfw5zq3y"
        ],
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
</pre>


### Example 3

> **Purchasing an postpaid instance on an hourly basis:**<br>
> Zone: Guangzhou Zone 2; billing method: postpaid by hour; image ID: img-pmqg1cw7; model: standard 1C1G (S1.SMALL1), 50 GB local common system disk with 100 GB local common data disk, basic network; public network billing method: traffic postpaid by hour; upper limit of public network bandwidth: 10 Mbps, assigned with public IP; instance name: QCLOUD-TEST; login password: Qcloud@TestApi123++; installed with Cloud Monitoring and Cloud Security; one instance is purchased.

### Request Parameters
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=RunInstances
  &Version=2017-03-12
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
  &<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Response Parameters
<pre>
{
    "Response": {
        "InstanceIdSet": [
            "ins-32kcaqoa"
        ],
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
</pre>

