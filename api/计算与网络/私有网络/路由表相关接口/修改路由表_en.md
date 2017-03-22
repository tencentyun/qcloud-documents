## 1. API Description

This API (ModifyRouteTableAttribute) is used to modify the attributes of routing table. 
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font> 

After the modification, the original content of routing table will be totally replaced with the newly submitted content.  If you need to add new routing policies, the new routing policies should be submitted together with the original content of routing table.

## 2. Input Parameters
 
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>.  The Action field for this API is ModifyRouteTableAttribute. 

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | ID of VPC to which the subnet belongs. It can be vpcId or unVpcId. unVpcId is recommended. For example, vpc-rqndayhs. It can be queried through API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| routeTableId | Yes | String | The routing table ID assigned by the system, which can be routeTableId or unRouteTableId. unRouteTableId is recommended. For example: rtb-rqndayhs. It can be queried through API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8" title="DescribeRouteTable">DescribeRouteTable</a>.  |
| routeTableName | No|  String| Routing table name; you can specify any name you like, but its length should be limited to 60 characters. The name must be unique within the same VPC.  |
| routeSet.n | No | array | Content of routing table. This is optional. |
| routeSet.n.destinationCidrBlock | Yes | String | Destination network segment, which cannot be within the VPC network segment. For example: 112.20.51.0/24. |
| routeSet.n.nextType | Yes | String | Type of next hop. Supported types: 0: public network gateway; 1: VPN gateway; 3: Direct Connect gateway; 4: peering connection; 7: sslvpn; 8: nat gateway. |
| routeSet.n.nextHub | Yes | String | Next hop address. You just need to specify gateway IDs (new ID is recommended) of different next hop types and the system will automatically match to the next hop address.  |
| routeSet.n.description | No | String | Route description, which should be limited to 60 characters.  |
  
## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:   Succeeded, other values:   Failed.   |
| message | String | Error message.   |


 ## 4. Error Code List
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://www.qcloud.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC.  VPC resource does not exist. Please verify that you have entered resource information correctly. You can query VPC through API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| InvalidRouteTableId.NotFound | Invalid routing table. The routing table ID does not exist. Please verify that you have entered resource information correctly. It can be queried through API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8" title="DescribeRouteTable">DescribeRouteTable</a>.  | 
| InvalidRouteTableName | Invalid routing table name. You can specify any name you like, but its length should be limited to 60 characters.  |
| InvalidRouteTableName.InUse | The routing table name has been used by another routing table under the VPC. The routing table name must be unique within the same VPC.  |
| RouteLimitExceeded | The upper limit of number of routing table policies has been exceeded. Please contact customer service for more resources. For more information on VPC resource restrictions, refer to <a href="https://www.qcloud.com/doc/product/215/537" title="VPC Usage Restrictions">VPC Usage Restrictions</a>.  |
| RouteAlreadyExists | The destination network segment already exists in the routing table policy. No conflict between destination network segments is allowed in the same routing table.  |
| InvalidRouteNextType | Invalid next hop type. For supported types, refer to the descriptions of input parameters.  |
| InvalidRouteNextHub.NotFound | The next hop address does not exist. Please verify that you have entered next hop address resource ID correctly.  |
| InvalidRoute.NextHubLimitExceeded | The maximum number of paths in public network gateway ECMP is 8.   |  
## 5. Example
 
Input
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=ModifyRouteTableAttribute
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-amhnnao5
  &routeTableId=rtb-8oidkjt2
  &routeSet.0.destinationCidrBlock=121.0.23.51/18
  &routeSet.0.nextType=1
  &routeSet.0.nextHub=vpngw-dystbrkv
  &routeTableName=tttt111

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```


