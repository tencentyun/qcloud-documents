## 1. API Description
This API (CreateNatGateway) is used to create an NAT gateway.
Domain for API request: vpc.api.qcloud.com

Before using this API, go to <a href="https://cloud.tencent.com/doc/product/215/1682" title="Gateway Description" >NAT Gateway Description</a> to learn the features of NAT gateway.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| natName | Yes | string | NAT gateway name; supports 1-25 characters, including uppercase and lowercase English letters, numbers, and underscores.  |
| vpcId | Yes | string | Virtual private cloud ID or unified ID (unified ID is recommended). It can be queried via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API.  |
| maxConcurrent | Yes | int | The upper limit of concurrent connection of NAT gateway, for example: 1000000, 3000000, 10000000. To learn more, please refer to <a href="https://cloud.tencent.com/doc/product/215/1682" title="Gateway Description" >Virtual Private Cloud Gateway Description</a>.  |
| bandwidth | No | int | The maximum public network output bandwidth of the gateway (unit: Mbps),  which is 100 Mbps by default. For more information, please refer to <a href="https://cloud.tencent.com/doc/product/215/1682" title="Gateway Description" >Virtual Private Cloud Gateway Description</a>.  |
| assignedEipSet.n | No | string | One of the two elastic IP arrays bound to the gateway, `assignedEipSet` and `autoAllocEipNum`, must be passed at least, for example: `assignedEipSet.0=10.0.0.1`. For more information on elastic IP, please refer to <a href="https://intl.cloud.tencent.com/document/product/213/5733" title="">Elastic IP</a>. |
| autoAllocEipNum | No | int | The number of elastic IPs for new requests. The system will generate several elastic IPs according to your needs. One of the assignedEipSet and autoAllocEipNum must be passed at least. For more information on elastic IP, please refer to <a href="https://intl.cloud.tencent.com/document/product/213/5733" title="">Elastic IP</a>.  |



## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed |
| message | string | Error message |
| billId | string | Order ID. You can query the creation result by calling <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2NAT%e7%bd%91%e5%85%b3%e7%9a%84%e7%94%9f%e4%ba%a7%e7%8a%b6%e6%80%81?viewType=preview" title="Query Creation Status of NAT Gateway">QueryNatGatewayProductionStatus</a> API.|

## 4. Error Codes
The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | This VPC does not exist. Please check the information entered. You can query the VPC via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API. |
| InvalidNatGatewayName | The NAT gateway name is invalid. It should contain 1-60 characters, including uppercase and lowercase letters, numbers, and underscores |
| NatGatewayLimitExceeded | Reached the upper limit of NAT gateways. Please contact customer service to raise the quota. For more information on VPC resource restrictions, see <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Service Limits">VPC Service Limits</a> |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateNatGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&natName=zhezhe
&vpcId=314
&maxConcurrent=1000000
&bandwidth=10
&autoAllocEipNum=1
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "billId":"20160415160000002485253313199244"
}
```


