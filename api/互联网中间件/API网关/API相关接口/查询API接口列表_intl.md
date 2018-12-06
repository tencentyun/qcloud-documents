## API Description
This API (DescribeApisStatus) is used to view a certain API or the list of all APIs under a service and relevant information.
​
## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ---------- | ---- | ------ | ---------------------------------------- |
| serviceId | Yes | String | Unique ID of the service of the API. |
| apiIds.n | No | String | Unique ID array of the API. |
| offset | No | Int | Offset. Default is 0. |
| limit | No | Int | Number of returned results. Default is 20. Maximum is 100. |
| orderby | No | String | Sorting field. |
| order | No | String | Sorting mode. |
| searchName | No | String | Conducts fuzzy search based on API path name. |
| searchId | No | String | Conducts exact search based on the unique ID of the API. |


## Output Parameters
| Parameter Name | Type | Description |
| -------------- | ------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| serviceId | String | Unique ID of the service of the API. |
| totalCount | Int | Number of APIs that meet the condition. |
| apiIdStatusSet | List of Array | API list. |

"apiIdStatusSet" is an array of "apiIdStatus", which is composed as follows:

| Parameter Name | Type | Description |
| ------------ | --------- | ---------------------------------------- |
| apiId | String | Unique ID of the API. |
| apiDesc | String | The custom description of the API. |
| apiName | String | API name. |
| apiType | String | API type. Only "NORMAL" is supported and other types will be available soon. |
| path | String | API request path. |
| method | Int | API request method. |
| createdTime | Timestamp | Creation time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |
| modifiedTime | Timestamp | Last modification time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |
| authRequired | String | Indicates whether signature verification is required. TRUE: required; FALSE: not required. |

## Example 

Query the details of an API of which the backend service type is HTTP:

The request example is as below:
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeApisStatus
&serviceId=service-XX
&apiIds.0=api-XX
&apiIds.1=api-XXX
&offet=0
&limit=2
&orderby=createdTime
&order=desc
&searchKey=aa
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success", 
    "serviceId":"service-XX",
    "totalCount":2,
	"apiIdStatusSet":[
		{
			"apiId":"api-XX",
			"apiName":"apiXXXX",
			"apiType":"NORMAL",
			"apiDesc":"apiDescription1",
			"path":"path1",
			"method":"http",
			"serviceId":"serviceId-XXX",
			"createdTime":"2017-08-07T00:00:00Z",
			"modifiedTime":"2017-08-07T00:00:00Z",
			"authRequired":"TRUE"
		},
		{
			"apiId":"api-XXX",
			"apiName":"apiXXXX",
			"apiType":"NORMAL",
			"apiDesc":"apiDescription2",
			"path":"path2",
			"method":"https",
			"serviceId":"serviceId-XXXX",
			"createdTime":"2017-08-07T00:10:00Z",
			"modifiedTime":"2017-08-07T00:10:00Z",
			"authRequired":"TRUE"
		}
	]
}
```

