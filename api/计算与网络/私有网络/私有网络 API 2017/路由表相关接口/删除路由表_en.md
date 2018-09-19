## 1. API Description

This API (DeleteRouteTable) is used to delete routing table. 
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font> 
 

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>.  The Action field for this API is DeleteRouteTable. 

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | ID of VPC to which the subnet belongs. It can be vpcId or unVpcId. unVpcId is recommended. For example, vpc-rqndayhs.  It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| routeTableId | Yes | String | The routing table ID assigned by the system, which can be routeTableId or unRouteTableId. unRouteTableId is recommended. For example, rtb-rqndayhs. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8" title="DescribeRouteTable">DescribeRouteTable</a>.  |

 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed.   |
| message |  String | Error message.   |

## 4. Error Codes
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>. 
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | VPC not exist. Please check the information you entered. You can query VPC through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  | 
| InvalidRouteTableId.NotFound | Routing table ID not exist. Please check the information you entered. It can be queried through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8" title="DescribeRouteTable">DescribeRouteTable</a>.  | 

## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DeleteRouteTable
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-amhnnao5
  &routeTableId=rtb-4ahe1qy2
</pre>

Output
```
{
    "code": 0,
    "message": ""
}

```


