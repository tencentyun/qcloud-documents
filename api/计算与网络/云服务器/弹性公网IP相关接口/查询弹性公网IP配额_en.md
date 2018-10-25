## 1. API Description

This API (DescribeAddressQuota) is used to query the quota information of the [Elastic IP](/document/product/213/1941) (EIP) in your account in the current region. For more information about the EIP quota, please see [Overview of EIP Products](/document/product/213/5733).

Domain name for API request: eip.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |


## 3. Output Parameters

| Parameter| Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |
| QuotaSet | Array of [Quota](/document/api/213/9451#quota) objects| The information of EIP quota in an account |




## 4. Sample Codes

### Request Parameters
<pre>
  https://eip.api.qcloud.com/v2/index.php?Action=DescribeAddressQuota
  &Version=2017-03-12
  &<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Response Parameters
<pre>
{
    "Response": {
        {
            'QuotaSet': [
            {'QuotaId': 'TOTAL_EIP_QUOTA', 'QuotaCurrent': 0, 'QuotaLimit': 20},
            {'QuotaId': 'DAILY_EIP_APPLY', 'QuotaCurrent': 0, 'QuotaLimit': 40},
            {'QuotaId': 'DAILY_EIP_ASSIGN','QuotaCurrent': 0, 'QuotaLimit': 40},
             ]
        }
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>

