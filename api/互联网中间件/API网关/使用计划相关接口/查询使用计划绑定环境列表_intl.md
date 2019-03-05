## API Description
This API (DescribeUsagePlanEnvironments) is used to query the list of environments bound to a usage plan.
After binding a usage plan to any environment, you can query the environments of all services bound with the usage plan.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ----------- | ---- | ------ | ------------------------------- |
| usagePlanId | Yes | String | The unique ID of the usage plan to be queried. |
| limit | No | Int | Number of results to be returned. For a usage plan bound to environments of multiple services, the number of returned results is 20 by default. |
| offset | No | Int | A query that returns multiple results starts from the offset. |
| bindType | No | String | Binding type. Value range: API and SERVICE. Default is SERVICE. |

## Output Parameters

| Parameter Name | Type | Description |
| --------------- | ------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| totalCount | Int | Number of the environments of the services to which a usage plan is bound. |
| environmentList | List of Array | Status of the environments of the services bound to a usage plan. |

"environmentList" indicates whether the service is bound to environments. "environmentList" is an array of "environment", which is composed as follows:

| Parameter Name | Type | Description |
| --------------- | ------ | --------- |
| serviceId | String | The unique ID of the bound service. |
| serviceName | String | Name of the bound service.
| environmentName | String | The name of the bound environment.
| apiId | String | The unique API ID. This parameter is returned if the input parameter bindType=API. |
| inUseRequestNum | Int | Number of used requests. |
| maxRequestNum | Int | Total request quota. -1: Disable. |


## Example 

```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeUsagePlanEnvironments
&usagePlanId=usagePlan-XX
```

The returned results are as below:

```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
	"totalCount":2,
	"environmentList":[
		{
			"seviceId":"sevice-XX",
			"serviceName":"xxx",
			"environmentName":"Test",
			"inUseRequestNum": 0,
			"maxRequestNum": -1
			
		},
		{
			"seviceId":"sevice-XXXX",
			"serviceName":"xxx",
			"environmentName":"release",
			"inUseRequestNum": 10,
			"maxRequestNum": 100
		}	
	],
}
```





