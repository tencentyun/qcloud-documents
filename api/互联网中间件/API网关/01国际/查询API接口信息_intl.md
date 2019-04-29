
## API Description

This API (DescribeApi) is used to query the details of the APIs deployed at an API gateway. ​

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name      | Required | Type     | Description            |
| --------- | ---- | ------ | ------------- |
| serviceId | Yes | String | Unique ID of the service of the API. |
| apiId | Yes | String | Unique ID of the API. |

## Output Parameters
| Parameter Name | Type | Description |
| ------------------------ | -------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| serviceId | String | Unique ID of the service of the API. |
| serviceName | String | Name of the service of the API. |
| serviceDesc | String | Description of the service of the API. |
| apiId | String | Unique ID of the API. |
| apiDesc | String | API description. |
| apiName | String | API name. |
| createdTime | Timestamp | Creation time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |
| modifiedTime | Timestamp | Last modification time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |
| requestConfig | Array | Fields configured in the request for calling the API from frontend. |
| requestParameters | List of Arrays | An array of parameters in the request for calling the API from frontend. |
| serviceType | Boolean | Backend service type of the API. Supported values: HTTP, MOCK and SCF |
| serviceTimeout | Int | Request timeout for calling the backend service from the API (in sec). |
| serviceConfig | Array | Fields configured in the request for calling the backend service from the API. This parameter is returned only if serviceType is HTTP. |
| serviceParameters | List of Arrays | An array of parameters in the request for calling the backend service from the API. This parameter is returned only if serviceType is HTTP. |
| constantParameters | List of Arrays | An array of constant parameters in the request for calling the backend service from the API. This parameter is returned only if serviceType is HTTP. |
| serviceMockReturnMessage | String | Returned message when the type of the backend service corresponding to the API is Mock. This parameter is returned only if serviceType is Mock. |
| serviceScfFunctionName | String | Name of the SCF function of the backend service corresponding to the API. This parameter is returned only if serviceType is SCF. |
| authRequired | String | Indicates whether signature verification is required. TRUE: required; FALSE: not required. |
| enableCORS | String | Indicates whether to enable cross-origin access. TRUE: required; FALSE: not required. |
| responseType | String | Returned response type for custom response configuration. HTML, JSON, TEST, BINARY, and XML are supported. |
| responseSuccessExample | String | Response example for a successful custom response configuration. |
| responseFailExample | String | Response example for a failed custom response configuration. |
| responseErrorCodes | List of Arrays | Error codes for custom response configuration. |

"requestConfig" in the request from frontend is composed as follows:

| Parameter Name | Type | Description |
| ------ | ------ | ---------------- |
| path | String | Path to the API from frontend, such as /path. |
| method | String | Request method for calling the API from frontend, such as GET. |

"requestParameters" in the request from frontend is an array of "requestParameter" which is composed as follows:

| Parameter Name | Type | Description |
| ------------ | ------- | ---------------------------------------- |
| name | String | Name of the parameter in the request for calling the API from frontend. |
| in | String | Position of the parameter in the request for calling the API from frontend, such as head. |
| type | String | Type of the parameter in the request for calling the API from frontend, such as String. |
| defaultValue | String | Default value of the parameter in the request for calling the API from frontend. |
| required | Boolean | Indicates whether the parameter in the request for calling the API from frontend is required. REQUIRED: required; OPTIONAL: optional. |
| desc | String | Description of the parameter in the request for calling the API from frontend. |

If the backend service type of an API is HTTP, "serviceConfig" is composed as follows:

| Parameter Name | Type | Description |
| ------ | ------ | ------------------ |
| url | String | URL of the backend service corresponding to the API. |
| path | String | Path to the backend service from the API, such as /path. |
| method | String | Request method for calling the backend service from the API, such as GET. |

"serviceParameters" in the request for calling the backend service is an array of "serviceParameter" which is composed as follows:

| Parameter Name | Type | Description |
| ---------------------------- | ------ | -------------------------- |
| name | String | Name of the parameter in the request for calling the backend service from the API. |
| position | String | Position of the parameter in the request for calling the backend service from the API, such as head. |
| relevantRequestParameterName | String | Name of the parameter in the request for calling the API from frontend corresponding to the parameter in the request for calling the backend service from the API. |
| relevantRequestParameterIn | String | Position of the parameter in the request for calling the API from frontend corresponding to the parameter in the request for calling the backend service from the API, such as head. |
| desc | String | Description of the parameter in the request for calling the backend service from the API. |

"constantParameters" is an array of "constantParameter", which is composed as follows:

| Parameter Name | Type | Description |
| ------------ | ------ | -------- |
| name | String | Constant parameter name. |
| desc | String | Constant parameter description. |
| position | String | Constant parameter position. |
| defaultValue | String | Default value of the constant parameter. |


## Example 

Query the details of an API of which the backend service type is HTTP:

The request example is as below:
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeApi
&serviceId=service-XX
&apiId=api-XX

```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success", 
    "serviceId":"service-XX",
    "serviceName":"test",
    "serviceDesc":"testDesc",
    "apiId":api-XX,
	"apiName":"apiXXXX",
	"apiType":"NORMAL",
    "apiDesc":"myHTTPTestApi",
	"createdTime":"2017-08-07T00:00:00Z",
	"modifiedTime":"2017-08-07T00:00:00Z",
    "requestConfig":{
		"path":"/path",
		"method":"GET",
	},
    "requestParameters":[
		{
			"name":"age",
			"in":"HEADER",
			"type":"Int",
			"defaultValue":18,
			"required:True,
			"desc:"Age"
		}
	],
    "serviceType":HTTP,
    "serviceTimeout":60,
    "serviceConfig":{
		"url":"cloud.tencent.com",
		"path":"/path",
		"method":"GET"
	},
    "serviceParameters":[
		{
			"name":"age",
			"in":"HEADER",
			"relevantRequestParameterName":"age",
			"relevantRequestParameterIn":"HEADER",
			"defaultValue":18,
			"desc":"Age"
		}
	],
}
```

Query the details of an API of which the backend service type is MOCK:

The request example is as below:
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeApi
&serviceId=service-XX
&apiId=api-XXX

```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success", 
    "serviceId":"service-XX",
    "serviceName":"test",
    "serviceDesc":"testDescription",
    "apiId":api-XXX,
	"apiName":"apiXXXX",
	"apiType":"NORMAL",
    "apiDesc":"myMockTestApi"
	"createdTime":"2017-08-07T00:00:00Z",
	"modifiedTime":"2017-08-07T00:00:00Z",
    "requestConfig":{
		"path":"/path",
		"method":"GET",
	},
    "requestParameters":[
		{
			"name":"age",
			"in":"HEADER",
			"type":"Int",
			"defaultValue":18,
			"required:"REQUIRED",
			"desc:"Age"
		}
	],
    "serviceType":MOCK,
    "serviceTimeout":60,
    "serviceMockReturnMessage":"Returned message from MOCK",
}
```

Query the details of an API of which the backend service type is SCF:

The request example is as below:
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeApi
&serviceId=service-XX
&apiId=api-XXXX

```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success", 
    "serviceId":"service-XX",
    "serviceName":"test",
    "serviceDesc":"testDescription",
    "apiId":api-XXXX,
	"apiName":"apiXXXX",
	"apiType":"NORMAL",
    "apiDesc":"mySCFTestApi",
	"createdTime":"2017-08-07T00:00:00Z",
	"modifiedTime":"2017-08-07T00:00:00Z",
    "requestConfig":{
		"path":"/path",
		"method":"GET",
	},
    "requestParameters":[
		{
			"name":"age",
			"in":"HEADER",
			"type":"Int",
			"defaultValue":18,
			"required:"REQUIRED",
			"desc:"Age"
		}
	],
    "serviceType":SCF,
    "serviceTimeout":60,
    "serviceScfFunctionName":"myScfFunction",
}
```

