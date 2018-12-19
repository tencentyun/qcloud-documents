## 1. API Description
This API (DescribeTaskInfo) is used to query the results of a task.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when API is called. For more information, please see <a href='https://cloud.tencent.com/document/api/239/7200' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is DescribeTaskInfo.

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> requestId<td> Yes <td> UInt <td> Task ID
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
<td> data <td> Array <td> Returned array of data
</tbody></table>

**Array data is composed as follows:**

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> data.status <td> Int <td> Task status. 0: To be executed; 1: Executing, 2: Succeeded; 3: Failed; -1: Execution Error |
</tbody></table>

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11201 | InvalidParameter | Incorrect business parameter |

 
## 5. Example
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=DescribeTaskInfo
&<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
&requestId=11963
</pre>
The returned results are as below:
```
{
    "code": 0,
	"message": "",
	"codeDesc": "Success",
    "data": {
        "status": 2
    }
}
```
