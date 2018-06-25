Common parameters are used for user identification and API authentication. Unless necessary, these parameters are not discussed in each API document. A request must contain these parameters to be initiated successfully.

| Parameter Name | Required | Type | Description |
| :-------------- | :------- | :----------------------------------------------------------- | :------ |
| Action | Yes | The name of the API for the desired operation. For example, if you want to call the CVM API for querying the list of instances, the Action parameter is DescribeInstances. | String |
| Region | Yes | The region parameter, which identifies the region to which the data you want to operate on belongs. | String |
| Timestamp | Yes | The current UNIX timestamp, which records the time at which the API request was initiated. | Integer |
| Nonce | Yes | A random positive integer, which is used in conjunction with Timestamp to prevent replay attacks. | Integer |
| SecretId | Yes | SecretId for identification which is applied for on Cloud API Key page. A SecretId corresponds to a unique SecretKey, which is used to generate the request Signature. | String |
| Signature | Yes | Request signature, which is used to verify the validity of the request. It is generated based on input parameters. | String |
| SignatureMethod | No | Signature method. Supported methods include HmacSHA256 and HmacSHA1. HmacSHA256 method is used only when the parameter is specified as HmacSHA256, otherwise HmacSHA1 is used to verify signatures. | String |
| Token | No | The token used for a temporary certificate. The token must be used together with a temporary key. No token is required for a long-term key. | String |
| Version | Yes | API version, such as 2017-03-12 | String |


For example, if you want to query the CVM instance list for Guangzhou region, the request link may be as follows:

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstances

&SecretId=xxxxxxx

&Region=ap-guangzhou

&Timestamp=1402992826

&Nonce=345122

&Signature=xxxxxxxx

&Version=2017-03-12
```






