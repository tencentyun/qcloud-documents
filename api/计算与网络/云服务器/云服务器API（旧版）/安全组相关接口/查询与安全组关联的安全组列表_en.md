## 1. API Description
 
This API (DescribeAssociateSecurityGroups) is used to query which security groups have outbound or inbound rules that contain the entered security group ID.
Domain name for API request: <font style="color:red">dfw.api.qcloud.com</font>
1) If the query for a security group ID does not return an empty result, then the security group cannot be directly deleted. You need to modify other security group rules that have referenced this ID.
If the rules of a security group contain the ID of its own, that security group will not show up in the query result. 

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Public request parameters need to be added when the API is called. See the Public Request Parameters page for details. The Action field for this API is DescribeAssociateSecurityGroups.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> sgIds.n <td> Yes <td> String <td> Security group ID list
</tbody></table>

 

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: succeeded, other values: failed |
| message | String | Error message |
| data | Object | Returned data structure|

Data structure

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> data.key <td> String <td> The associated security group ID
<tr>
<td> data.value <td> String <td> The associated security group ID
</tbody></table>

## 4. Error Codes
<table class="t"><tbody><tr>
<th><b>Error Code</b></th>
<th><b>Description</b></th>
<tr>

<td> 7000 <td> Security group backend exception
<tr>
<td> 9003 <td> Empty input
</tbody></table>


## 5. Example
 
Input
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=DescribeAssociateSecurityGroups
  &sgIds.0=sg-5ua9adfv
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "data": {
        "sg-5ua9adfv": ['sg-exnsygsn']
    }
}

```

