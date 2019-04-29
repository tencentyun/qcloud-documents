## 1. API Description
This API (CreateVpcPeeringConnectionEx) is used to create cross-regional peering connection.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

1) Cross-regional peering connection is used to establish connectivity between VPCs in two different regions. The segments of the two VPCs that need to interconnect with each other cannot overlap. For more information, refer to <a href="https://cloud.tencent.com/doc/product/215/1685" title="About Peering Connection">About Peering Connection</a>.
2) Cross-account peering connection will take effect only after the receiver accepts the request. The connection between the same accounts will take effect immediately.
3) You can set the bandwidth for cross-regional interconnection. For any changes after creation of the peering connection, please contact customer service.
4) For more information about the regions, bandwidth limit, billing methods supported for cross-regional peering connection, refer to <a href="https://cloud.tencent.com/doc/product/215/1685" title="About Peering Connection">About Peering Connection</a>.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is CreateVpcPeeringConnectionEx.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | ID of VPC, which can be vpcId or unVpcId. unVpcId is recommended. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>. |
| peerVpcId | Yes | String | Receiver's VPC ID, which can be vpcId or unVpcId. unVpcId is recommended. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>. |
| peerUin | Yes | String | Receiver's unique account ID on Tencent Cloud. You can check this in the personal information at User Center by contacting receiver. <a href="https://cloud.tencent.com/doc/product/215/5000#.E6.9F.A5.E7.9C.8B.E5.AF.B9.E7.AB.AF.E8.B4.A6.E5.8F.B7id">Click here to view instructions</a>. |
| peeringConnectionName | Yes | String | Peering connection name. You can specify any name you like, but its length should be limited to 60 characters.|
| peerRegion | Yes | String | Receiver's region. For more information about the supported regions, refer to <a href="https://cloud.tencent.com/doc/product/215/1685" title="About Peering Connection">About Peering Connection</a>.  |
| bandwidth | Yes | String | Upper limit of bandwidth for peering connection (in Mbps). There is no limit by default. For more information about the limit, refer to <a href="https://cloud.tencent.com/doc/product/215/1685" title="About Peering Connection">About Peering Connection</a>. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed. |
| message | String | Error message. |
| taskId | Int | Task ID. The creation result can be queried with taskId. For more information, refer to <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">API for Querying Task Execution Result</a>.  |


## 4. Error Codes
The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidPeeringConnectionName | Invalid peering connection name. It should be within 60 characters.  |
| InvalidPeeringConnectionName.InUse | The peering connection name is already in use. The peering connection name must be unique within the same VPC.  |
| PeeringConnectionVpcConflict | Conflict occurs between VPC IP address range in peering connection |
| PeeringConnectionLimitExceeded | The limit of requested peering connection resources for the specified region has been reached. Please contact customer service for more resources. For more information on VPC resources restrictions, refer to <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Service Limits">VPC Service Limits</a>.  |
| InvalidVpc.NotFound |VPC does not exist. Please check the information you entered. |


## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateVpcPeeringConnectionEx
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=gz_vpc_226
&peerVpcId=gz_vpc_89
&peerUin=2407912486
&peeringConnectionName=tses
&peerRegion=gz
&bandwidth=20
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "taskId":112245
}
```


