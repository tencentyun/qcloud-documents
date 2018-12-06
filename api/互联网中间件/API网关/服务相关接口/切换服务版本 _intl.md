## API Description

This API (UpdateService) is used to update from the running version to a specific version in the publishing environment. After a user creates a service and publishes it to an environment via an API gateway, several versions of the service will be generated during development. Then you can call this API to update between versions.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ----------------- | ---- | ------- | ---------------------------------------- |
| serviceId | Yes | String | The unique ID of the service to be updated. |
| environmentName | Yes | Boolean | The name of the environment to be rolled back. Three environments are supported: Test, Pre and release |
| versionName | Yes | String | Updated version number. |
| updateDesc | No | String | Update description. |

## Output Parameters
| Parameter Name | Type | Description |
| ---------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| updateDesc | String | Update description. |

## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=UpdateService
&serviceId=service-XX
&environmentalName=release
&versionName=xxxxx
&updateDesc=updateDesc
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",    
	"updateDesc":"updateDesc"
}
```





