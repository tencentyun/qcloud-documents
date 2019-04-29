## 1. API Description

Domain name: live.api.qcloud.com
API name: StopLVBChannel

Enter the ID of an LVB channel to stop the channel (channels can be stopped in batch).


## 2. Input parameters
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> channelIds
<td> <font color"red">Yes</font>
<td> Array
<td> Channel ID value, batch operation supported. See examples for how to use
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
</tbody></table>

</b></th>

## 4. Example

Input 1
<pre>
https://domain/v2/index.php?Action=StopLVBChannel&channelIds.1=96171715553394810&<a href="https://cloud.tencent.com/doc/api/229/6976">Public Request Parameters</a>
</pre>

Output 1
```
{
    "code" : 0,
    "message" : "",
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
