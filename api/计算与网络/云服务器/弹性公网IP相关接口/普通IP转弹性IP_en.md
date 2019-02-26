## 1. API Description

This API (TransformAddress) is used to change an ordinary public IP into an [Elastic IP](/document/product/213/1941) (EIP).

Domain name for API request: eip.api.qcloud.com


* Tencent Cloud imposes quotas on the number of ordinary public IPs that a user can re-assign for each region per day after the EIP is unbound. Please see [Overview of EIP Products](/document/product/213/1941). The above quotas can be obtained via API [DescribeAddressQuota](/document/api/213/1378).


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter  Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version number, used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceId | String | Yes | ID of the instance to be operated which has an ordinary public IP, such as `ins-11112222`. You can obtain the instance ID by either of the following ways: query the instance ID via [Console](https://console.cloud.tencent.com/cvm); obtain the instance ID from the `InstanceId` field of the returned values of API [DescribeInstances](/document/api/213/9389). |


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error code | Description |
|---------|---------|
| AddressQuotaLimitExceeded | Account quota is exceeded. At most 20 EIPs can be created by each Tencent Cloud account in each region. |
| AddressQuotaLimitExceeded.DailyAllocate | The maximum number of requests is exceeded. The maximum number of requests can be made by each Tencent Cloud account in each region equals to two times the quota. |
| InvalidInstanceId.NotFound | The instance ID does not exist. |
| InvalidInstanceState | The ordinary public IP cannot be transformed to EIP for the instance in the current status. |
| InvalidInstance.NotSupported | The ordinary public IP cannot be transformed to EIP for the specified instance. |

## 5. Sample Codes

### Input

<pre>
https://eip.api.qcloud.com/v2/index.php?Action=TransformAddress
&Version=2017-03-12
&InstanceId=ins-3ea0qeu6
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Output

<pre>
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>

