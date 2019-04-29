## 1. API Description
This API (ModifyUserGw) is used to modify customer gateway.
Domain for API request: <font style='color:red'>vpc.api.qcloud.com </font>



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is ModifyUserGw.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| userGwId | Yes | String | Customer gateway ID assigned by the system. For example: cgw-e098slul |
| userGwName | Yes | String | Customer gateway name. You can use any content as long as it does not exceed 60 characters.  |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |

## 4. Error Codes
 The following list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error code | Description |
|---------|---------|
| InvalidUserGwName | Invalid customer gateway name. It should be within  60 characters.  |
| InvalidUserGw.NotFound | Invalid customer gateway. Customer gateway resource does not exist. Please check the information you entered. You can query customer gateway by using the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e5%af%b9%e7%ab%af%e7%bd%91%e5%85%b3?viewType=preview" title="DescribeUserGw">DescribeUserGw</a> API.  |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=ModifyUserGw
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&userGwId=cgw-e098slul
&userGwName=9101
</pre>
Output
```
{
    "code":"0",
    "message":""
}
```


