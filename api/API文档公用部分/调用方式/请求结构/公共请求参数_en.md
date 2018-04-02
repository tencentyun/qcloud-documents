A complete Tencent Cloud API request requires two types of request parameters: common request parameter and API request parameter. This document will describe 6 common request parameters used in Tencent Cloud API requests. For more information about API request parameters, please see [API Request Parameters](https://cloud.tencent.com/document/product/582/13381).
Common request parameters are required in every API. When developers use Tencent Cloud APIs to send requests, they should make sure that the requests carry these common request parameters, otherwise the requests will fail. In order to differentiate from API request parameters, the initial letters of common request parameters are all capital letters.

Common request parameters are as follows:
>**Note:**
>The API examples in this document use Tencent Cloud CVM as example. For other Tencent Cloud products, refer to their instructions accordingly.

| Parameter | Description | Type | Required |
|---------|---------|---------|---------|
| Action | API name of a specific operation. For example, when a Tencent Cloud CVM user calls the [Query Instance List](/doc/api/229/831) API, the Action parameter is DescribeInstances. | String | Yes |
| Region | Region parameter which is used to indicate the region of the instance to be operated in. For more information, please see the [Regions and Availability Zones](/doc/product/213/6091) list, or use the [Query Region List](/doc/api/213/9456) API. <br>**Note:** 1. This parameter is required in normal conditions unless stated otherwise in the API description.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Some of the regions are under internal trial and are only available to certain users. | String | No |
| Timestamp | The current UNIX timestamp that records the time at which the API request was initiated. | UInt | Yes |
| Nonce | A random positive integer that is used in conjunction with Timestamp to prevent replay attacks. | UInt | Yes |
| SecretId | SecretId applied from [Cloud API Key](https://console.cloud.tencent.com/capi) which is used for identification. Each SecretId corresponds to a unique SecretKey, while SecretKey is used to generate request Signature. For more information, please see [Signature Method](/doc/api/372/4214). | String | Yes |
| Signature | Request signature which is used to verify the validity of the current request. The signature must be calculated according to input parameters. For more information, please see [Signature Method](/doc/api/372/4214). | String | Yes |
| SignatureMethod | Signature method. Currently supported methods are HmacSHA256 and HmacSHA1. HmacSHA256 method is used only when the parameter is specified as HmacSHA256, otherwise HmacSHA1 is used to verify signatures. For more information, please see [Signature Method](/doc/api/372/4214). | String | No |
| Token | Token used for temporary certificate. The token must be used together with temporary key. A long-term key does not require a Token. | String | No |

### Example
The format of common request parameters in API request links for Tencent Cloud products are shown below. Take Tencent Cloud CVM as example, suppose a user needs to query the list of CVM instances in Guangzhou region, the request link should be:

<pre>
https://cvm.api.qcloud.com/v2/index.php?
Action=DescribeInstances
&SecretId=xxxxxxx
&Region=ap-guangzhou
&Timestamp=1465055529
&Nonce=59485
&Signature=mysignature
&SignatureMethod=HmacSHA256
&<<a href="https://cloud.tencent.com/document/api/377/4154">API request parameters</a>>
</pre>



