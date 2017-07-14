## 1. API Description
This API (ShutdownDevice) is used to shut down CPMs. 
Domain: bm.api.qcloud.com


## 2. Input Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> instanceIds
<td> Yes
<td> String array
<td> Device ID list
<tr>
<td> opUin
<td> Yes
<td> String
<td> Operator's UIN
</tbody></table>



## 3. Output Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, see <a href="/doc/api/456/6725" title="Common Error Codes">Common Error Codes</a> on Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> data
<td> null
<td> 
</tbody></table>



## 4. Module Error Codes

| code | codeDesc | Description |
|------|------| -----|
| 9001 | InternalError.DbError | Error occurred when operating the database |
| 9005 | InternalError.RbmqError | Operating system queue error |
| 10001 | InvalidParameter | Invalid parameter |
| 12002 | OperationDenied.IncorrectInstanceStatus | Cannot shut down the device |


## 5. Example
Input
<pre>
https://bm.api.qcloud.com/v2/index.php?
Action=ShutdownDevice
&instanceIds_0=cpm-d1pryrrb
&instanceIds_1=cpm-d1yngex3
&opUin=1307774067
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": null
}
```


