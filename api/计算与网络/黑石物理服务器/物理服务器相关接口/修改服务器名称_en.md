## 1. API Description

This API (ModifyDeviceAlias) is used to modify CPM alias. Batch modification is supported.
Domain for API request: <font style="color:red">bm.api.qcloud.com</font>




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
<td> aliases
<td> Yes
<td> String array
<td> Name list of the corresponding instanceIds array
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
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="/doc/api/456/6725" title="Common Error Codes">Common Error Codes</a> on the Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.

</tbody></table>



## 4. Module Error Codes

| code | codeDesc | Description |
|------|------| -----|
| 9001 | InternalError.DbError | Error occurred when operating the database |
| 10001 | InvalidParameter | Invalid parameter |


## 5. Example
Input
<pre>
https://bm.api.qcloud.com/v2/index.php?
Action=ModifyDeviceAlias
&instanceIds.0=cpm-34xs43xs
&aliases.0=test
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```


