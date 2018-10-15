## API Description

This API (CreateApiKey) is used to create a new pair of API keys.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ---------- | ---- | ------ | ---------- |
| secretName | No | String | User-defined key name. |

## Output Parameters

| Parameter Name | Type | Description |
| ----------- | --------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| secretName | String | User-defined key name. |
| secretId | String | ID of API key. |
| secretKey | String | API key. |
| createdTime | Timestamp | Creation time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |

## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=CreateApiKey
&secretName=myTest
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",   
	"secretName":"myTest",   
    "secretId":"AKIDXXXXWKipDlK",
	"secretKey":"adasfdasffa",
	"createdTime":"2017-08-07T00:00:00Z",
}
```





