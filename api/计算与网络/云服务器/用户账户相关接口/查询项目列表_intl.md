## 1. API Description
 
Domain name: account.api.qcloud.com


This API (DescribeProject) is used to query project list. Project is a virtual concept. Users can create multiple projects under one account and manage different resources in each project.

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> Null <td> -- <td> -- <td> --
</tbody></table>

 

## 3. Output Parameters
 | Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Successful; other values: Failed |
| message | String | Error Message |
| data | Array | Returned lists |

Parameter data is composed as follows: 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> projectName <td> String <td> Project name
<tr>
<td> projectId <td> String <td> Project ID
<tr>
<td> createTime <td> String <td> Creation time of project
<tr>
<td> creatorUin <td> String <td> Project creator
</tbody></table>

 

## 4. Example
 
Input
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=DescribeProject
  &<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "data": [
        {
            "projectName": "test1",
            "projectId": 1002189,
            "createTime": "2015-04-28 14:42:53",
            "creatorUin": 670569769
        },
        {
            "projectName": "test2",
            "projectId": 1002190,
            "createTime": "2015-04-28 14:42:57",
            "creatorUin": 670569769
        }
    ]
}
```


