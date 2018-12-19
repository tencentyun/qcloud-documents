## 1. API Description
This API (DescribeUserGwVendor) is used to acquire information on supported customer gateway vendors.
Domain for API request: <font style='color:red'>vpc.api.qcloud.com </font>



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is DescribeUserGwVendor.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| None | None | None | None |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/215/4781' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| data | Array | Returned information |
| data.platform | String | Platform | 
| data.software | String | Software version | 
| data.vendorname | String | Vendor | 

## 4. Error Codes
The API does not have a business error code. For common error codes, see <a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="VPC Error Codes for details">VPC Error Codes for details</a>

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeUserGwVendor
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[
        {
            "platform":"ios",
            "software":"V15.4",
            "vendorname":"cisco"
        },
        {
            "platform":"comware",
            "software":"V1.0",
            "vendorname":"h3c"
        }
    ]
}
```


