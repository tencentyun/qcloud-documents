## API Description

This API (DescribeService) is used to query the details of a service, including its description, domain name, protocol, creation time, publishing etc.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| --------- | ---- | ------ | ----------- |
| serviceId | Yes | String | The unique ID of the service to be queried. |

## Output Parameters

| Parameter Name | Type | Description |
| --------------------- | -------------- | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| serviceId | String | The unique ID of the service. |
| serviceName | String | User-defined service name. |
| serviceDesc | String | Service description. |
| subDomain | String | The domain name that the system assigns to the service automatically. |
| protocol | String | Frontend request type of the service, such as HTTP and HTTPS. |
| createdTime | Timestamp | Creation time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |
| modifiedTime | Timestamp | Last modification time. It is in the format of YYYY-MM-DDThh:mm:ssZ according to the ISO8601 standard. UTC time is used. |
| availableEnvironments | List Of String | The list of published environments, such as Test, Pre, release. |

## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=DescribeService
&serviceId=service-XX
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
	"serviceId":"service-XX",
	"serviceName":"test1",
	"serviceDesc:"test1",
	"subDomain":"523e8dc7bbe04613b5b1d726c2a7889d-apigateway.ap-guangzhou.qcloud.com",
	"protocol":"http",
	"createdTime":"2017-08-07T00:00:00Z",
	"modifiedTime":"2017-08-07T00:00:00Z",
	"availableEnvironments":[
		"Pre",
		"release"
	]
}
```





