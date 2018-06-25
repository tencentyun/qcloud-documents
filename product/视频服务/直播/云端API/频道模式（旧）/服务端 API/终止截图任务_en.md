## 1. API Description

Domain name: live.api.qcloud.com
API name: StopLVBShot

Note: The screenshot files are stored on COS for long-term storage. You need to activate the service before you can use this feature, and you will be charged a fee (for the storage and etc.) based on the billing mode for COS. For more information, refer to [Relevant Document](http://cloud.tencent.com/product/cos.html).



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
<td> taskId
<td> Yes
<td> Int
<td> Task ID
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
<tr>

</tbody></table>


</b></th>

## 4. Example

Input 1
<pre>

http://domain/v2/index.php?Action=StopLVBShot&channelId=123&taskId=1&<a href="https://cloud.tencent.com/doc/api/229/6976">Public Request Parameters</a>

</pre>

Output 1
```
{

   "code": 0,
"message": "",

}

```

