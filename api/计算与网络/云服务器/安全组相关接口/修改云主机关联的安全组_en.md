## 1. API Description
 
This API (ModifySecurityGroupsOfInstance) is used to modify security groups associated with specified CVMs.
Domain name for API request: dfw.api.qcloud.com
1) CVMs are used as the index for operations with this API. The list of security group IDs to associate with needs to be set individually for each CVM.
2) Past-due CVMs or those in the process of migration and change are not allowed to be associated with security groups until the situation returns to normal.
3) For a CVM associated with multiple NICs, this API modifies the security groups associated with the primary NIC of the CVM, and those bound to other elastic NICs will remain unchanged. To modify security groups of an elastic NIC, use ModifySecurityGroupsOfNetworkInterface.
4) After the API is called, the new security group association will overwrite the previous CVM association. If your CVM is associated with security groups A and B, and you want to associate security group C while retaining A and B, the entered sgIds parameter needs to contain A, B, and C. In case of removal of a security group, the entered sgIds parameter needs to contain the list of remaining security group IDs.
5) Similar to rules in security groups, security groups associated with one CVM are in a certain order, and take effect in the order the sgIds entered for this API are presented in. When your security group rule contains action = drop, a change in the order may lead to different network protection results, so you should be careful when making modifications.

## 2. Input Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> instanceSet <td> Yes <td> Array <td> Data list for CVM and security group association
</tbody></table> 
Data fields for elastic CVM and security group association
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> instanceId <td> Yes <td> String <td> CVM instance ID; associates all the passed virtual machines with all the passed security groups in order
<tr>
<td> sgIds <td> Yes <td> Array <td> List of unique IDs of associated security groups, in the order the sgIds members are presented in
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
<td> 7003 <td> The CVM is in a state in which association is prohibited
</tbody></table>
 

## 5. Example
 
Input
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=ModifySecurityGroupsOfInstance
  &instanceSet.0.instanceId=ins-4q118hl2
  &instanceSet.0.sgIds.0=sg-1sdj39df
  &instanceSet.0.sgIds.1=sg-o8sk37is
  &<a href="https://www.qcloud.com/doc/api/229/6976">Public request parameters</a>

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```

