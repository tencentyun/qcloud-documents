## 1. API Description
 
Domain name: eip.api.qcloud.com
API name: EipUnBindInstance

Unbind the binding between EIP and server.
>Note:
The platform imposes a quota on the number of attempts to unbind an EIP and reallocate an ordinary public IP per day for each region (refer to <a href="/doc/product/213/1941" title="/doc/product/213/1941">Overview of EIP Products</a>). The above quota can be obtained through <a href="http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E9%85%8D%E9%A2%9D" title="DescribeEipQuota">DescribeEipQuota</a> API.

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> eipId <td> No <td> String <td> Instance ID of EIP, which can be obtained from eipId in the returned field of <a href="http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E5%88%97%E8%A1%A8" title="DescribeEipQuota">DescribeEip</a> API
<tr>
<td> allocWanIp <td> No <td> Int <td> Whether to a reallocate a new ordinary public IP for the primary IP of the server's primary ENI after the EIP is unbound from the server. The ordinary public IP will be released upon the release of the server and is not elastic. <br>0: Do not allocate; 1: Allocate (The default is 0).
<tr>
<td> networkInterfaceId <td> No <td> String <td> The unique ID of ENI, which can be obtained from networkInterfaceId in the returned field of <a href="/doc/api/245/4814" title="DescribeNetworkInterfaces">DescribeNetworkInterfaces</a> API
<tr>
<td> privateIpAddress <td> No <td> String <td> Private IP of the server. Either the parameter eipId, or the parameters networkInterfaceId and privateIpAddress are passed during the unbinding.
<tr>
<td> unBindPrivateIpWithEip <td> No <td> Int <td> Whether to unbind the binding between networkInterfaceId/privateIpAddress and EIP after the EIP is unbound from the server. This parameter applies only when the primary IP of non-primary ENI is unbound for a server supporting ENI. In other cases, unbinding is performed by default. <br>0: Do not unbind; 1: Unbind (The default is 1).
</tbody></table>

 

## 3. Output Parameters
 

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |


 

## 4. Example
 
Input
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &eipId=eip-mksy14ay
  &allocWanIp=0

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```

