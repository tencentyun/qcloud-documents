## 1. API Description

Domain name: live.api.qcloud.com
API name:  CreateLVBShot

> **Note: You need to complete the configuration at the video cloud backend before calling this API to enable the screenshot feature, otherwise the feature cannot be enabled normally. Before using this feature, you need to submit a ticket or contact the customer service by calling 4009-100-100.**

Note:
1. Screenshots are captured based on the original LVB bitrate. The frequency is one screenshot every 10 seconds, which is fixed and cannot be modified;
2. The output format is JPG;
3. When the task starts, you will obtain the screenshot file after 20 seconds upon the start of LVB process.


## 2. Input Parameters
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
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
<td> Start time, which is 2 minutes later by default. The time needs to be encoded
<tr>
<td> endTime
<td> No
<td> String
<td> End time, which is one day after the start time by default. The time needs to be encoded
</tbody></table>


</b></th>

## 3. Output Parameters
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error code. 0: Successful; other values: Failed
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
http://domain/v2/index.php?Action=CreateLVBShot&channelId=123&start_time=2016-01-21%2012%3A00%3A00&<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>

Note: 2016-01-21%2012%3A00%3A00 is encoded from 2016-01-21 12:00:00
</pre>

Output 1
```
{
   "code": 0,
"message": "",
"task_id": "1"

}

```


