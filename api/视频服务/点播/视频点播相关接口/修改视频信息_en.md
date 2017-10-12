## 1. API Description
 
This API (ModifyVodInfo) is used to modify the description information of video files, including category, name, and description.

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
<td> String
<td> File ID
<tr>
<td> fileName
<td> No
<td> String
<td> File name
<tr>
<td> fileIntro
<td> No
<td> String
<td> File description
<tr>
<td> classId
<td> No
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
<td> Error message
</tbody></table>

 

## 4. Example
 
Input 1
<pre>
  https://domain/v2/index.php?Action=ModifyVodInfo&fileId=16092504232103571137&fileName=NEW_NAME&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output 1
```

{
    "code" : 0,
    "message" : "",
}

```



