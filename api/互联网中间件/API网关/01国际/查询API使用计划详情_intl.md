## API Description

This API (DescribeApiUsagePlan) is used to query the usage plan information of the APIs in a service.
If authentication is required for the service to take effect, you need to bind usage plans to this service. This API is used to query all usage plans bound to a service and the APIs in the service.


## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ----------------- | ---- | ------ | ------------------- |
| serviceId | Yes | String | The unique ID of the service to be queried. |
| offset | No | Int | Offset. Default is 0. |
| limit | No | Int | Number of returned results. Default is 20. Maximum is 100. |
| searchEnvironment | No | String | Conducts exact search based on the environment name of a usage plan. |
| apiIds.n | No | List of String | Array of API unique IDs. The usage plan information of all APIs under current service is returned if this parameter is left empty. |

## Output Parameters
| Parameter Name | Type | Description |
| ------------- | -------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| totalCount | Int | Number of usage plans bound to the service. |
| usagePlanList | List of Arrays | List of usage plans bound to the service. |

"usagePlanList" is an array of "usagePlanAttribute" which is composed as follows:

| Parameter Name | Type | Description |
| ------------- | --------- | ----------- |
| usagePlanId | String | The unique ID of the usage plan. |
| usagePlanName | String | The name of the usage plan. |
| usagePlanDesc | String | The description of the usage plan. |
| environment | String | The service environment to which the usage plan is bound. |
| createdTime | Timestamp | Creation time of the usage plan. |
| modifiedTime | Timestamp | Last modification time of the usage plan. |
| inUseRequestNum | Int | Number of used requests. |
| maxRequestNum | Int | Total request quota. -1: Disable. |
| maxRequestNumPreSec | Int | QPS limit. -1: Disable. |
| apiId | String | Unique ID of the API. |
| path | String | Request path. |
| method | String | Request method. |
| apiName | String | API name. |
| serviceId | String | The unique ID of the service. |
| serviceName | String | Service name. |

## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeApiUsagePlan
&serviceId=service-XX
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
	"totalCount":2,
	"usagePlanList":[
		{
			"maxRequestNumPreSec": 2000,
			"usagePlanId": "usagePlan-0var1p8v",
			"modifiedTime": "2018-07-31 20:26:28",
			"usagePlanDesc": "test",
			"apiId": "api-2yuua008",
			"environment": "release",
			"serviceId": "service-XX",
			"apiName": "sjiofjsdioj",
			"createdTime": "2018-07-20 14:09:47",
			"path": "/fsodjfsd",
			"usagePlanName": "test",
			"method": "GET",
			"serviceName": "test"
		}
	]
}
```





