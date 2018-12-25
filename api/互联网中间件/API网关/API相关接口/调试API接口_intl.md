
## API Description

This API (RunApi) is used to debug an API. You can call this API to debug an API after configuring it, without having to wait until the API is formally published.


## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ------------- | ---- | ------ | ---------------------------------------- |
| serviceId | Yes | String | Unique ID of the service of the API. |
| apiId | Yes | String | Unique ID of the API. |
| requestHeader | No | String | Request header for calling the API from frontend, which is encoded by json_dump. |
| requestQuery | No | String | Request query for calling the API from frontend, which is encoded by json_dump. |
| requestPath | No | String | Path to the API from frontend, which is encoded by json_dump. |
| requestMethod | No | String | Request method for calling the API from frontend. Only HEAD, GET, POST, PUT, PATCH and DELETE are supported. |
| requestBody | No | String | Request header for calling the API from frontend. |
| requestBodyDict | No | Dict | Request header for calling the API from frontend. This parameter is passed in array format if Body parameter is configured for this API. |
| contentType | No | String | Content type of the debugging request. Only application/json and application/x-www-form-urlencoded are supported. If this parameter is left empty, default is application/x-www-form-urlencoded. |

## Output Parameters
| Parameter Name | Type | Description |
| ------------ | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| returnHeader | String | Response header returned for the API. |
| returnBody | String | Response body returned for the API. |
| returnCode | Int | Response code returned for the API. |
| delay | Int | Response delay for the API (in ms). |


## Example 

Modify an API of which the backend service type is HTTP:
The request example is as below:
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=RunApi
&serviceId=service-XX
&apiId=api-XX
&requestHeader={"headerKey1":"headerValue1","headerKey2":"headerValue2"}
&requestQuery={"queryKey1":"queryValue1","queryKey2":"queryValue2"}
&requestPath={"pathKey1":"pathValue1","pathKey2":"pathValue2"}
&requestMethod=GET
&requestBody=abalabala
&contentType=application/json
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
	"returnHeader":"abcd",
	"returnBody":"efgh",
	"returnCode":200,
	"delay":300,
}
```

