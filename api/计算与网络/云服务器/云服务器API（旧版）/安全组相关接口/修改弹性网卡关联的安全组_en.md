## 1. API Description
This API (ModifySecurityGroupsOfNetworkInterface) is used to modify security groups associated with specified ENIs.
Domain name for API request: <font style="color:red">dfw.api.qcloud.com</font>
1) ENIs are used as the index for operations with this API. The list of security group IDs to associated with needs to be set individually for each ENI.
2) After the API is called, the new security group association will overwrite the previous ones. If you want to add new security groups and keep the existing ones, please enter all IDs of security group you want in the sgIds parameter. To remove a security group, just remove its ID from the sgIds parameter.
3) Similar to rules in security groups, security groups associated with one ENI are in a certain order, and take effect in the order the sgIds entered for this API are presented in. When your security group rule contains action = DROP, a change in the order may lead to different network protection results, so you should be careful when making modifications.

## 2. Input Parameters
Only request parameters of this API are listed below. Public request parameters need to be added when the API is called. See the Public Request Parameters page for details. The Action field for this API is ModifySecurityGroupsOfNetworkInterface.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> networkInterfaceSet <td> Yes <td> Array <td> List of security groups accossicated with an ENI
</tbody></table> 

Data fields for ENI and security group association
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> networkInterfaceId <td> Yes <td> String <td> ENI ID; associates all the passed ENIs with all the passed security groups in order
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

## 4. Error Codes
 <table class="t"><tbody><tr>
<th><b>Error Code</b></th>
<th><b>Description</b></th>
<tr>
<td> 7000 <td> Security group backend exception
</tbody></table>

## 5. Example
 
Input
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=ModifySecurityGroupsOfInstance
  &networkInterfaceSet.0.networkInterfaceId=eni-3056glfn
  &networkInterfaceSet.0.sgIds.0=sg-1sdj39df
  &networkInterfaceSet.0.sgIds.1=sg-o8sk37is
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```
