## 1. API Description

This API (DeleteRoute) is used to delete routing policies. 
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font> 

You can delete routing policies in batch for a routing table. 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>.  The Action field for this API is DeleteRoute. 


| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | ID of VPC to which the subnet belongs. It can be vpcId or unVpcId. unVpcId is recommended. For example, vpc-rqndayhs.  It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| routeTableId | Yes | String | The routing table ID assigned by the system, which can be routeTableId or unRouteTableId. unRouteTableId is recommended. For example: rtb-rqndayhs.  It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8" title="DescribeRouteTable">DescribeRouteTable</a>.  |
| routeSet.n | Yes | array | Content of routing table. This is optional. |
| routeSet.n.destinationCidrBlock | Yes | String | Destination network segment, which cannot be within the VPC network segment. For example: 112.20.51.0/24.  |
| routeSet.n.nextType | Yes | String | Type of next hop. Supported types: 0: public network gateway; 1: VPN gateway; 3: Direct Connect gateway; 4: peering connection; 7: sslvpn gateway; 8: NAT gateway; 9: general cvm . |
| routeSet.n.nextHub | Yes | String | Next hop address. You just need to specify gateway IDs (new ID is recommended) of different next hop types and the system will automatically match to the next hop address.  |

 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:   Succeeded, other values:   Failed.   |
| message | String | Error message.   |

## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>. 

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | VPC not exist. Please check the information you entered. You can query VPC through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| InvalidRouteTableId.NotFound | Routing table ID not exist. Please check the information you entered. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8" title="DescribeRouteTable">DescribeRouteTable</a>.  | 
| InvalidDestinationCidr | Invalid destination IP address range.   |
| InvalidRouteNextType | Invalid next hop type. For supported types, refer to the descriptions of input parameters.  |
| InvalidRouteNextHub.NotFound | The next hop address does not exist.  Please check the information you entered.  |
 

## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DeleteRoute
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-amhnnao5
  &routeTableId=rtb-4ahe1qy2
  &routeSet.0.destinationCidrBlock=121.0.23.51/16
  &routeSet.0.nextType=1
  &routeSet.0.nextHub=vpngw-dystbrkv

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```


