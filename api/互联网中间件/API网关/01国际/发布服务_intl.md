## API Description

This API (ReleaseService) is used to publish services.
This API cannot be called until it is published to an environment after it is created by an API gateway. This API is used to publish a service to an environment, such as release environment.


## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| --------------- | ---- | ------- | ---------------------------------------- |
| serviceId | Yes | String | The unique ID of the service to be published. |
| environmentName | Yes | Boolean | The name of the environment to be published. Three environments are supported: test, prepub and release. |
| releaseDesc | Yes | String | Publishing description. |

## Output Parameters
| Parameter Name | Type | Description |
| ----------- | --------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| releaseTime | Timestamp | Publishing time of the service. You can roll back at this time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |
| releaseDesc | String | The remarks filled in when publishing. |

## Example	 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=ReleaseService
&serviceId=service=XX
&environmentName=Online
&releaseDesc=Publishing description
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success", 
	"releaseTime":"2017-08-07T00:00:00Z"     
    "releaseDesc":1234,
}
```





