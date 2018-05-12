## 1. API Description

This API (ModifyVpcPeeringConnection) is used to modify the attributes of regional peering connection.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is ModifyVpcPeeringConnection.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| peeringConnectionId | Yes | String | ID of VPC peering connection, e.g. pcx-krmzap90. |
| peeringConnectionName | Yes | String | Peering connection name. You can specify any name you like, but its length should be limited to 60 characters. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed. |
| message | String | Error message. |

## 4. Error Codes
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error code | Description |
|---------|---------|
| InvalidPeeringConnectionName | Invalid peering connection name. It should be within 60 characters.  |
| InvalidVpc.NotFound | VPC not exist. Please check the information you entered.|
| InvalidPeeringConnection.NotFound |Peering connection not exist. Please check the information you entered. |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=ModifyVpcPeeringConnection
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&peeringConnectionId=pcx-krmzap90
&peeringConnectionName=uuuuuuu
</pre>
Output
```
{
    "code":"0",
    "message":""
}
```


