## 1. API Description
 
Domain:  vpc.api.qcloud.com
API name:  CreateDirectConnectGateway

This API is used to create a Direct Connect gateway.

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> vpcId <td> Yes <td> String <td> Virtual private cloud ID, which can be vpcId or unVpcId. unVpcId is recommended. Can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>
<tr>
<td> directConnectGatewayName <td> Yes <td> String <td> Direct Connect gateway name
<tr>
<td> natType <td> No <td> String <td> NAT type
</tbody></table>

 

## 3. Output Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code <td> Int <td> Error code, 0: Succeeded; other values: Failed
<tr>
<td> message <td> String <td> Error message
</tbody></table>

 

## 4. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=CreateDirectConnectGateway
  &vpcId=vpc-lzwkkgyz
  &directConnectGatewayName=barrytest
  &<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>

</pre>

Output
```
{
    "code": 0,
    "message": ""
}

```


