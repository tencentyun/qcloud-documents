## 1. API Description

Domain name: live.api.qcloud.com
API name: CreateLVBShot

Note: **If you want to enable screen capturing via APIs, please submit us a ticket for related backend configurations.**

Note:
1. Screenshots are captured based on the original bit rate, and the frequency is one screenshot every 10 seconds which is fixed and cannot be modified;
2. The output format is JPG;
3. After the task is started, it is expected that the corresponding file will be obtained in 20 seconds after the LVB time.



## 2. Input parameters
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> channelId
<td> Yes
<td> String
<td> Channel ID
<tr>
<td> startTime
<td> No
<td> String
<td> The start time, 2 minutes later by default
<tr>
<td> endTime
<td> No
<td> String
<td> The end time, one day after the start time by default
</tbody></table>


</b></th>

## 3. Output parameters
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error code, 0: succeeded; other values: failed
<tr>
<td> message
<td> String
<td> Error message
<tr>
<tr>
<td> task_id
<td> Int
<td> Task ID
<tr>

</tbody></table>


</b></th>

## 4. Example

Input 1
<pre>

http://domain/v2/index.php?Action=CreateLVBShot&channelId=123&start_time=2016-01-21 12:00:00&<a href="https://www.qcloud.com/doc/api/229/6976">Public Request Parameters</a>




</pre>

Output 1
```
{

   "code": 0,
"message": "",
"task_id": "1"

}

```

