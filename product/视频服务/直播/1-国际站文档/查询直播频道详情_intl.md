## 1. API Description

Domain name: live.api.qcloud.com
 

This API (DescribeLVBChannel) is used to enter the ID number of a channel to be queried to get its current status, name, description, LVB source, and output source information.


## 2. Input Parameters
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> channelId
<td> <font color"red">Yes</font>
<td> Unsigned integer
<td> Channel ID
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
<td> channelInfo
<td> Array
<td> Channel information, such as its current status, name, description, LVB source, and output source information.
</tbody></table>

</b></th>

## 4. Example

Input 1
<pre>
https://domain/v2/index.php?Action=DescribeLVBChannel&channelId=96171715553394807&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>

Output 1
```
{
    "code": 0,
    "message": "",
    "channelInfo": [
        {
            "channel_id": "XXX",
            "channel_name": "XXX",
            "channel_describe": "XXX",
            "channel_status": "1",
            "upstream_list": [
                {
                    "sourceName": "RTMP",
                    "sourceID": "YYYYYYYYYYY",
                    "sourceType": "1",
                    "sourceAddress": "rtmp://2000.livepush.myqcloud.com/live/YYYYYYYYYYYYYYYYYY?bizid2000"
                }
            ],
            "hls_downstream_address": "",
            "rtmp_downstream_address": "rtmp://2000.liveplay.myqcloud.com/live/XXX",
            "player_id": "226",
            "resolution": null,
            "password": null
        }
    ]
}
```



## 5. Standard Parameter Definitions
Channel status definitions:
<table class="t"><tbody><tr>
<th><b>Value</b></th>
<th><b>Status</b></th>
<tr>
<td> 0
<td> No input stream
<tr>
<td>1
<td> LVB in progress
<tr>
<td> 2
<td> Exception
<tr>
<td> 3
<td>Disable
</tbody></table>

Receiver type definitions:
<table class="t"><tbody><tr>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> 1
<td> RTMP output
<tr>
<td>2
<td> HLS output
<tr>
<td> 3
<td> RTMP and HLS output
</tbody></table>
LVB stream protocol definitions:
<table class="t"><tbody><tr>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> 1
<td> RTMP push
<tr>
<td>2
<td>RTMP pull
<tr>
<td> 3
<td> HLS pull
</tbody></table>
