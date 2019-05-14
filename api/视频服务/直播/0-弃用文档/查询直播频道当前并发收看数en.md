## 1. API Description
Domain name: live.api.cloud.tencent.com
API name: DescribeLVBOnlineUsers

Note: This API calculates the number of concurrent online users based on the number of access connections to the video distribution URL. If the RTMP downstream protocol is used, the calculated result can fully reflect the number of online users, or viewers. If the HLS or HLS/RTMP downstream protocol is used, the access connections calculated in real time may not accurately reflect the number of online users since HLS itself performs access based on the TS fragment characteristics, and can be used for reference only.


## 2. Input parameters

<table class="t"><tbody><tr>
<th><b>Parameter name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> channelIds.n
<td> No
<td> String
<td> Indicates a channel ID. If this parameter is empty, the total number of LVB channels is obtained.
</tbody></table>



## 3. Output parameters

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
<td> list
<td> Array
<td> Indicates a list set.
</tbody></table>

</b></th>List set</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> channelID
<td> String
<td> Channel ID
</tbody></table>

If the value of channel ID is -1, the number of online users for all channels is displayed.

## 4. Example

Query based on a video ID
Input
<pre>`https://domain/v2/index.php?Action=DescribeLVBOnlineUsers`
&<a href="https://cloud.tencent.com/doc/api/229/6976">Public Request Parameters</a>
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "list": [
        {
            "channelId": 123,
            "online": 1
        }
    ]
}

```

