## 1. API Description

This API (RejectVpcPeeringConnection) is used to reject regional peering connection within the same region.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is RejectVpcPeeringConnection.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| peeringConnectionId | Yes | String | ID of VPC peering connection, e.g. pcx-8g675gr8. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed. |
| message | String | Error message. |

## 4. Error Codes
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
	
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | VPC does not exist. Please check the information your entered. |
| InvalidPeeringConnection.NotFound | Peering connection does not exist. Please check the information your entered.|

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=RejectVpcPeeringConnection
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&peeringConnectionId=pcx-8g675gr8
</pre>
Output
```
{
    "code":"0",
    "message":""
}
```


