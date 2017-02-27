## 1. API Description

Domain name: live.api.qcloud.com
API name: CreateRecord

Note: Recording files are stored on the VOD platform. If you want to use the recording function, you need to activate a VOD account first and then ensure that the account is available. When recording files are stored, the charges (including charges for storage and downstream playback traffic) are calculated with VOD billing method. For more information, refer to [Relevant Document](https://www.qcloud.com/doc/product/266/%E4%BB%B7%E6%A0%BC%E6%80%BB%E8%A7%88).

Recording rules
1) The recording task starts at the preset time and ends when the LVB ends
2) The recording is fragmented by time, and the longest fragment time is 0.5 hour
3) The recording is stopped and a fragment is generated in case of a stream interruption
A new fragment recording task is started after the stream is recovered to repeat the preceding steps until the entire recording is completed
Fragment recording request URL format: http://(VOD bizid).vod.myqcloud.com/(vid).f0.flv
Or view the fragment on the VOD page

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
<td> The start time, 2 minutes later by default. To set it explicitly, set it to 2 minutes later
<tr>
<td> endTime
<td> No
<td> String
<td> The end time, one day after the start time by default</font>
<tr>

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
<td> task_id
<td> Int
<td> Task ID
</tbody></table>

</b></th>

## 4. Example

Input 1
<pre>

http://domain/v2/index.php?Action=CreateRecord&channelId=123&start_time=2016-01-21 12:00:00&<a href="https://www.qcloud.com/doc/api/229/6976">Public Request Parameters</a>

</pre>

Output 1
```
{
   "code": 0,
   "message": "",
   "task_id": "1"

}

```

