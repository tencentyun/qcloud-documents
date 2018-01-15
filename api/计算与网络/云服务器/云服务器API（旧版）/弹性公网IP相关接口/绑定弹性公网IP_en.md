## 1. API Description
 
Domain name: eip.api.qcloud.com
API name: EipBindInstance

This API is used to bind an elastic public IP (EIP) to a CVM or an ENI.

>Note:
If the taget CVM is bound with a non-elastic public IP, it will be unbound and released automatically. Then the specified EIP will be bound to the CVM.

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> eipId <td> Yes <td> String <td> Instance ID of EIP, which can be obtained from eipId in the returned field of <a href="http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E5%88%97%E8%A1%A8" title="DescribeEip">DescribeEip</a> API
<tr>
<td> unInstanceId <td> No <td> String <td> Instance ID of the server to be operated, which can be obtained from unInstanceId in the returned field of <a href="http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeInstances">DescribeInstances</a> API. Passing the parameter unInstanceId indicates that the EIP is bound to the primary IP of primary ENI on the server.
<tr>
<td> networkInterfaceId <td> No <td> String <td> The unique ID of ENI, which can be obtained from networkInterfaceId in the returned field of <a href="/doc/api/245/4814" title="DescribeNetworkInterfaces">DescribeNetworkInterfaces</a> API
<tr>
<td> privateIpAddress <td> No <td> String <td> Private IP of the server. During the binding, either the parameter "unInstanceId", or the parameters "networkInterfaceId" and "privateIpAddress" are passed. If "networkInterfaceId" and "privateIpAddress" are not bound to the server, the binding operation will maintain the relationship between them and the EIP.
</tbody></table>

 

## 3. Output Parameters
 

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values​ indicate failure. For more information, please refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, please refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |


 

## 4. Examples
 
Input
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &eipId=eip-mksy14ay
  &unInstanceId=ins-hyvbipjg

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```

