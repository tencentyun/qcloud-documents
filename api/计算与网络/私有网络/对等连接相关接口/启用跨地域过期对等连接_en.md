## 1. API Description

This API (EnableVpcPeeringConnectionEx) is used to activate cross-region peering connection.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

If the receiver does not accept the request for a cross-account peering connection within 7 days after the request is initiated, the peering connection will expire. Upon the expiration, the receiver will not be able to perform any action on the peering connection. The initiator can use this API to enable the peering connection and notify the receiver to process the connection.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is EnableVpcPeeringConnectionEx.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| peeringConnectionId | Yes | String | ID of VPC peering connection, e.g. pcx-6gw5wvmk. | |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | int | Error code. 0: Succeeded; other values: Failed. |
| message | string | Error message. |
| taskId | int | Task ID. The operation result can be queried with taskId. For more information, refer to <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">API for Querying Task Execution Result</a>.  |

## 4. Error Code List
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
	
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | VPC not exist. Please check the information you entered. |
| InvalidPeeringConnection.NotFound | Peering connection not exist. Please check the information you entered.  |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=EnableVpcPeeringConnectionEx
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&peeringConnectionId=pcx-6gw5wvmk
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "taskId":1584
}
```


