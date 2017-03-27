## 1. API Description
 
Domain: vod.api.qcloud.com
API name:  CreateClass

Used to create categories to manage video files. This operation is considered global, category association of specific files is not involved. Refer to ModifyVodInfo function for detailed file operations.

 

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
  https://domain/v2/index.php?Action=CreateClass&className=forTt&parentId=-1&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output 1
```

{
    "code": 0,
    "message": "",
    "newClassId": "250"
}

```



