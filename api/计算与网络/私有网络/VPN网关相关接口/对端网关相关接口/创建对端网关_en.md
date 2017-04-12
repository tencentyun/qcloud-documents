## 1. API Description

This API (AddUserGw) is used to create peer gateway.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font> 
 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is AddUserGw.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| userGwName | Yes | String | Peer gateway name, up to 60 characters, must be unique under the same developer account.  |
| userGwAddr | Yes | String | Public IP of the peer gateway. For example: 183.30.0.1.  |

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed.  |
| message | String | Error message.  |
| userGwId | String | Peer gateway ID assigned by the system. For example: cgw-e098slul |

## 4. Error Codes
 The following list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://www.qcloud.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error code | Description |
|---------|---------|
| InvalidUserGwName | Invalid peer gateway name. It should be within 60 characters.  |
| InvalidUserGw.InUse | Peer gateway public IP already in use. The peer gateway public IP must be unique under the same account.  |
| UserGwLimitExceeded | Reached the upper limit of requested peer gateways for the specific region. Please contact customer service for more resources. For more information, see <a href="https://www.qcloud.com/doc/product/215/537" title="VPC Service Limits"> VPC Service Limits</a>.  |

## 5. Example
 
Input
<pre>
  https://domain/v2/index.php?Action=AddUserGw
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
  &userGwName=ddtest
  &userGwAddr=183.30.0.1
</pre>

Output
```

{
    "code" : 0,
    "message" : "ok",
		"userGwId" : "cgw-e098slul"
}



