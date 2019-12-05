
## API Description

This API (CreateApi) is used to create an API. You need to create a service before creating an API. Each API corresponds to a service.


## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ---------------------------------------- | ---- | ------- | ---------------------------------------- |
| serviceId | Yes | String | Unique ID of the service of the API. |
| apiName | No | String | The custom name of the API. |
| apiDesc | No | String | The custom description of the API. |
| apiType | No | String | API type. Only "NORMAL" is supported and other types will be available soon. |
| authRequired | No | String | Indicates whether signature verification is required. TRUE: required; FALSE: not required. Default is TRUE. You must pass in TRUE for APIs published in cloud marketplace. |
| enableCORS | No | String | Indicates whether to enable cross-origin access. TRUE: enable; FALSE: not enable. Default is FALSE. |
| requestConfig.path | Yes | String | Path to the API from frontend, such as /path. |
| requestConfig.method | Yes | String | Request method for calling the API from frontend, such as GET. |
| requestParameters.n.name | No | String | Name of the parameter in the request for calling the API from frontend. |
| requestParameters.n.position | No | String | Position of the parameter in the request for calling the API from frontend. Only PATH, QUERY and HEADER are supported. |
| requestParameters.n.type | No | String | Type of the parameter in the request for calling the API from frontend, such as String and int. |
| requestParameters.n.defaultValue | No | String | Default value of the parameter in the request for calling the API from frontend. |
| requestParameters.n.required | No | Boolean | Indicates whether the parameter in the request for calling the API from frontend is required. TRUE: required; FALSE: optional. |
| requestParameters.n.desc | No | String | Description of the parameter in the request for calling the API from frontend. |
| serviceType | Yes | Boolean | Type of the backend service corresponding to the API. Supported values: HTTP, MOCK and SCF. |
| serviceTimeout | Yes | Int | Request timeout for calling the backend service from the API (in sec). |
| serviceConfig.url | No | String | URL of the backend service corresponding to the API. This parameter is required if serviceType is HTTP. |
| serviceConfig.path | No | String | Path to the backend service from the API, such as /path. This parameter is required if serviceType is HTTP. The path to the API from frontend and the path to the backend service from the API can be different. The API gateway will map the paths. |
| serviceConfig.method | No | String | Request method for calling the backend service from the API, such as GET. This parameter is required if serviceType is HTTP. The request method for calling the API from frontend and the request method for calling the backend service from the API can be different. The API gateway will map the methods. |
| serviceParameters.n.name | No | String | Name of the parameter in the request for calling the backend service from the API. This parameter is required only when serviceType is HTTP. The name of the parameter in the request for calling the backend service from the API and the name of the parameter in the request for calling the API from frontend can be different. The API gateway will map the parameter names. The values of the parameters must be the same. |
| serviceParameters.n.position | No | String | Position of the parameter in the request for calling the backend service from the API, such as head. This parameter is required only when serviceType is HTTP. The position of the parameter in the request for calling the backend service from the API and the position of the parameter in the request for calling the API from frontend can be different. The API gateway will map the parameter positions. |
| serviceParameters.n.relevantRequestParameterName | No | String | Name of the parameter in the request for calling the API from frontend corresponding to the parameter in the request for calling the backend service from the API. This parameter is required only when serviceType is HTTP. |
| serviceParameters.n.relevantRequestParameterPosition | No | String | Position of the parameter in the request for calling the API from frontend corresponding to the parameter in the request for calling the backend service from the API. This parameter is required only when serviceType is HTTP. |
| serviceParameters.n.desc | No | String | Description of the parameter in the request for calling the backend service from the API. This parameter is required only when serviceType is HTTP. |
| constantParameters.n.name | No | String | Name of the constant parameter. This parameter is required only when serviceType is HTTP. Constant parameters are configured by API publishers at the backend and are invisible to frontend callers. |
| constantParameters.n.desc | No | String | Description of the constant parameter. This parameter is required only when serviceType is HTTP. |
| constantParameters.n.position | No | String | Position of the constant parameter. Only header and query are supported. This parameter is only required when serviceType is HTTP. | 
| constantParameters.n.defaultValue | No | String | Default value of the constant parameter. This parameter is required only when serviceType is HTTP. |
| serviceMockReturnMessage | No | String | Returned message when the type of the backend service corresponding to the API is Mock. This parameter is required if serviceType is Mock. |
| serviceScfFunctionName | No | String | Name of the SCF function of the backend service corresponding to the API. This parameter is required if serviceType is SCF. |
| responseType | No | String | Returned response type for custom response configuration. HTML, JSON, TEST, BINARY, and XML are supported. (This configuration is only used to generate an API documentation for callers' reference) |
| responseSuccessExample | No | String | Response example for a successful custom response configuration. (This configuration is only used to generate an API documentation for callers' reference) |
| responseFailExample | No | String | Response example for a failed custom response configuration. (This configuration is only used to generate an API documentation for callers' reference) |
| responseErrorCodes.n.code | No | Int | Error code for custom response configuration. (This configuration is only used to generate an API documentation for callers' reference) |
| responseErrorCodes.n.msg | No | String | Error message for custom response configuration. (This configuration is only used to generate an API documentation for callers' reference) |
| responseErrorCodes.n.desc | No | String | Error description for custom response configuration. (This configuration is only used to generate an API documentation for callers' reference) |


## Output Parameters
| Parameter Name | Type | Description |
| ----------- | --------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| apiId | String | Unique ID of the API. |
| path | String | Path. |
| method | String | Request method. |
| createdTime | Timestamp | Creation time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |


## Example 

Create an API of which the backend service is HTTP:
The request example is as below:

```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=CreateApi
&serviceId=service-XX
&apiDesc=myTestApi
&requestConfig.path=/path
&requestConfig.method=GET
&requestParameters.0.name=age
&requestParameters.0.position=HEADER
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
&serviceParameters.0.in=HEADER
&serviceParameters.0.relevantRequestParameterName=age
&serviceParameters.0.relevantRequestParameterIn=HEADER
&serviceParameters.0.defaultValue=18
&serviceParameters.0.desc=Age
&constantParameters.0.name=aa
&constantParameters.0.desc=aa
&constantParameters.0.position=HEADER
&constantParameters.0.defaultValue=aa
```

The returned results are as below:

```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
	"apiId":"api-XX",
	"path":"/path",
	"method":"GET",
	"createdTime":"2017-08-07T00:00:00Z",
}
```

Create an API of which the backend service is MOCK:
The request example is as below:

```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=CreateApi
&serviceId=service-XX
&apiDescription=myTestApi
&requestConfig.path=/path
&requestConfig.method=GET
&requestConfig.protocol=Http
&requestParameters.0.name=age
&requestParameters.0.in=HEADER
&requestParameters.0.type=Int
&requestParameters.0.defaultValue=18
&requestParameters.0.required=REQUIRED
&requestParameters.0.desc=Age
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
	"apiId":"api-XXX",
	"path":"/path",
	"method":"GET",
	"createdTime":"2017-08-07T00:00:00Z",
}
```

Create an API of which the backend service is SCF:
The request example is as below:

```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=CreateApi
&serviceId=service-XX
&apiDescription=myTestApi
&requestConfig.path=/path
&requestConfig.method=GET
&requestConfig.protocol=Http
&requestParameters.0.name=age
&requestParameters.0.in=HEADER
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
	"apiId":"api-XXXX",
	"path":"/path",
	"method":"GET",
	"createdTime":"2017-08-07T00:00:00Z",
}
```



