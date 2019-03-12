A complete Tencent Cloud API request requires two types of request parameters: common request parameters and API request parameters. This document describes 6 common request parameters used in Tencent Cloud API requests. For more information about API request parameters, see [API Request Parameters](https://cloud.tencent.com/document/product/582/13381).
Common request parameters are required in every API. When developers use Tencent Cloud APIs to send requests, they should make sure that the requests carry these common request parameters. Otherwise, the requests will fail. The first letter of each common request parameter is in uppercase so that the parameter can be differentiated from API request parameters.

Common request parameters are as follows:
>**Note:**
>This document illustrates APIs specific to Tencent Cloud CVMs. For APIs specific to other Tencent Cloud products, see the relevant documents.

| Parameter Name | Description | Type | Required |
|---------|---------|---------|---------|
| Action | The name of the API for the desired operation. For example, when a Tencent Cloud CVM user calls the API [Query Instance List](https://cloud.tencent.com/document/api/213/9388), the Action parameter is DescribeInstances. | String | Yes |
| Region | Region parameter, which is used to identify the region to which the instance you want to work with belongs. For more information, see [Regions and Availability Zones](/document/product/213/6091), or use the API [Query Region List](/document/api/213/9456).<br>**Notes:** 1. Unless otherwise specified in the API document, this parameter is required generally.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Some of the regions are under internal trial and only available to certain users. | String | No |
| Timestamp | The current UNIX timestamp, which is used to record the time when the API request was initiated. | UInt | Yes |
| Nonce | A random positive integer that is used in conjunction with Timestamp to prevent replay attacks. | UInt | Yes |
| SecretId | SecretId for identifying identity that is applied for on [Cloud API Key](https://console.cloud.tencent.com/capi). A SecretId corresponds to a unique SecretKey, which is used to generate the request Signature. For more information, see [Signature Method](https://cloud.tencent.com/document/product/215/1693). | String | Yes |
| Signature | Request signature, which is used to verify the validity of the request. It is generated based on input parameters. For more information, see [Signature Method](https://cloud.tencent.com/document/product/215/1693). | String | Yes |
| SignatureMethod | Signature method. Supported methods include HmacSHA256 and HmacSHA1. The HmacSHA256 method is used to verify signatures only when the parameter is specified as HmacSHA256. Otherwise, HmacSHA1 is used. For more information, see [Signature Method](https://cloud.tencent.com/document/product/215/1693). | String | No |
| Token | The token used for the temporary certificate, which must be used together with a temporary key. No token is required for a long-term key. | String | No |

### Use Case
The following example shows how common request parameters look like in an API request link for a Tencent Cloud product. If, for example, you want to query the list of Tencent Cloud CVM instances in the Guangzhou region, the request link should look like this:

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



