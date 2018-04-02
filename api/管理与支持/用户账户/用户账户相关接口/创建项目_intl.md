## 1. API Description
This API (AddProject) is used to add a project. The project is a virtual concept. A user can create multiple projects under an account, with different resources managed in each project.

Domain name: account.api.qcloud.com

 

## 2. Input Parameters 
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> projectName <td> Yes <td> String <td> Name of the project to be added, which can only consist of "Chinese", "English" or "digits" 
<tr>
<td> projectDesc <td> No <td> String <td> projectDesc
</tbody></table>

 

## 3. Output Parameters 
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code <td> Int <td> Error code, 0: Successful; other values: Failed. 
<tr>
<td> message <td> String <td> Error message 
<tr>
<td> projectId <td> Int <td> projectId
</tbody></table>

 

## 4. Example 
 
Input
<pre>
  https://account.api.qcloud.com/v2/index.php?Action=AddProject
  &projectName=test
  &projectDesc=Used for testing
  &<a href="https://cloud.tencent.com/doc/api/229/6976">Public Request Parameters</a>
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "projectId": 1002996
}
```


