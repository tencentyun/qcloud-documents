The common parameters are used to authenticate the user and API. If not necessary, these parameters are not described in individual API documents. However, they have to be carried by each request to initiate properly.

|Parameter name | Type | Required | Description|
|:---------|:---------| -----|:---- |
|Action | String | Yes | The name of the command API for the specific operation. For example, if you want to call the instance list query API of Cloud Virtual Machine, then the Action parameter is DescribeInstances. |
| Region | String | Yes | The Region parameter used to identify the region whose data you want to operate on. |
| Timestamp | Integer | Yes | The current UNIX timestamp which records when an API request is initiated. For example, 1529223702. If it is too different from the current time, it will cause a signature expiry error. |
| Nonce | Integer | Yes | A random positive integer used to prevent replay attacks along with Timestamp. |
| SecretId | String | Yes | The identifying SecretId obtained on the [Cloud API Key](https://console.cloud.tencent.com/capi) page. A SecretId corresponds to a unique SecretKey which is used to generate the request signature (Signature). |
| Signature | String | Yes | Request signature used to verify the validity of this request. This is generated based on the actual input parameters. For details on how to generate, see the API authentication document. |
| Version | String | Yes | The version of the API. For example, 2017-03-12 |
| SignatureMethod | String | No | Signature mode. Currently, HmacSHA256 and HmacSHA1 are supported. The HmacSHA256 algorithm is used to verify the signature only when this parameter is specified as HmacSHA256. In other cases, the signature is verified with HmacSHA1. |
| Token | String | No | The token used by the temporary certificate, which needs to be used in conjunction with the temporary key. The temporary key and token need to be obtained through the access management service call API. Long-term keys do not require a token. |


Assuming you want to query the list of Cloud Virtual Machine instances in the Guangzhou region, the form of the request link may be as follows:

<pre>
https://cvm.tencentcloudapi.com/?Action=DescribeInstances
&SecretId=xxxxxxx
&Region=ap-guangzhou
&Timestamp=1402992826
&Nonce=345122
&Signature=xxxxxxxx
&Version=2017-03-12
</pre>


## **Region List**

The possible values for the Region field in all APIs of this product are as shown below. If an API does not support any of the listed regions, the detail will be described separately in the API document.


| Region | Value |
|------|------|
|North China (Beijing)|ap-beijing|
|Southwest China (Chengdu)|ap-chengdu|
|South China (Guangzhou)|ap-guangzhou|
|South China (Guangzhou Open)|ap-guangzhou-open|
|Asia Pacific (Mumbai)|ap-mumbai|
|East China (Shanghai)|ap-shanghai|
