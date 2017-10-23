## 1. API Description
This API (CreateVpcPeeringConnection) is used to create regional peering connection.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

1) Regional peering connection is used to establish connectivity between two VPCs within the same region. The segments of the two VPCs that need to interconnect with each other cannot overlap. For more information, refer to <a href="https://cloud.tencent.com/doc/product/215/1685" title="Peering Connection">Peering Connection</a>.
2) Cross-account peering connection will take effect only after the receiver accepts the request. The connection between the same accounts will take effect immediately.
3) There is no limit for the traffic of regional peering connection.
4) Regional peering connection is available for free.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is CreateVpcPeeringConnection.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | ID of VPC, which can be vpcId or unVpcId. unVpcId is recommended. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>. |
| peerVpcId | Yes | String | Receiver's VPC ID, which can be vpcId or unVpcId. unVpcId is recommended. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>. |
| peerUin | Yes | String | Receiver's uin.  |
| peeringConnectionName | Yes | String | Peering connection name. You can specify any name you like, but its length should be limited to 60 characters. The name must be unique within the same VPC.  |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed. |
| message | String | Error message. |
| peeringConnectionId | String | Peering connection ID assigned by the system, e.g. pcx-6gw5wvmk |  |

## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidPeeringConnectionName | Invalid peering connection name. You can specify any name you like, but its length should be limited to 60 characters.  |
| PeeringConnectionVpcConflict | Conflict occurs between VPC segments in peering connection |
| PeeringConnectionLimitExceeded | The limit of requested peering connection resources for the specified region has been reached. Please contact customer service for more resources. For more information, see <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Service Limits">VPC Service Limits</a>.  |
| InvalidVpc.NotFound | VPC does not exist. Please verify that you have entered resource information correctly.  |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateVpcPeeringConnection
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=gz_vpc_226
&peerVpcId=gz_vpc_89
&peerUin=2407912486
&peeringConnectionName=tses
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "peeringConnectionId":"pcx-6gw5wvmk"
}
```


