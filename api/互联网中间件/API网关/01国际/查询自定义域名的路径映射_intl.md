## API Description
This API (DescribeServiceSubDomainMappings) is used to query the path mapping of the custom domain name.
API gateway can bind the custom domain name to a service, and can map the path of the custom domain name to three environments of the service. This API is used to query the list of path mapping of the custom domain names under a service.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| --------- | ---- | ------ | ----------- |
| serviceId | Yes | String | The unique ID of the service. |
| subDomain | Yes | String | The custom domain name bound to the service. |

## Output Parameters
| Parameter Name | Type | Description |
| ---------------- | ------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| isDefaultMapping | String | Whether to use default path mapping. TRUE: Using the default path mapping; FALSE: Using the custom path mapping, and pathMappingSet is not empty at this time. |
| pathMappingSet | List of Array | The list of custom path mapping. |

pathMappingSet is a list of custom path mapping, consisting of the following items:

| Parameter Name | Type | Description |
| ----------- | ------ | ------------- |
| path | String | The path of the custom path mapping. |
| environment | String | The environment name of the custom path mapping. |


## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeServiceSubDomainMappings
&serviceId=service-XXXX
&subDomain=www.qq.com
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
	"totalCount":2,
	"isDefaultMapping":"FALSE",
	"pathMapping":[
		{
			"path":"/path1",
			"environment":"release",
		},
		{
			"path":"/path2",
			"environment":"test",
		}
	]
}
```





