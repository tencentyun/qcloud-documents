## 1. API Description

This API (InquiryPriceResetInstance) is used to inquire the prices of reinstalled instances.

Domain name for API request: cvm.api.qcloud.com


* If you have specified `ImageId` parameter, the price inquiry is performed with the specified image. Otherwise, the image used by the current instance is used.
* Currently, using this API for price inquiry of reinstalled instances after switching between `Linux` and `Windows` operating systems is only supported for the instances with a [system disk type](/document/api/213/9452#block_device) of `CLOUD_BASIC`, `CLOUD_PREMIUM` and `CLOUD_SSD`.
* For the instances in overseas regions, this feature is not supported.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| instanceId | Yes | String | Instance ID. It can be obtained from `InstanceId` in the returned values of API [DescribeInstances](/document/api/213/9388).
| ImageId | String | No | Valid [image](/document/product/213/4940) ID, such as `img-xxx`. There are four types of images: <br/><li>Public Images</li><li>Custom Images</li><li>Shared Images</li><li>Marketplace Images</li><br/>You can obtain the available image IDs by the following ways:<br/><li> For `public images`, `custom images` and `shared images`, log in to [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the image IDs; for `marketplace images`, query the image IDs through Cloud Marketplace.</li><li>This value can be obtained from the `ImageId` field in the returned values of API [DescribeImages](/document/api/213/9418).</li>|
|SystemDisk|[SystemDisk](/document/api/213/9451#systemdisk) object|No| Configuration information of instance's system disk. For the instances with a cloud disk as the system disk, you can specify the system disk capacity after re-installation using this parameter to allow the capacity expansion of the system disk. If the parameter is not specified, the system disk capacity remains unchanged by default. Only expansion, instead of reduction, is supported for system disk capacity. You can only modify the system disk capacity for re-installation. The system disk type cannot be modified. |
| LoginSettings | [LoginSettings object](https://cloud.tencent.com/document/api/213/9451#loginsettings) | No | Login settings of the instance. This parameter is used to set the login password and key for the instance, or to keep the original login settings for the image. By default, a random password is generated and notified to the user via the internal message. |
| EnhancedService | [EnhancedService object](https://cloud.tencent.com/document/api/213/9451#enhancedservice) | No | To enhance the service. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, the Cloud Monitoring and Cloud Security are enabled by default. |


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
|Price|[Price](/document/api/213/9451#price) object| The price of the reinstalled instance.|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error Code | Description |
|---------|---------|
| MissingParameter |A required parameter is missing in the request. |
| InvalidInstanceId.NotFound | The specified instance ID does not exist. |
| InvalidInstanceId.Malformed | The specified instance ID is in an incorrect format. For example, `ins-1122` indicates an ID length error. |
| InvalidParameterValue | Parameter value is in an incorrect format or is not supported. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InternalServerError | Internal operation error. |


## 5. Examples
### Example 1

> **Price inquiry for a reinstalled prepaid instance:**<br>


### Request Parameters
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=InquiryPriceResetInstance
&Version=2017-03-12
&InstanceId=ins-2zvpghhc
&SystemDisk.DiskSize=50
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Response Parameters
<pre>
{
    "Response": {
        "Price": {
            "OriginalPrice": "9.46",
            "DiscountPrice": "9.46"
        },
        "RequestId": "c2d86443-dcb7-4279-a06d-5b3b700451d4"
    }
}
</pre>

### Example 2

> **Price inquiry for a reinstalled postpaid instance:**<br>


### Request Parameters
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=InquiryPriceResetInstance
&Version=2017-03-12
&InstanceId=ins-fd8spnmq
&SystemDisk.DiskSize=50
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Response Parameters
<pre>
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0.43,
                "ChargeUnit": "HOUR"
            }
        },
        "RequestId": "2cc6136b-12f4-4632-bba4-386d7b76abec"
    }
}
</pre>

