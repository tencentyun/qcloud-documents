## API Description

This API (ModifyUsagePlan) is used to modify the name, description and QPS of a usage plan.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ------------------- | ---- | ------ | ----------------- |
| usagePlanId | Yes | String | The unique ID of the usage plan. |
| usagePlanName | No | String | The modified custom name of the usage plan. |
| usagePlanName | No | String | The modified custom description of the usage plan. |
| maxRequestNumPreSec | No | Int | QPS limit. |
| maxRequestNum | No | Int | Total request quota. -1: Disable. |

## Output Parameters

| Parameter Name | Type | Description |
| ------------------- | --------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| usagePlanId | String | The unique ID of the usage plan. |
| usagePlanName | String | The modified custom name of the usage plan. |
| usagePlanName | String | The modified custom description of the usage plan. |
| maxRequestNumPreSec | Int | Modified QPS. |
| modifiedTime | Timestamp | Last modification time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |

## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=ModifyUsagePlan
&usagePlanId=usagePlan-XX
&usagePlanName=newusagePlanName
&usagePlanDesc=newUsagePlanDescription
&maxRequestNumPreSec=1000
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
	"usagePlanId":"usagePlan-XX",
	"usagePlanName":"newusagePlanName",
	"usagePlanDesc":"newUsagePlanDescription",
	"maxRequestNumPreSec":1000,
	"modifiedTime":"2017-08-07T00:00:00Z",
}
```





