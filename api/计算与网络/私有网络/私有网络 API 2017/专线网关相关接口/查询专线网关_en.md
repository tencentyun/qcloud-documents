## 1. API Description

This API (DescribeDirectConnectGateway) is used to query Direct Connect gateway.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DescribeDirectConnectGateway.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | VPC ID assigned by the system, e.g. vpc-dfg5445. |
| directConnectGatewayId | No | String | Direct Connect gateway ID assigned by the system, e.g. dcg-4d545d. |
| directConnectGatewayName | No | String | Direct Connect gateway name. Fuzzy query is supported. |
| offset | No | Int | Offset of initial line. Default is 0. |
| limit | No | Int | Number of lines per page. Default is 20. Maximum is 50. |
| orderField | No | String | Sort by a certain field. Currently, sorting by createTime (default) and directConnectGatewayName is supported.  |
| orderDirection | No | String | Ascending order (asc) or descending order (desc). Default is desc.  |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| totalCount | Int | Total number of Direct Connect gateways to be queried. |
| data.n | Array | VPC information array. |
| data.n.vpcId | String | vpcId assigned by the system, e.g. gz_vpc_266. |
| data.n.unVpcId | String | Unified vpc ID assigned by the system, e.g. vpc-d454dd. |
| data.n.directConnectGatewayName | String | Direct Connect gateway name. |
| data.n.directConnectGatewayId | String | Direct Connect gateway ID assigned by the system, e.g. dcg-dgd454. |
| data.n.type | Int | Type of Direct Connect gateway; 0: Non-NAT; 1: NAT. |
| data.n.snatNum | Int | Number of local IP translation rules. |
| data.n.dnatNum | Int | Number of peer IP translation rules. |
| data.n.snaptNum | Int | Number of local source IP port translation rules. |
| data.n.dnaptNum | Int | Number of local destination IP port translation rules. |
| data.n.createTime | String | Creation time. |

## 4. Error Codes
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that you have entered resource information correctly.  |
| InvalidDirectConnectGateway.NotFound | Invalid Direct Connect gateway. Direct Connect gateway resource does not exist. Please verify that you have entered resource information correctly.  |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeDirectConnectGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-dfgg190
&directConnectGatewayId=dcg-ddf14d
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "totalCount": 1,
    "data": [
        {
            "vpcId": "gz_vpc_20",
            "vpcName": "vpc20联调dondon666",
            "directConnectGatewayId": "dcg-46i442a7",
            "directConnectGatewayName": "apollan",
            "directConnectGatewayIp": "10.212.253.59",
            "snatNum": 1,
            "dnatNum": 0,
            "snaptNum": 0,
            "dnaptNum": 0,
            "createTime": "2016-06-29 19:20:45",
            "vpcCidrBlock": "172.17.0.0/16",
            "unVpcId": "vpc-kx49lmyv",
            "type": 1
        }
    ]
}
```


