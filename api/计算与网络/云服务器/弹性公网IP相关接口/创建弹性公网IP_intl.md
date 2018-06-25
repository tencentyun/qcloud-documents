## 1. API Description

This API (AllocateAddresses) is used to apply for one or more [Elastic IPs](https://intl.cloud.tencent.com/document/product/213/5733) (EIPs).

Domain name for API request: eip.api.qcloud.com

* EIP is a static IP address designed for dynamic cloud computing. With EIP, you can quickly remap the EIP to another instance, shielding off the instance failures.
* Your EIP is associated with a Tencent Cloud account, instead of an instance, until you choose to explicitly release it or your payment is more than seven days overdue.
* The platform imposes quotas on number of EIPs that a user can request for each region. Please see [Overview of EIP Products](/document/product/213/5733). The above quotas can be obtained via API [DescribeAddressQuota](/document/api/213/1378).


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| AddressCount | Integer| No | The number of EIPs that can be requested. Value range: [1, 5]. Default is 1. |


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |
| AddressSet | Array of Strings | List of unique IDs of the requested EIPs |

## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error code | Description |
|---------|---------|
| AddressQuotaLimitExceeded | Account quota is exceeded. Up to 20 EIPs can be created by each Tencent Cloud account in each region. |
| AddressQuotaLimitExceeded.DailyAllocate | The maximum number of requests is exceeded. The maximum number of requests can be made by each Tencent Cloud account in each region equals to two times the quota. |

## 5. Sample Codes

### Input

<pre>
https://eip.api.qcloud.com/v2/index.php?Action=AllocateAddresses
&Version=2017-03-12
&AddressCount=1
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Output
<pre>
{
    "Response": {
        "AddressSet": [
            "eip-m44ku5d2"
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>

