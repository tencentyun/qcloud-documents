## 1. API Description

Domain name: live.api.qcloud.com
 

Note: This API (StopRecord) is used to store recorded files on the VOD platform. If you want to use the recording feature, you need to activate a VOD account first and ensure that the account is available. When recording files are stored, the charges (including charges for storage and downstream playback traffic) are calculated with VOD billing method. For more information, please see [relevant document](https://cloud.tencent.com/document/product/267/2818).



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
<td> taskId
<td> Yes
<td> Int
<td> Task ID
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

</tbody></table>

</b></th>

## 4. Example

Input 1
<pre>

http://domain/v2/index.php?Action=StopRecord&channelId=123&taskId=1&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>


</pre>

Output 1
```
{
    "code": 0,
    "message": "",
}

```


