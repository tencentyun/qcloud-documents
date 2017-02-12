## 1. API Description
 
This API (ModifySecurityGroupAttributes) is used to modify the attribute information of existing security groups, including the name and description.
Domain name for API request: <font style="color:red">dfw.api.qcloud.com</font>
1) Security group names and descriptions can be modified with the system-generated unique ID (a string with the prefix sg) as the index. Only security groups under the current account can be modified.
2) Modified security group names cannot be the same as the names of other security groups in the project, and must not be longer than 25 UTF-8 characters. Modified security group descriptions must not be longer than 100 UTF-8 characters.
3) Modifying the attribute information of security groups does not affect network security policies on bound CVMs.

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Public request parameters need to be added when the API is called. See the Public Request Parameters page for details. The Action field for this API is ModifySecurityGroupAttributes.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> sgId <td> Yes <td> String <td> Unique security group ID, e.g, sg-33ocnj9n; may derive from DescribeSecurityGroups or CreateSecurityGroup
<tr>
<td> sgName <td> No <td> String <td> New security group name; arbitrary naming is allowed; must be no more than 60 characters in length
<tr>
<td> sgRemark <td> No <td> String <td> New security group remarks; must be no more than 100 characters in length
</tbody></table>

 

## 3. Output Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code <td> Int <td> Error code, 0: succeeded, other values: failed
<tr>
<td> message <td> String <td> Error message
</tbody></table>

 ## 4. Error Code Table
 <table class="t"><tbody><tr>
<th><b>Error Code Value</b></th>
<th><b>Cause</b></th>
<tr>

<td> 7000 <td> Security group backend exception
<tr>
<td> 7005 <td> The security group name already exists
<tr>
<td> 7006 <td> The system prohibits modifying the security group by default
<tr>
<td> 9003 <td> The security group name / remark is too long or contains invalid character(s)
</tbody></table>


## 5. Example
 
Input
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=ModifySecurityGroupAttributes
  &sgId=sg-o1wkaolh
  &sgName=Test 1
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Public request parameters</a>>

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```

