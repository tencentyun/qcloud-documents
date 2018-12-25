## API Description

This API (DescribeServiceEnvironmentList) is used to query the list of environments of a service. All the environments and their statuses under the service can be queried.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| --------- | ---- | ------ | ----------- |
| serviceId | Yes | String | The unique ID of the service to be queried. |
| limit | No | Int | Number of results to be returned. |
| offset | No | Int | Offset. |

## Output Parameters
| Parameter Name | Type | Description |
| --------------- | ------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| totalCount | String | Total number of environments. |
| environmentList | List of Array | The list of environments. |

environmentList is a list of environments, which is an array of environmentAttribute. environmentAttribute is composed as follows:

| Parameter Name | Type | Description |
| --------------- | ------ | ------------------ |
| environmentName | String | The environment name. |
| url | String | The access path. |
| status | Int | Publishing status. 1: Published. 0: Not published |
| verisonName | String | The running version. |

## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeServiceEnvironmentList
&serviceId=service-XX
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
			"environmentName":"test",
			"url":"hahah.ap-guangzhou.1251000011.tencentyunapi.com/test",
			"status":0,
			"verisonName":""
		},
		{
			"environmentName":"pre",
			"url":"hahah.ap-guangzhou.1251000011.tencentyunapi.com/pre",
			"status":1,
			"verisonName":"version-20170904xx"
		}
	]
}
```





