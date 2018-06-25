## 1. API Description 
This API (ModifyRedisProject) is used to modify the project to which a CRS instance belongs.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/api/239/7200' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is ModifyRedisProject.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|
| redisIds.n | Yes | String | An array of instance IDs, with the array subscript starting with 0. You can use the API [DescribeRedis](http://cloud.tencent.com/doc/api/260/1384) to query the instance IDs.|
| projectId | Yes | UInt | Project ID. This value is subject to the projectId returned via User Account > User Account-related API > [Query Project List](https://cloud.tencent.com/doc/api/403/4400) |

## 3. Output Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code <td> Int <td> Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page.
<tr>
<td> message <td> String <td> Error message
<tr>
<td> codeDesc <td> String <td> Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.
</tbody></table>

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11201 | InvalidParameter | Incorrect business parameter |
| 10701 | InstanceNotExists | No instance can be found for the serialId |

## 5. Example
<pre>
  https://redis.api.qcloud.com/v2/index.php?Action=ModifyRedisProject
	&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
	&redisIds.0=crs-ifmymj41
	&projectId=1004306
</pre>
The returned results are as below:
```
{
    "code": 0,
    "message": "",
	"codeDesc": "Success"
}
```
