## 1. API Description
 
This API (DeleteVodFile) is used to delete uploaded video files.

Domain: vod.api.qcloud.com 

 

## 2. Input Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> fileId
<td> Yes
<td> string
<td> File ID
<tr>
<td> priority
<td> Yes
<td> int
<td> You may enter 0. Priority 0: Medium. 1: High. 2: Low
</tbody></table>

 

## 3. Output Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error code. 0:  Succeeded, other values:  Failed
<tr>
<td> message
<td> String
<td> Error Message
</tbody></table>

 

## 4. Example
 
Input 1
<pre>
  https://domain/v2/index.php?Action=DeleteVodFile&fileId=16092504232103571364&priority=0&<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>
</pre>
Output 1
```

{
    "code" : 0,
    "message" : "",
}

```


