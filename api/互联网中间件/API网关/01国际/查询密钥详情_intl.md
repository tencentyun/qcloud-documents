## API Description
This API (DescribeApiKey) is used to query the details of keys.
After you have created a key, you can query the details of an API key using this API which will display the key.


## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| -------- | ---- | ------ | -------- |
| secretId | Yes | String | ID of API key. |

## Output Parameters

| Parameter Name | Type | Description |
| ------------ | --------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| secretName | String | User-defined key name. |
| secretId | String | ID of API key. |
| secretKey | String | API key. |
| status | Int | Status of an API key. 1: In use; 0: Disabled |
| createdTime | Timestamp | Creation time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |
| modifiedTime | Timestamp | Last modification time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |



## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeApiKey
&secretId=AKIDXXXXWKipDlK
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
	"secretId":"AKIDXXXXWKipDlK",
	"secretKey":"asdkXXXXKOlhKn",
	"secretName":"mytest",
	"status":1,
	"createdTime":"2017-08-07T00:00:00Z",
	"modifiedTime":"2017-08-07T00:00:00Z",
}
```





