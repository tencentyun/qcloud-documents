## 1. API Description

Domain name: live.api.qcloud.com
 

Note: **<font color='red'>This API (CreateRecord) is used to store recorded files on the VOD platform. If you want to use the recording feature, you need to activate VOD Service first</font>**. When recording files are stored, the charges (including charges for storage and downstream playback traffic) are calculated with VOD billing method. For more information, please see [relevant document](https://cloud.tencent.com/doc/product/266/%E4%BB%B7%E6%A0%BC%E6%80%BB%E8%A7%88). Note: API calling timeout should be greater than 3 seconds, because retries within 3 seconds and frequent calls may lead to duplicate recording tasks.

Recording rules
(1) The recording task starts at the preset time and ends when the LVB ends
(2) The recording is fragmented by time, and the longest fragment time is 0.5 hour
(3) The recording is stopped and a fragment is generated in case of a stream interruption
A new fragment recording task is started after the stream is resumed to repeat the preceding steps until the entire recording is completed
Fragment recording request URL format: `http://(VOD bizid).vod.myqcloud.com/(vid).f0.flv`  
Or view the fragment on the VOD page

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
<td> Yes
<td> String
<td> Start time (China Standard Time), such as 2017-01-01 10:10:01
<tr>
<td> endTime
<td> Yes
<td> String
<td> End time (China Standard Time), such as 2017-01-01 10:10:01</font>
<tr>
<tr>
<td> tapeType
<td> Yes
<td> Int
<td> Whether to enable real-time recording. 1 - Enable; 0 - Disable; 1 is recommended.<br> a. Creating real-time recording tasks requires that VJs push streams actively. The video recording starts at the moment when this API is successfully called. In this case, the parameter of task start time is ignored.<br> b. The real-time recording task supports a maximum length of 30 minutes. If the time difference between the passed task end time and the current time is longer than 30 minutes, only a length of 30 minutes is recorded. The recommended recording length is within 5 minutes.<br> c. If real-time recording is disabled, the parameter of task start time is required, and the time difference between the end time and the start time should not be longer than 1 day.</font>
<tr>

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
<td> task_id
<td> Int
<td> Task ID. 64-bit unsigned integer
</tbody></table>

</b></th>

## 4. Example

Input 1
<pre>

http://domain/v2/index.php?Action=CreateRecord&channelId=123&tapeType=1&endTime=2016-01-21 12:00:00&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>

</pre>

Output 1
```
{
   "code": 0,
   "message": "",
   "task_id": 1

}

```


