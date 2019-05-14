## 1. API Description

Domain name: live.api.qcloud.com

API name: CreateRecord

Note: Recorded files are stored on the VOD platform. If you want to use the recording feature, you need to activate a VOD account first and ensure that the account is available. When recorded files are stored, the charges (including charges for storage and downlink playback traffic) are calculated with VOD billing method. For more information, please see [relevant document](https://cloud.tencent.com/doc/product/266/%E4%BB%B7%E6%A0%BC%E6%80%BB%E8%A7%88).

Recording rules
1) The recording task starts at the preset time and ends when the LVB ends
2) The recording is fragmented by time, and the longest fragment time is 0.5 hour
3) The recording is stopped and a fragment is generated in case of a stream interruption
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
<td> No
<td> String
<td> Start time, which is 2 minutes later by default. To set it explicitly, set it to 2 minutes later. The time needs to be encoded.
<tr>
<td> endTime
<td> No
<td> String
<td> End time, which is one day after the start time by default. The time needs to be encoded</font>
<tr>
<tr>
<td> tapeType
<td> No
<td> String
<td> Whether to start the real-time video recording, with each fragment lasting less than 5 minutes. 0 means normal video, and 1 means Mini LVB. <br>(1) If real-time recording is enabled, the video recording starts at the moment when you call this API. In this case, the input parameter of task start time is invalid. <br>(2) When real-time recording is enabled, if the end time of task is input, the recording ends at this end time. If no end time is input, the recording automatically ends after 30 minutes. <br>(3) When real-time recording is enabled, if the difference between the start time of recording and the input end time of recording exceeds 30 minutes, the recording ends automatically after 30 minutes. It is recommend to limit the duration of real-time recording to 5 minutes on console.</font>
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
<td> Task ID, 64 bit unsigned integer
</tbody></table>

</b></th>

## 4. Example

Input 1
<pre>

http://domain/v2/index.php?Action=CreateRecord&channelId=123&start_time=2016-01-21%2012:00:00&<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>

Note: start_time needs to be encoded. 2016-01-21%2012:00:00 is encoded from 2016-01-21 12:00:00.
</pre>

Output 1
```
{
   "code": 0,
   "message": "",
   "task_id": 1

}

```


