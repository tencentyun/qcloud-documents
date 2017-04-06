## 1. API Description
 
Domain: vod.api.qcloud.com
API name:  DeleteClass 

Used to delete categories to manage video files. This operation is considered global, category association of specific files is not involved. Refer to ModifyVodInfo function for detailed file operations.

 

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
  https://domain/v2/index.php?Action=DeleteClass&classId=108&<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>
</pre>
Output 1
```

{
    "code" : 0,
    "message" : "",
}

```



