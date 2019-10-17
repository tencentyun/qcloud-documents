## 1. API Description

Domain name: live.api.qcloud.com
 

This API (ModifyLVBChannel) is used to modify the basic information of LVB channels, including the channel name and description.


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
<tr>
<td> channelName
<td> <font color"red">Yes</font>
<td> String
<td> LVB channel name
<tr>
<td> channelDescribe
<td> <font color"red">No</font>
<td> String
<td> LVB channel description
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
</tbody></table>

</b></th>

## 4. Example

Input 1
<pre>
https://domain/v2/index.php?Action=ModifyLVBChannel&channelId=96171715553394807&channelName=test-15&channel
Describe=%E7%AC%AC15%E4%B8%AA%E6%B5%8B%E8%AF%95%E9%A2%91%E9%81%93%E7%94%A8%E4%BE%8B&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
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
