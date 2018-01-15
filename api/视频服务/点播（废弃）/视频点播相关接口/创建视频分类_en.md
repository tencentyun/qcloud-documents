## 1. API Description
 
This API （CreateClass） is used to create categories to manage video files. This is a global operation, which doesn't involve the category and association of specific files.  For details, see ModifyVodInfo function.

Domain: vod.api.qcloud.com
 

## 2. Input Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> className
<td> Yes
<td> String
<td> Category information
<tr>
<td> parentId
<td> No
<td> Int
<td> ID number of the parent category. A level-1 category will be created if this is left empty
</tbody></table>


 

## 3. Output Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error Code, 0:  Succeeded, other values:  Failed
<tr>
<td> newClassId
<td> String
<td> ID of the created category. ID for the top category is -1
<tr>
<td> message
<td> String
<td> Error Message
</tbody></table>


 

## 4. Example
 
Input 1
<pre>
  https://domain/v2/index.php?Action=CreateClass&className=forTt&parentId=-1&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output 1
```

{
    "code": 0,
    "message": "",
    "newClassId": "250"
}

```



