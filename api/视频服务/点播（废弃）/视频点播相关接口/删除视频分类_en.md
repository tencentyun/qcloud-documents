## 1. API Description
 
This API (DeleteClass) is used to delete categories to manage video files. This is a global operation, which doesn't involve the category and association of specific files. For details, see ModifyVodInfo function.

Domain: vod.api.qcloud.com

 

## 2. Input Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> classId
<td> Yes
<td> int
<td> Category ID
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
  https://domain/v2/index.php?Action=DeleteClass&classId=108&<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>
</pre>
Output 1
```

{
    "code" : 0,
    "message" : "",
}

```



