## API Description

This API (DescribeUsagePlansStatus) is used to query one or more usage plan lists. You can get the names, descriptions and QPS details of the usage plans by using this API.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| -------------- | ---- | ---------------- | ------------------- |
| usagePlanIds.n | No | Array of Strings | Queries by the unique ID(s) of one or more usage plans. |
| offset | No | Int | Offset. Default is 0. |
| limit | No | Int | Number of returned results. Default is 20. Maximum is 100. |
| orderby | No | String | Sorting field. |
| order | No | String | Sorting mode. |
| searchName | No | String | Conducts fuzzy search based on the usage plan name. |
| searchId | No | String | Conducts exact search based on the unique ID of the usage plan. |

## Output Parameters

| Parameter Name | Type | Description |
| ------------------ | ------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| totalCount | Int | Number of usage plans matching the filter condition. |
| usagePlanStatusSet | List of Array | List of usage plans. |

"usagePlanStatusSet" is an array of "usagePlanStatus", which is composed as follows:

| Parameter Name | Type | Description |
| -------------------- | --------- | ---------------------------------------- |
| usagePlanId | String | The unique ID of the usage plan. |
| usagePlanName | String | The custom name of the usage plan. |
| usagePlanDescription | String | The custom description of the usage plan. |
| requestControlUnit | String | Unit of the request limit. Default is SECOND. Only SECOND is supported at the moment, and MINUTE and HOUR will be supported in the future. |
| requestControlNum | Int | Request limit. |
| createdTime | Timestamp | Creation time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |
| modifiedTime | Timestamp | Last modification time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |
| maxRequestNum | Int | Total request quota. -1: Disable. |


## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeUsagePlansStatus
&usagePlanIds.0=usagePlan-XX
&usagePlanIds.1=usagePlan-XXXX
&offset=0
&limit=2
&orderby=createdTime
&order=desc
&searchKey=aa
&filter.notServiceId=service-6qdpttk
&filter.environment=Test
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
    "totalCount":2,
	"usagePlanStatusSet":[
		{
			"usagePlanId":"usagePlan-XX",
			"usagePlanName":"test1",
			"usagePlanDescription":"test1",
			"maxRequestNumPreSec":500,
			"createdTime":"2017-08-07T00:00:00Z",
			"modifiedTime":"2017-08-07T00:00:00Z",
			"maxRequestNum": -1
		},
		{
			"usagePlanId":"usagePlan-XXXX",
			"usagePlanName":"test2",
			"usagePlanDescription":"test2",
			"maxRequestNumPreSec":500,
			"createdTime":"2017-08-07T00:10:00Z",
			"modifiedTime":"2017-08-07T00:10:00Z",
			"maxRequestNum": 100
		}
	]
}
```





