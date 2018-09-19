## 1. API Description

This API (InquiryVpnPrice) is used to query the VPN price.
Domain for API request: vpc.api.qcloud.com 
 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. 

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| period | Yes | Int | Length of purchase to be queried (in months). The maximum is 36 months.  |
| bandwidth | Yes | Int | Bandwidth, supported values: 5, 10, 20, 50, 100 (in Mb/s).  |

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed.  |
| message | String | Error message.  |
| price | Int | Price.  |

## 4. Error Codes
 The API does not have a business error code. For common error codes, see <a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="VPC Error Codes for details">VPC Error Codes for details</a>

## 5. Example
 
Input
<pre>
  https://domain/v2/index.php?Action=InquiryVpnPrice
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &period=1
  &bandwidth=5
</pre>

Output
```
{
    "code" : 0,
    "message" : "ok",
}
```


