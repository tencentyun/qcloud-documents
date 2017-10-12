## 1. API Description

This API (DescribeVpcPeeringConnections) is used to query VPC peering connection.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DescribeVpcPeeringConnections.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | Initiator's VPC ID, which can be vpcId or unVpcId. unVpcId is recommended. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>. |
| peeringConnectionId | No | string | ID of VPC peering connection, e.g. pcx-dt8c7fa0. |
| peeringConnectionName | No | String | Peering connection name. |
| state | No | Int | Connection status<br>0: Requesting; 1: Connected; 2: Expired; 3: Rejected; 4: Deleted. |
| offset | No | Int | Offset of initial line. Default is 0. |
| limit | No | Int | Number of lines per page. Default is 20. A maximum of 50 is allowed. |
| orderField | No | String | Sort by a certain field. No sorting by default. <br>Available fields: peeringConnectionname, createTime. |
| orderDirection | No | String | Ascending order (asc) or descending order (desc). Default is desc. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed.
| message | String | Error message |
| totalCount | Int | Returned number of peering connections |
| data.n | Array | Peering connection information array |
| data.n.vpcId | String | Initiator's VPC ID, e.g. gz_vpc_245 | 
| data.n.unVpcId | String | Unified ID of initiator's VPC, e.g. vpc-8e0ypm3z | 
| data.n.peerVpcId | String | ID of receiver's VPC, e.g. gz_vpc_24 | 
| data.n.unPeerVpcId | String | Unified ID of receiver's VPC, e.g. vpc-8e0ypm35 | 
| data.n.appId | String | Initiator's appId | 
| data.n.peeringConnectionId | String | Peering connection ID, e.g. pcx-dt8c7fa0 | 
| data.n.peeringConnectionName | String | Peering connection name | 
| data.n.state | Int | Connection status<br>0: Requesting; 1: Connected; 2: Expired; 3: Rejected; 4: Deleted | 
| data.n.createTime | String | Creation time of peering connection | 
| data.n.uin | String | Your unique account ID on Tencent Cloud. You can check this on Tencent Cloud User Center. <a href="https://cloud.tencent.com/doc/product/215/5000#.E6.9F.A5.E7.9C.8B.E5.AF.B9.E7.AB.AF.E8.B4.A6.E5.8F.B7id">Learn more</a>. | 
| data.n.peerUin | String | Receiver's unique account ID on Tencent Cloud. The receivers can check this by themselves on Tencent Cloud User Center. <a href="https://cloud.tencent.com/doc/product/215/5000#.E6.9F.A5.E7.9C.8B.E5.AF.B9.E7.AB.AF.E8.B4.A6.E5.8F.B7id">Learn more</a>. | 

## 4. Error Codes
The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | VPC does not exist. Please check the information you entered.  |
| InvalidPeeringConnection.NotFound | Peering connection does not exist. Please check the information you entered. |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeVpcPeeringConnections
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&peeringConnectionId=pcx-dt8c7fa0
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "totalCount":"8",
    "data":[
        {
            "vpcId":"gz_vpc_245",
            "unVpcId":"vpc-8e0ypm3z",
            "peerVpcId":"gz_vpc_20",
            "unPeerVpcId":"vpc-kx49lmyv",
            "appId":"1351000042",
            "peeringConnectionId":"pcx-dt8c7fa0",
            "peeringConnectionName":"Example 1",
            "state":"1",
            "createTime":"2016-01-06 20:56:07",
            "uin":"909619400",
            "peerUin":"909619400"
        }
    ]
}
```


