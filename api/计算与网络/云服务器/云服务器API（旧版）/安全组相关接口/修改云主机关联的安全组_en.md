## 1. API Description
 
This API (ModifySecurityGroupsOfInstance) is used to modify security groups associated with specified CVMs.
Domain name for API request: dfw.api.qcloud.com
1) CVMs are used as the index for operations with this API. The list of security group IDs to associate with needs to be set individually for each CVM.
2) Past-due CVMs or those in the process of migration and change are not allowed to be associated with security groups.
3) This API is used to modify the security groups associated with the primary ENI of the CVM. For other ENIs, please use ModifySecurityGroupsOfNetworkInterface.
4) Once this API is called, the new security group association will overwrite the previous ones. If you want to add new associated security groups but not to change the existing ones, please include all security group information in "sgId". To remove a security group, just delete it from the "sgId" parameter.
5) Similar to rules in security groups, security groups associated with one CVM are in a certain order, and take effect in the order the sgIds entered for this API are presented in. When your security group rule contains action = drop, a change in the order may lead to different network protection results, so you should be careful when making modifications.

## 2. Input Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> instanceSet <td> Yes <td> Array <td> List of security group associated with this CVM
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

## 4. Error CodeS
 <table class="t"><tbody><tr>
<th><b>Error Code</b></th>
<th><b>Description</b></th>
<tr>

<td> 7000 <td> Security group backend exception
<tr>
<td> 7003 <td> This CVM cannot be associated now
</tbody></table>
 

## 5. Example
 
Input
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=ModifySecurityGroupsOfInstance
  &instanceSet.0.instanceId=ins-4q118hl2
  &instanceSet.0.sgIds.0=sg-1sdj39df
  &instanceSet.0.sgIds.1=sg-o8sk37is
  &<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```

