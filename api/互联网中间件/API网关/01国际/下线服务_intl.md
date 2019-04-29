## API Description

This API (UnReleaseService) is used to deactivate services.
After a user publishes a service to an environment, the API in the service can be called. If a user wants to deactivate the service from the publishing environment, this API (UnReleaseService) can be called. Deactivated service cannot be called.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| --------------- | ---- | ------- | ---------------------------------------- |
| serviceId | Yes | String | The unique ID of the service to be deactivated. |
| environmentName | Yes | Boolean | The name of the environment to be deactivated. Three environments are supported: test, prepub and release |
| unReleaseDesc | No | String | Deactivation description. |

## Output Parameters
| Parameter Name | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |

## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=UnReleaseService
&serviceId=service=XX
&environmentName=Online
&unReleaseDesc=Deactivation description
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",    
	"unReleaseDesc":"unReleaseDesc"
}
```





