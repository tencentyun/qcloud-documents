## 1. API Description
This API (ModfiyRedisPassword) is used to modify the password for a CRS instance.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>

Rule on password: It should be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers, special characters (!, @, #, %, ^, ()).

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/api/239/7200' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is ModfiyRedisPassword.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> redisId <td> Yes <td> String <td> Instance ID
<tr>
<td> oldPassword <td> Yes <td> String <td> Old password
<tr>
<td> password <td> Yes <td> String <td> New password. Rule on password: It should be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers, special characters (!, @, #, %, ^, ()).
</tbody></table>

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
<tr>
<td> data <td> Array <td> Returned array</td>
</tbody></table>

**Array data is composed as follows:**
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> data.requestId <td> UInt <td> Task ID. You can use the API <a href='/doc/api/260/1387' >DescribeTaskInfo</a> to query the task execution status
</tbody></table>

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11201 | InvalidParameter | Incorrect business parameter |
| 10701 | InstanceNotExists | No instance can be found for the serialId |
| 10707 | InstanceLockedError | The operation is impossible because the instance is locked |
| 10702 | InstanceStatusAbnormal | The operation is impossible due to an abnormal instance status. For example, the instance has a status of "in process" or "isolated" or "deleted" |
| 10501 | PasswordEmpty | Password is left empty |
| 10502 | OldPasswordError | Wrong old password is entered for resetting password |
| 11058 | PasswordRuleError | Incorrect password rule. The password must be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers and special characters (!, @, #, %, ^, *, ()) |

## 5. Example
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=ModfiyRedisPassword
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
&redisId=crs-ifmymj41
&oldPassword=49A2d!e@f12e
&password=12D3E@!r5ed
</pre>
The returned results are as below:
```
{
    "code": 0,
    "message": "",
	"codeDesc": "Success",
	"data": {
        "requestId": 11966
    }
}
```

