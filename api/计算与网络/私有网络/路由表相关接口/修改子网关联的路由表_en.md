## 1. API Description

This API (AssociateRouteTable) is used to modify the routing table associated with the subnet. 
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font> 

A subnet can only be associated with one routing table. 

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>.  The Action field for this API is AssociateRouteTable. 

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | ID of VPC to which the subnet belongs. It can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-amhnnao5. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| subnetId | Yes | String | ID of the subnet to be deleted. Either subnetId or unSubnetId can be used. unSubnetId is recommended. For example, subnet-3x5lf5q0. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8" title="DescribeSubnetEx">DescribeSubnetEx</a>.  |
| routeTableId | Yes | String | The routing table ID assigned by the system, which can be routeTableId or unRouteTableId. unRouteTableId is recommended. For example, rtb-rqndayhs. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8" title="DescribeRouteTable">DescribeRouteTable</a>.  |


 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page.  |
| message | String | Module error message description depending on API.  |

## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>. 

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound |VPC not exist. Please check the information you entered. You can query VPC through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| InvalidSubnet.NotFound |Subnet not exist. Please check the information you entered. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8" title="DescribeSubnetEx">DescribeSubnetEx</a>.  |
| InvalidRouteTableId.NotFound | Routing table ID not exist. Please check the information you entered. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8" title="DescribeRouteTable">DescribeRouteTable</a>.  | 

## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=AssociateRouteTable
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-amhnnao5
  &routeTableId=rtb-rqndayhs
  &subnetId=subnet-3x5lf5q0
</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```


