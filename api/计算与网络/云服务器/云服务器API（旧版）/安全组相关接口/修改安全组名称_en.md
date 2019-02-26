## 1. API Description
 
This API (ModifySecurityGroupAttributes) is used to modify the names and descriptions of existing security groups.
Domain name for API request: <font style="color:red">dfw.api.qcloud.com</font>
1) Security group names and descriptions can be modified with the system-generated unique ID (a string with the prefix sg) as the index. You can only modify security groups under your current account.
2) Security group names in the same project must be unique. The security group name can contain up to 25 UTF-8 characters and the description can contain up to 100 UTF-8 characters.
3) Modifying the attribute information of security groups does not affect network security policies on bound CVMs.

## 2. Input Parameters
 
Only request parameters of this API are listed below. Public request parameters need to be added when the API is called. See the Public Request Parameters page for details. The Action field for this API is ModifySecurityGroupAttributes.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> sgId <td> Yes <td> String <td> Unique security group ID, e.g, sg-33ocnj9n; you can obtain it using DescribeSecurityGroups or CreateSecurityGroup
<tr>
<td> sgName <td> No <td> String <td> New security group name; up to 60 characters
<tr>
<td> sgRemark <td> No <td> String <td> New security group remarks; up to 100 characters
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

## 4. Error Codes
<table class="t"><tbody><tr>
<th><b>Error Code</b></th>
<th><b>Description</b></th>
<tr>

<td> 7000 <td> Security group backend exception
<tr>
<td> 7005 <td> The security group name already exists
<tr>
<td> 7006 <td> This is a preset security group and cannot be modified
<tr>
<td> 9003 <td> The security group name/remark is too long or contains invalid characters
</tbody></table>


## 5. Example
 
Input
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=ModifySecurityGroupAttributes
  &sgId=sg-o1wkaolh
  &sgName=Test 1
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```

