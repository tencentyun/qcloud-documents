
## API Description

This API (ModifyApi) is used to modify a configured API. The API configuration takes effect after the service of the API is released to its environment.  

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ---------------------------------------- | ---- | ------- | ---------------------------------------- |
| serviceId | Yes | String | Unique ID of the service of the API. |
| apiId | Yes | String | Unique ID of the API. |
| apiName | No | String | The custom name of the API. |
| apiDesc | No | String | The custom description of the API. |
| authRequired | No | String | Indicates whether signature verification is required. TRUE: required; FALSE: not required. |
| enableCORS | No | String | Indicates whether to enable cross-origin access. TRUE: enable; FALSE: not enable. |
| apiDesc | No | String | The custom description of the API. |
| requestConfig.path | No | String | Path to the API from frontend, such as /path. |
| requestConfig.method | No | String | Request method for calling the API from frontend, such as GET. |
| requestConfig.protocol | No | String | Request type for calling the API from frontend, such as HTTP or HTTPS, or HTTP and HTTPS. |
| requestParameters.n.name | No | String | Name of the parameter in the request for calling the API from frontend. |
| requestParameters.n.position | No | String | Position of the parameter in the request for calling the API from frontend, such as head. "head", "query" and "path" are supported. |
| requestParameters.n.type | No | String | Type of the parameter in the request for calling the API from frontend, such as String and int. |
| requestParameters.n.defaultValue | No | String | Default value of the parameter in the request for calling the API from frontend. |
| requestParameters.n.required | No | Boolean | Indicates whether the parameter in the request for calling the API from frontend is required. TRUE: required; FALSE: optional. |
| requestParameters.n.desc | No | String | Description of the parameter in the request for calling the API from frontend. |
| serviceType | No | Boolean | Type of the backend service corresponding to the API. Supported values: HTTP, MOCK and SCF. |
| serviceTimeout | No | Int | Request timeout for calling the backend service from the API (in sec). |
| serviceConfig.url | No | String | URL of the backend service corresponding to the API. This parameter is required if serviceType is HTTP. |
| serviceConfig.path | No | String | Path to the backend service from the API, such as /path. This parameter is required if serviceType is HTTP. The path to the API from frontend and the path to the backend service from the API can be different. |
| serviceConfig.method | No | String | Request method for calling the backend service from the API, such as GET. This parameter is required if serviceType is HTTP. The request method for calling the API from frontend and the request method for calling the backend service from the API can be different. |
| serviceParameters.n.name | No | String | Name of the parameter in the request for calling the backend service from the API. This parameter is required only when serviceType is HTTP. The name of the parameter in the request for calling the API from frontend and the name of the parameter in the request for calling the backend service from the API can be different. |
| serviceParameters.n.position | No | String | Position of the parameter in the request for calling the backend service from the API, such as head. This parameter is required only when serviceType is HTTP. The position of the parameter in the request for calling the API from frontend and the position of the parameter in the request for calling the backend service from the API can be different. |
| serviceParameters.n.relevantRequestParameterName | No | String | Name of the parameter in the request for calling the API from frontend corresponding to the parameter in the request for calling the backend service from the API. This parameter is required only when serviceType is HTTP. |
| serviceParameters.n.relevantRequestParameterPosition | No | String | Position of the parameter in the request for calling the API from frontend corresponding to the parameter in the request for calling the backend service from the API, such as head. This parameter is required only when serviceType is HTTP. |
| serviceParameters.n.desc | No | String | Description of the parameter in the request for calling the backend service from the API. This parameter is required only when serviceType is HTTP. |
| constantParameters.n.name | No | String | Name of the constant parameter. This parameter is required only when serviceType is HTTP. |
| constantParameters.n.desc | No | String | Description of the constant parameter. This parameter is required only when serviceType is HTTP. |
| constantParameters.n.position | No | String | Position of the constant parameter. This parameter is required only when serviceType is HTTP. |
| constantParameters.n.defaultValue | No | String | Default value of the constant parameter. This parameter is required only when serviceType is HTTP. |
| serviceMockReturnMessage | No | String | Returned message when the type of the backend service corresponding to the API is Mock. This parameter is required if serviceType is Mock. |
| serviceScfFunctionName | No | String | Name of the SCF function of the backend service corresponding to the API. This parameter is required if serviceType is SCF. |
| serviceScfFunctionName | No | String | Name of the SCF function of the backend service corresponding to the API. This parameter is required if serviceType is SCF. |
| responseType | No | String | Returned response type for custom response configuration. HTML, JSON, TEST, BINARY and XML are supported. |
| responseSuccessExample | No | String | Response example for a successful custom response configuration. |
| responseFailExample | No | String | Response example for a failed custom response configuration. |
| responseErrorCodes.n.code | No | String | Error code for custom response configuration. |
| responseErrorCodes.n.msg | No | String | Error message for custom response configuration. |
| responseErrorCodes.n.desc | No | String | Error description for custom response configuration. |
| isDeleteResponseErrorCodes | No | String | Indicates whether to delete error codes for custom response configuration. If this parameter is FALSE or left empty, the error codes will not be deleted; if this parameter is TRUE, all custom response configuration error codes for this API will be deleted. |

## Output Parameters
| Parameter Name | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |


## Example 

Modify an API of which the backend service type is HTTP:
The request example is as below:
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=ModifyApi
&serviceId=service-XX
&apiId=api-XX
&apiDesc=myTestApi
&requestConfig.path=/path
&requestConfig.method=GET
&requestConfig.protocol=Http
&requestParameters.0.name=age
&requestParameters.0.location=head
&requestParameters.0.type=Int
&requestParameters.0.defaultValue=18
&requestParameters.0.required=REQUIRED
&requestParameters.0.description=Age
&serviceType=Http
&serviceTimeout=60
&serviceConfig.url=cloud.tencent.com
&serviceConfig.path=/path
&serviceConfig.method=GET
&serviceParameters.0.name=age
&serviceParameters.0.location=head
&serviceParameters.0.relevantRequestParameterName=age
&serviceParameters.0.relevantRequestParameterIn=head
&serviceParameters.0.defaultValue=18
&serviceParameters.0.description=Age
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
}
```

Modify an API of which the backend service type is Mock:
The request example is as below:
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=ModifyApi
&serviceId=service-XX
&apiId=api-XX
&apiDescription=myTestApi
&requestConfig.path=/path
&requestConfig.method=GET
&requestConfig.protocol=Http
&requestParameters.0.name=age
&requestParameters.0.location=head
&requestParameters.0.type=Int
&requestParameters.0.defaultValue=18
&requestParameters.0.required=REQUIRED
&requestParameters.0.description=Age
&serviceType=MOCK
&serviceTimeout=60
&serviceMockReturnMessage=Returned message from MOCK
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
}
```

Modify an API of which the backend service type is SCF:
The request example is as below:
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=ModifyApi
&serviceId=service-XX
&apiId=api-XX
&apiDescription=myTestApi
&requestConfig.path=/path
&requestConfig.method=GET
&requestConfig.protocol=Http
&requestParameters.0.name=age
&requestParameters.0.location=head
&requestParameters.0.type=Int
&requestParameters.0.defaultValue=18
&requestParameters.0.required=REQUIRED
&requestParameters.0.description=Age
&serviceType=SCF
&serviceTimeout=60
&serviceScfFunctionName=myScfFunction
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
}
```



```



```

