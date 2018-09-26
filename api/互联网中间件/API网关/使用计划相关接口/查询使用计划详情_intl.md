## API Description

This API (DescribeUsagePlan) is used to query the details about a usage plan, such as its name, QPS, creation time and the environment it is bound to.


## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ----------- | ---- | ------ | ------------- |
| usagePlanId | Yes | String | The unique ID of the usage plan to be queried. |

## Output Parameters

| Parameter Name | Type | Description |
| ------------------------- | -------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| usagePlanId | String | The unique ID of the usage plan. |
| usagePlanName | String | The custom name of the usage plan. |
| usagePlanDesc | String | The description of the usage plan. |
| maxRequestNumPreSec | Int | QPS limit. |
| createdTime | Timestamp | Creation time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |
| modifiedTime | Timestamp | Last modification time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |
| bindSecretIdTotalCount | Int | Number of keys bound to the usage plan. |
| bindSecretIds | List of String | List of the keys bound to the usage plan. |
| bindEnvironmentTotalCount | Int | Number of the environments of the services to which the usage plan is bound. |
| bindEnvironments | List of Array | Status of the environments of the services bound to a usage plan. |

"bindEnvironments" indicates whether the service is bound to environments. "bindEnvironments" is an array of "bindEnvironment", which is composed as follows:

| Parameter Name | Type | Description |
| --------------- | ------ | --------- |
| serviceId | String | The unique ID of the bound service. |
| environmentName | String | The name of the bound environment.


## Example 

```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeUsagePlan
&usagePlanId=usagePlan-XX
```

The returned results are as below:

```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
	"usagePlanId":"usagePlan-XX",
	"usagePlanName":"test1",
	"usagePlanDesc":"test1",
	"maxRequestNumPreSec":500,
	"createdTime":"2017-08-07T00:00:00Z",
	"modifiedTime":"2017-08-07T00:00:00Z",
	"bindSecretIdTotalCount":2,
	"bindSecretIds":[
		"AKIDXXXXXwdeqDFaw",
		"AKIDXXXXXkoihMAlS",
	],
	"bindEnvironmentTotalCount":2,
	"bindEnvironments":[
		{
			"seviceId":"sevice-XX",
			"environmentName":"Test",
			
		},
		{
			"seviceId":"sevice-XXXX",
			"environmentName":"release"
		}	
	],
}
```





