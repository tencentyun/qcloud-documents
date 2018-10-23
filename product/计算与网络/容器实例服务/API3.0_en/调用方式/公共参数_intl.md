Common parameters are used for user identification and API authentication. Unless necessary, these parameters will not be discussed in each API document. A request must contain these parameters to be initiated successfully.

| Parameter Name | Type | Required | Description |
|:---------|:---------|:-----|:---- |
| Action | String | Yes | The name of the API for the desired operation. For example, if you want to call the CVM API "Query Instance List", the Action parameter is DescribeInstances. |
| Region | String | Yes | Region parameter, which is used to identify the region to which the data you want to work with belongs. |
| Timestamp | Integer | Yes | The current UNIX timestamp, which is used to record the time when the API request was initiated. for example, 1529223702. If the time difference between the timestamp and the current time is too large, a signature expiration error may occur. |
| Nonce | Integer | Yes | A random positive integer that is used in conjunction with Timestamp to prevent replay attacks. |
| SecretId | String | Yes | SecretId for identifying identity that is applied for on <a href="https://console.cloud.tencent.com/capi">Cloud API Key</a>. A SecretId corresponds to a unique SecretKey that is used to generate the request Signature. |
| Signature | String | Yes | Request signature, which is used to verify the validity of the request. It is generated based on input parameters. For more information on how to compute the signature, see the API authentication documentation. |
| Version | String | Yes | API version. such as 2017-03-12 |
| SignatureMethod | String | No | Signature method. Supported methods include HmacSHA256 and HmacSHA1. The HmacSHA256 method is used to verify signatures only when the parameter is specified as HmacSHA256. Otherwise, HmacSHA1 is used. |
| Token | String | No | The token used for the temporary certificate, which must be used together with a temporary key. You can obtain the temporary key and token by calling the CAM API. No token is required for a long-term key. |


If, for example, you want to query the list of Tencent Cloud CVM instances in the Guangzhou region, the request link should look like this:

<pre>
https://cvm.tencentcloudapi.com/?Action=DescribeInstances
&SecretId=xxxxxxx
&Region=ap-guangzhou
&Timestamp=1402992826
&Nonce=345122
&Signature=xxxxxxxx
&Version=2017-03-12
</pre>


## Region List

The Region fields of all APIs for this product can be set to the following values. Any API that does not support the regions in the table will be described separately in the relevant API document.


| Region | Value |
|------|------|
| North China (Beijing) | ap-beijing |
| Southwest (Chengdu) | ap-chengdu |
| South China (Guangzhou) | ap-guangzhou |
| East China (Shanghai) | ap-shanghai |

