## 1. API Description

This API (DeleteVpcPeeringConnection) is used to delete regional peering connection.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

1) Either of the sides can delete the peering connection at any time. The peering connection becomes invalid immediately after being deleted.
2) When the peering connection is deleted, the routing entry containing this connection in the routing table will also be deleted.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DeleteVpcPeeringConnection.
 
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| peeringConnectionId | Yes | String | ID of VPC peering connection, e.g. pcx-0jtgah4s. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed. |
| message | String | Error message. |

## 4. Error Codes
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error code | Description |
|---------|---------|
| InvalidVpc.NotFound |VPC not exist. Please check the information you entered. |
| InvalidPeeringConnection.NotFound | Peering connection not exist. Please check the information you entered.|

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DeleteVpcPeeringConnection
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&peeringConnectionId=pcx-0jtgah4s
</pre>
Output
```
{
    "code":"0",
    "message":""
}
```


