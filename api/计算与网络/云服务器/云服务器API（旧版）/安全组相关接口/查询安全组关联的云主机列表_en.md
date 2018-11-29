## 1. API Description
 
This API (DescribeInstancesOfSecurityGroup) is used to query CVMs associated with specified security groups.
Domain name for API request:<font style="color:red">dfw.api.qcloud.com</font>
1) This API can be used to query the information about a subset of the members in the CVM list, which is controlled by the input fields "offset" and "limit". When these fields are left empty, the first 20 CVMs will be queried by default.
2) A CVM can be associated with multiple security groups. The query results for different security groups may include duplicate CVM instance IDs.
3) The CVM list is returned in a list format. The list members are CVM instance IDs.

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Public request parameters need to be added when the API is called. See the Public Request Parameters page for details. The Action field for this API is DescribeInstancesOfSecurityGroup.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> sgId <td> Yes <td> String <td> Security group ID
<tr>
<td> offset <td> No <td> Int <td> The position where a page begins, 0 by default
<tr>
<td> limit <td> No <td> Int <td> Number limit, 20 by default
</tbody></table>

 

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: succeeded, other values: failed |
| message | String | Error message |
| totalCount | Int |Total number of associated CVM instances|
| data | Array | Returned data structure|

Data structure:
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> instanceId <td> Array <td> CVM instance ID, e.g., ins-a1iofc4j
</tbody></table>

 

## 4. Example
 
Input
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=DescribeInstancesOfSecurityGroup
  &sgId=sg-56p1yd1o
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>

</pre>

Output
```

{
    "code": 0,
    "message": "",
   "totalCount":0,
    "data": [
            {
                "instanceId": "ins-tks7a12z"
            }
     ]
}

```

