## 1. API Description
 
This API (DescribeNetworkInterfacesOfSecurityGroup) is used to query ENI associated with specified security groups.
Domain name for API request: dfw.api.qcloud.com
(1) An ENI can be associated with multiple security groups. The query results for different security groups may include duplicate ENI instance IDs.
(2) The ENI list is returned in a list format. The list members are ENI instance IDs.

## 2. Input Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> sgId <td> Yes <td> String <td> Security group ID
</tbody></table> 

 
## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Successful; other values: Failed |
| message | String | Error message |
| totalCount | Int | Total number of associated ENIs |
| networkInterfaceSet | Array | Data structure of ENI list |

`networkInterfaceSet` structure:
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> networkInterfaceId <td> String <td> ENI ID, such as eni-3056glfn
</tbody></table>

## 4. Error Codes
 <table class="t"><tbody><tr>
<th><b>Error Code Value</b></th>
<th><b>Reason</b></th>
<tr>

<td> 7000 <td> Security group backend exception
<tr>
<td> 7001 <td> Security group does not belong to the current user
</tbody></table>
 

## 5. Example
 
Input
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=DescribeNetworkInterfacesOfSecurityGroup
  &sgId=sg-33ocnj9n
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output
```

{
    "code": 0,
    "message": "",
    "data": {
        "totalCount": 1,
        "networkInterfaceSet": [
            {
                "networkInterfaceId": "eni-3056glfn"
            }
        ]
    }
}

```


