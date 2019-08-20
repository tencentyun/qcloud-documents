## 1. API Description
This API (InquiryCdbRenewPrice) is used to query the renewal price of Cloud Database instances (including master instances and read-only instances) with an annual or monthly plan. Renewal is not applicable to instances with pay by usage mode.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is InquiryCdbRenewPrice.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| period | Yes | Int | Renewal period (Unit: month). The minimum and maximum values are 1 and 36 respectively. You can use API [Query Supported Specifications](/doc/api/253/1333) to acquire the validity period of an instance that can be renewed. The returned field "timeSpan" represents the available period |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| price | Int | Price for renewing an instance (unit: RMB 0.01) |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |


## 4. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=InquiryCdbRenewPrice
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-dwkpvwgf
&period=12
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "price":114540
}
```


