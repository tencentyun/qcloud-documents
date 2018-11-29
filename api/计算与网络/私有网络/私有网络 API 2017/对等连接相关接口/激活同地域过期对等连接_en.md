## 1. API Description

This API (EnableVpcPeeringConnection) is used to activate expired regional peering connection.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

If the receiver does not accept the request for a cross-account peering connection within 7 days after the request is initiated, the peering connection become expired. Upon the expiration, the receiver will not be able to perform any action on the peering connection. The initiator can use this API to activate the peering connection and notify the receiver to process the request.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is EnableVpcPeeringConnection.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| peeringConnectionId | Yes | String | ID of VPC peering connection, e.g. pcx-6gw5wvmk. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed. |
| message | String | Error message. |

## 4. Error Codes
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
	
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound |VPC does not exist. Please check the information you entered.  |
| InvalidPeeringConnection.NotFound |Peering connection does not exist. Please check the information you entered. |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=EnableVpcPeeringConnection
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&peeringConnectionId=pcx-6gw5wvmk
</pre>
Output
```
{
    "code":"0",
    "message":""
}
```


