## 1. API Description
 
Domain name: eip.api.qcloud.com
API name: ModifyEipAttributes

This API is used to modify the name of elastic public IP (EIP).

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> eipId <td> Yes <td> String <td> Instance ID of EIP, which can be obtained from eipId in the returned field of <a href="http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E5%88%97%E8%A1%A8" title="DescribeEip">DescribeEip</a> API
<tr>
<td> eipName <td> Yes <td> String <td> Alias of EIP instance 
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
  &eipId=eip-p2x6wxc0
  &eipName=test1111

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```

