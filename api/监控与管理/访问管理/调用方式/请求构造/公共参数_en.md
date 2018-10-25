A complete Tencent Cloud API request requires two types of request parameters: common request parameter and API request parameter. This document will describe 6 common request parameters used in Tencent Cloud API requests. For more information on API request parameters, please see API Request Parameters.
Common request parameters are required in every API. When developers use Tencent Cloud APIs to send requests, they should make sure that the requests carry these common request parameters, or the requests will fail. In order to differentiate from API request parameters, the initial letters of common request parameters are all capital letters.

Common request parameters are as follows:

| Parameter Name | Required | Type | Description |
| ------------ | ------------ | ------------ | ------------ |
| Action | Yes | String | The name of the API for the desired operation. For example, if you want to call the API Get Temporary Access Credentials for User with Federated Identity, the Action parameter is GetFederationToken. |
| Region | No | String | Region parameter, which is used to identify the region to which the STS service you want to use belongs. Notes: 1. only ap-guangzhou and ap-shanghai are available to all users, and STS services in other regions are still in internal trial; 2. default is ap-guangzhou. |
| Timestamp | Yes | UInt | The current UNIX timestamp that records the time at which the API request was initiated. |
| Nonce | Yes | UInt | A random positive integer that is used in conjunction with Timestamp to prevent replay attacks. |
| SecretId | Yes | String | SecretId for identifying identity that is applied for on [Cloud API Key](https://console.cloud.tencent.com/capi) which is used for identification. A SecretId corresponds to a unique SecretKey, which is used to generate the request Signature. For more information, please see [Signature Method](https://cloud.tencent.com/document/api/377/4214). |
| Signature | Yes | String | Request signature, which is used to verify the validity of the request. The signature must be calculated according to input parameters. For more information, please see [Signature Method](https://cloud.tencent.com/document/api/377/4214). |
| SignatureMethod | Yes | String | Signature method. The supported methods for now are HmacSHA256 and HmacSHA1. HmacSHA256 method is used only when the parameter is specified as HmacSHA256, otherwise HmacSHA1 is used to verify signatures. For more information, please see [Signature Method](https://cloud.tencent.com/document/api/377/4214). |


**Example**

The format of common request parameters in API request links for Tencent Cloud products are shown below. Take Tencent Cloud CVM as example, suppose a user needs to query the list of CVM instances in Guangzhou region, the request link should be:
```
https://cvm.api.qcloud.com/v2/index.php?
Action=DescribeInstances
&SecretId=xxxxxxx
&Region=ap-guangzhou
&Timestamp=1465055529
&Nonce=59485
&Signature=mysignature
&SignatureMethod=HmacSHA256
&<API request parameters>
```

