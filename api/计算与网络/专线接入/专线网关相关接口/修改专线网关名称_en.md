## 1. API Description
 
Domain:  vpc.api.qcloud.com
API name:  ModifyDirectConnectGateway

This API is used to modify the Direct Connect gateway name.

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> vpcId <td> Yes <td> String <td> Virtual private cloud ID, which can be vpcId or unVpcId. unVpcId is recommended. Can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>
<tr>
<td> directConnectGatewayId <td> Yes <td> String <td> Direct Connect gateway ID. Can be queried via the API <a href="http://www.qcloud.com/doc/api/259/%E6%9F%A5%E8%AF%A2%E4%B8%93%E7%BA%BF%E7%BD%91%E5%85%B3%E5%88%97%E8%A1%A8" title="DescribeDirectConnectGateway">DescribeDirectConnectGateway</a>
<tr>
<td> directConnectGatewayName <td> Yes <td> String <td> Modified Direct Connect gateway name
</tbody></table>

 

## 3. Output Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code <td> Int <td> Error code, 0:  Succeeded, other values:  Failed
<tr>
<td> message <td> String <td> Error message
<tr>
<td> data <td> Array <td> Returned array
</tbody></table>

 

## 4. Example
 
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=ModifyDirectConnectGateway</nowiki>
  &vpcId=vpc-cor5n2a5
  &directConnectGatewayId=dcg-o5g3urc1
  &directConnectGatewayName=Direct Connect gateway test
  &<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "data": []
}

```


