## 1. API Description

This API (DescribeInstanceInternetBandwidthConfigs) is used to query the instance bandwidth configuration.

Domain name for API request: cvm.api.qcloud.com

* You can only query the bandwidth configuration of `BANDWIDTH_PREPAID` billing method.
* All bandwidth configuration information (including historical bandwidth configuration information) of an instance is returned via the API.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version number, used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceId | String| Yes | ID of the instance you want to query. It can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](document/api/213/9388). |


## 3. Output Parameters

| Parameter| Type | Description |
|---------|---------|---------|
| RequestId | String | For each request, a unique request is returned. In case of API calling failures, you need to provided the `RequestId` to Tencent Cloud to locate your problem. |
 | InternetBandwidthConfigSet | Array of [InternetBandwidthConfig](/document/api/213/9451#internetbandwidthconfig) object | Bandwidth configuration information of the instance |


## 4. Error Codes

The following error codes are specific to this API. For other error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error code | Description |
|---------|---------|
| MissingParameter | A required parameter is missing in the request. |
| InvalidInstanceId.NotFound | Invalid instance `ID`. The specified instance `ID` does not exist. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InternalServerError | Tencent Cloud server error |


## 5. Example

Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstanceInternetBandwidthConfigs
&Version=2017-03-12
&InstanceId=ins-6lafsaz0
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

Output
<pre>
{
    "Response": {
        "InternetBandwidthConfigSet": [
            {
                "StartTime": "2017-03-12T16:00:00Z",
                "EndTime": "2017-04-12T16:00:00Z",
                "InternetAccessible": {
                    "InternetMaxBandwidthOut": 50,
                    "InternetChargeType": "BANDWIDTH_PREPAID"
                }
            }
        ],
        "RequestId": "314161cd-ee40-4c37-921e-b10c4ed5607c"
    }
}
</pre>

