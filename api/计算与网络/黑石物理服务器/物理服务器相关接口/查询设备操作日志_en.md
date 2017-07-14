## 1. API Description

This API (DescribeDeviceOperationLog) is used to acquire the operation log of device.
Domain for API request: <font style="color:red">bm.api.qcloud.com</font>



## 2. Input Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> instanceId
<td> Yes
<td> String
<td> Unique device ID
<tr>
<td> startTime
<td> No
<td> Date. e.g.: 2014-08-02
<td> Start time. Default is 7 days ago
<tr>
<td> endTime
<td> No
<td> Date. e.g.: 2014-08-02
<td> End time. Default is the current day
<tr>
<td> offset
<td> No
<td> Int
<td> Starting position
<tr>
<td> limit
<td> No
<td> Int
<td> Number of data entries
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
<tr>
<td> data
<td> Object
<td> Contains the attributes: logs, totalCount
<tr>
<td> data.logs
<td> Array
<td> The logs instance arrays that are returned. Data structure is shown in the table below
<tr>
<td> data.totalCount
<td> Int
<td> Total number of logs instance arrays that are returned
</tbody></table>

</b></th>Element structure of logs array</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> id
<td> Int
<td> log ID.
<tr>
<td> instanceId
<td> String
<td> Unique device ID.
<tr>
<td> taskId
<td> String
<td> Task ID.
<tr>
<td> appId
<td> Int
<td> User's appId.
<tr>
<td> taskName
<td> String
<td> Name of the operation task.
<tr>
<td> taskCName
<td> String
<td> Name description of the operation task.
<tr>
<td> startTime
<td> Date. e.g.: 2014-08-02
<td> Start time
<tr>
<td> endTime
<td> Date. e.g.: 2014-08-02
<td> End time
<tr>
<td> status
<td> Int
<td> 0: Executing; 1: Task succeeded; 2: Task failed
<tr>
<td> opUin
<td> String
<td> Operator's uIn.
<tr>
<td> memo
<td> String
<td> Note.
</tbody></table>


## 4. Module Error Codes

| code | codeDesc | Description |
|------|------|------|
| 9001 | InternalError.DbError | An error occurred when operating the database |
| 10001 | InvalidParameter | Invalid parameter |



## 5. Example
Input
<pre>
https://bm.api.qcloud.com/v2/index.php?
Action=DescribeDeviceOperationLog
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&Region=bj
&instanceId=cpm-d1pryrrb
&startTime=2016-08-02
&endTime=2016-10-12
&offset=0&limit=10
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "logs": [
            {
                "id": "6958",
                "instanceId": "cpm-d1pryrrb",
                "taskId": "10033",
                "appId": "0",
                "taskName": "bindEip",
                "taskCName": "Bind EIP",
                "startTime": "2016-10-11 19:54:37",
                "endTime": "2016-10-11 19:54:37",
                "status": "1",
                "opUin": "1307774067",
                "memo": "Bind EIP"
            },
            {
                "id": "6957",
                "instanceId": "cpm-d1pryrrb",
                "taskId": "10031",
                "appId": "0",
                "taskName": "unbindEip",
                "taskCName": "Unbind RIP",
                "startTime": "2016-10-11 19:53:10",
                "endTime": "2016-10-11 19:53:10",
                "status": "1",
                "opUin": "1307774067",
                "memo": "Unbind RIP"
            }
        ],
        "totalCount": 2
    }
}
```


