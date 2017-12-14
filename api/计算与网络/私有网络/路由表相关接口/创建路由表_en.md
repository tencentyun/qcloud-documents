## 1. API Description

This API (CreateRouteTable) is used to create routing table. 
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font> 

When VPC has been created, the system will create a default routing table with which all new subnets will be associated. By default, you can use the default routing table to manage your routing policies.  It you have many routing policies, you can call the API for creating routing table to create more routing tables to manage your routing policies. 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>.  The Action field for this API is CreateRouteTable. 


| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | ID of VPC to which the subnet belongs. It can be vpcId or unVpcId. unVpcId is recommended. For example, vpc-rqndayhs. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| routeTableName | Yes|  String| Routing table name. You can specify any name you like, but its length should be limited to 60 characters.   |
| routeSet.n | No | array | (Optional) Content of routing table.|
| routeSet.n.destinationCidrBlock | Yes | String | Destination network segment, which cannot be within the VPC network segment. For example: 112.20.51.0/24. |
| routeSet.n.nextType | Yes | String | Type of next hop. Supported types: 0: public network gateway; 1: VPN gateway; 3: Direct Connect gateway; 4: peering connection; 7: sslvpn; 8: NAT gateway; 9: general cvm . |
| routeSet.n.nextHub | Yes | String | Next hop address. You just need to specify gateway IDs (new ID is recommended) of different next hop types and the system will automatically match to the next hop address.  |
| routeSet.n.description | No | String | Route description, which should be limited to 60 characters.   |

 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:   Succeeded, other values:   Failed.   |
| message | String | Error message.   |
| routeTableId | String | Routing table ID, for example: gz_rtb_4545.   |
| unRouteTableId | String | Unified ID of routing table. It is recommended to use a unified ID to identify the routing table, for example, rtb-rqndayhs.   |
| routeTableSet.n | Array  | Content of routing table.  |
| routeTableSet.n.destinationCidrBlock | String  | Destination network segment, which cannot be within the VPC network segment. For example: 112.20.51.0/24.   |
| routeTableSet.n.nextType | String  | Type of next hop. Supported types: 0: public network gateway; 1: VPN gateway; 3: Direct Connect gateway; 4: peering connection; 7: sslvpn; 8: nat gateway; 9: general cvm .  |
| routeTableSet.n.nextHub | String  | Next hop address. You just need to specify the gateway ID (new ID is recommended) of a different next hop type and the system will automatically match to the next hop address.  |
| routeTableSet.n.description | String  | Route description.   |

## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>. 

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC.  VPC resource does not exist. Please verify that you have entered resource information correctly. You can query VPC through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| InvalidRouteTableName | Invalid routing table name.  You can specify any name you like, but its length should be limited to 60 characters.   |
| InvalidDestinationCidr | Invalid destination network segment.   |
| RouteTableLimitExceeded | Number of routing tables allowed to be created has been exceeded.  Please contact customer service for more resources.  For more information on VPC resource restrictions, refer to <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Usage Restrictions">VPC Usage Restrictions</a>.   |
| RouteLimitExceeded | The upper limit of number of routing table policies has been exceeded.  Please contact customer service for more resources. For more information on VPC resource restrictions, refer to <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Usage Restrictions">VPC Usage Restrictions</a>.  |
| RouteAlreadyExists | The destination network segment already exists in the routing table policy.  No conflict between destination network segments is allowed in the same routing table.  |
| InvalidRouteNextType | Invalid next hop type.  For supported types, refer to the descriptions of input parameters.  |
| InvalidRouteNextHub.NotFound | The next hop address does not exist.  Please verify that you have entered next hop address resource ID correctly.  |
 

## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=CreateRouteTable
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-amhnnao5
  &routeTableName=tttt111
  &routeSet.0.destinationCidrBlock=121.0.23.51/16
  &routeSet.0.nextType=1
  &routeSet.0.nextHub=vpngw-dystbrkv

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "routeTableId": "gz_rtb_8755",
    "unRouteTableId": "rtb-rqndayhs",
    "routeTableSet": [
        {
            "destinationCidrBlock": "121.0.23.51\/16",
            "nextType": 1,
            "nextHub": "vpngw-dystbrkv"
        }
    ]
}

```


