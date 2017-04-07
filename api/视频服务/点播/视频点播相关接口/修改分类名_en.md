## 1. API Description
 
Domain:  vod.api.qcloud.com
API name:  ModifyClass

Modify the category name

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> classId <td> Yes <td> Int <td> ID of the category to be modified
<tr>
<td> className <td> Yes <td> String <td> New category name
</tbody></table>

 

## 3. Output Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code <td> Int <td> Error code, 0:  Succeeded, other values:  Failed
<tr>
<td> message <td> String <td> Error message
</tbody></table>

 

## 4. Example
 
Input
<pre>
  https://domain/v2/index.php?Action=ModifyClass
  &classId=100
  &className=test
  &<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```



