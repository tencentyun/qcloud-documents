## 1. 接口描述
本接口(CreatePeerIPTranslationNatRule)用于添加专线网关对端IP转换。
接口请求域名：<font style='color:red'>vpc.api.qcloud.com </font>

1) 专线对端原始IP映射为新 IP，并以新IP 与连接的私有网络进行网络互访，只能NAT类型网关才支持。
2) 转换后IP不能在VPC网段内。
3) 同一个NAT网关下的对端IP转换规则原始IP不能重复，转换后IP也不能重复。


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='/doc/api/372/4153' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为CreatePeerIPTranslationNatRule。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 私用网络ID或者统一ID，建议使用统一ID。|
| directConnectGatewayId | 是 | String | 专线网关ID。|
| peerIPTranslation.n | 是 | Array | 对端IP转换规则数组。 |
| peerIPTranslation.n.originalIP | 是 | String | 原始IP。 |
| peerIPTranslation.n.translationIP | 是 | String | 转换后IP。 |
| peerIPTranslation.n.description | 否 | String | 备注。 |


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| codeDesc | String | 错误码。 |
| data | Array | 返回信息。 |

 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
	
| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC，VPC资源不存在。请再次核实您输入的资源信息是否正确。可调用<a href="https://cloud.tencent.com/doc/api/245/%e5%88%9b%e5%bb%ba%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c?viewType=preview" title="查询私有网络列表">查询私有网络列表</a>(DescribeVpcEx)接口查询。|
| InvalidDirectConnectGateway.NotFound | 无效的专线网关，专线网关资源不存在。请再次核实您输入的资源信息是否正确。可调用<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3?viewType=preview" title="查询专线网关">查询专线网关</a>(DescribeDirectConnectGateway)接口查询。|
| InvalidOriginalIP.Duplicate | 无效的原始IP，原始IP重复。原始IP已经在该网关的本端IP专线规则中，原始IP不可重复。|
| InvalidTranslationIP.InVpcCidr | 无效的转换后IP，转换后IP在VPC网段内。|
| InvalidTranslationIP.Duplicate | 无效的转换后IP，转换后IP重复。转换后IP已经在该网关的本端IP专线规则中，转换后IP不可重复。|
| PeerIPTranslationLimitExceeded | 您添加的对端IP转换转换规则已达上限，如果需要更多资源，请联系客服申请。更多VPC资源限制信息详见<a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a>。|

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreatePeerIPTranslationNatRule
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&vpcId=vpc-csnmo39l
&directConnectGatewayId=dcg-mm01ughx
&peerIPTranslation.0.originalIP=10.100.10.3
&peerIPTranslation.0.translationIP=183.0.0.1
&peerIPTranslation.0.description=183.0.0.1
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[
        
    ]
}
```

