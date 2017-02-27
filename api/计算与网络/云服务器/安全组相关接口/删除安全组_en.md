## 1. API Description
 
This API (DeleteSecurityGroup) is used to delete new security groups.
Domain name for API request: <font style="color:red">dfw.api.qcloud.com</font>
1) Security groups can be deleted with the system-generated unique ID (a string with the prefix sg) as the index. Only security groups under the current account can be deleted.
2) By default, a security group cannot be deleted directly if there are any CVMs that haven't been unbound within the security group. You can add the forced = 1 parameter to have the system unbind all the associated CVMs before you can delete the current security group. If these CVMs were bound to more than one security group previously, the security groups not deleted by this operation will continue to stay bound to the CVMs.
3) A security group cannot be deleted directly if its ID is referenced in the rule of other security groups. In this case, you need to call DescribeAssociateSecurityGroups to query out these security groups and modify the rule before you can delete the original security group.
Once a security group is deleted, it cannot be recovered, so please proceed with the request with caution.

 

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Public request parameters need to be added when the API is called. See the Public Request Parameters page for details. The Action field for this API is DeleteSecurityGroup.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> sgId <td> Yes <td> String <td> Unique security group ID; may derive from DescribeSecurityGroups or CreateSecurityGroup
<tr>
<td> forced <td> No <td> Int <td> Forced execution or not; this parameter must be passed for a security group bound to CVMs to be deleted; the value is 0 by default
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
<td> 7001 <td> The security group does not exist
<tr>
<td> 7006 <td> The system prohibits deleting the security group by default
</tbody></table>


## 5. Example
 
Input
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=DeleteSecurityGroup
  &sgId=sg-c3y9ak17
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Public request parameters</a>>

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```

