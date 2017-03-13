## 1. API Description
 
Domain:  vpc.api.qcloud.com
API name:  DescribeDirectConnectGateway

This API is used to query the Direct Connect gateway list.

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> vpcId <td> No <td> String <td>  Virtual private cloud ID, which can be vpcId or unVpcId. unVpcId is recommended. Can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>
<tr>
<td> directConnectGatewayId <td> No <td> String <td> Direct Connect gateway ID
<tr>
<td> directConnectGatewayName <td> No <td> String <td> Direct Connect gateway name
<tr>
<td> offset <td> No <td> Int <td> Offset of initial line. Default is 0
<tr>
<td> limit <td> No <td> Int <td> Number of rows per page. Default is 20
<tr>
<td> orderField <td> No <td> String <td> Sort by a certain field. No sorting by default
<tr>
<td> orderDirection <td> No <td> String <td> Ascending (asc) or descending (desc). Default is asc
</tbody></table>

 

## 3. Output Parameters
| Parameter Name | Type| Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed |
| message |  String | Error message |
|  totalCount |   Int | Return the total number of Direct Connect gateways in the result
| data | array  | Returned array|

Data structure

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>


<tr>
<td> data.vpcId <td> String <td> VPC ID
<tr>
<td> data.unVpcId <td> String <td> VPC unified ID
<tr>
<td> data.vpcName <td> String <td> VPC name
<tr>
<td> data.directConnectGatewayId <td> String <td> Direct Connect gateway ID
<tr>
<td> data.directConnectGatewayName <td> String <td> Direct Connect gateway name
<tr>
<td> data.directConnectGatewayIp <td> String <td> Direct Connect gateway IP
<tr>
<td> data.natType <td> Int <td> Static route type
<tr>
<td> data.createTime <td> String <td> Creation time
<tr>
<td> data.vpcCidrBlock <td> String <td> VPC network segment

</tbody></table>

 

## 4. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeDirectConnectGateway
  &vpcId=180
  &<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>

</pre>

Output
```
{
    "code": 0,
    "message": "",
    "totalCount": 1,
    "data": [
        {
            "vpcId": "gz_vpc_180",
            "vpcName": "test",
            "directConnectGatewayId": "dcg-r40su6xt",
            "directConnectGatewayName": "test-180",
            "directConnectGatewayIp": "10.212.253.59",
            "natType": 1,
            "snatNum": 1,
            "dnatNum": 0,
            "snaptNum": 0,
            "dnaptNum": 0,
            "createTime": "2015-11-03 15:44:21",
            "vpcCidrBlock": "10.100.181.0\/24",
            "unVpcId": "vpc-cor5n2a5"
        }
    ]
}

```


