## 1. API Description
Domain name: live.api.qcloud.com
API name: DescribeLVBChannelList

Obtain all LVB channel information of a user, including channel ID, current status, name, and creation time.


## 2. Input parameters
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> channelStatus
<td> <font color"red">No</font>
<td> Unsigned integer
<td> Channel status, used to filter channel list (0: without input stream; 1: with input stream; 2: exception; 3: Closed; 4: incomplete configuration)
<tr>
<td> ascDesc
<td> <font color"red">No</font>
<td> Unsigned integer
<td> Order the results are in. By default, the results are sorted by creation time. 0: by time in an ascending order; 1: by time in a descending order.
<tr>
<td> pageNo
<td> <font color"red">No</font>
<td> Unsigned integer
<td> Page number. For example, to view the list in page 3, set the value to 3.
<tr>
<td> pageSize
<td> <font color"red">No</font>
<td> Unsigned integer
<td> The number of channels displayed on each page.
<tr>
<td> orderBy
<td> <font color"red">No</font>
<td> String
<td> By default, the results are sorted by the channel creation time.
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
<td> all_count
<td> int
<td> Total number of channels
<tr>
<td> channelSet
<td> Array
<td> Channel list
</tbody></table>

</b></th>

## 4. Example

Input 1
<pre>
https://domain/v2/index.php?Action=DescribeLVBChannelList&channelStatus=0&ascDesc=1&pageNo=1&pageSize=10&<a href="https://cloud.tencent.com/doc/api/229/6976">Public Request Parameters</a>

</pre>

Output 1
```
{
    "code": 0,
    "message": "",
    "all_count": "2",
    "channelSet": [
        {
            "channel_id": "96171715553394811",
            "channel_name": "World Table Tennis Championship 3",
            "channel_status": "0",
            "create_time": "2015-07-23 20:05:52"
        },
        {
            "channel_id": "96171715553394810",
            "channel_name": "World Table Tennis Championship 2",
            "channel_status": "0",
            "create_time": "2015-07-23 19:54:05"
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
<td> Without input stream
<tr>
<td>1
<td> LVB in progress
<tr>
<td> 2
<td> Exception
<tr>
<td> 3
<td>Closed
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
Live streaming protocol definitions:
<table class="t"><tbody><tr>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> 1
<td> RTMP push
<tr>
<td>2
<td> RTMP pull
<tr>
<td> 3
<td> HLS pull
</tbody></table>
