## 1. 接口描述

本接口(CreateDirectConnectGateway)用于创建专线网关。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

1) 专线网关用于连接私有网络和您的物理专线，更多产品介绍详见<a href="https://cloud.tencent.com/doc/product/216/549" title="专线网关" >专线网关产品说明</a>。
2) 专线网关分NAT和非NAT两种类型，NAT类型支持网络地址转换配置，类型确定后不能修改；一个私有网络可以创建一个NAT类型的专线网关和一个非NAT类型的专线网关。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为CreateDirectConnectGateway。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 私有网络ID，例如：vpc-dgd545 |
| directConnectGatewayName | 是 | String | 专线网关名称，取值：1-25个中文、英文大小写的字母、数字和下划线分隔符 |
| type | 否 | Int  | 专线网关类型；0：非NAT网关；1：NAT网关，默认为非NAT网关 |


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data.directConnectGatewayId | String | 专线网关ID，例如：dcg-mmf0dp2b |

 ## 4. 错误码表
  以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误码 | 描述 |
|---------|---------|
| InvalidDirectConnectGatewayName | 专线网关名称不合法，专线网关名称取值范围：1-60个中文、英文大小写的字母、数字和下划线分隔符。 |
| DirectConnectGatewayLimitExceeded | 您已经达到指定区域专线网关资源申请数量上限，如果需要更多资源，请联系客服申请。更多VPC资源限制信息详见<a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a>。 |
| InvalidVpc.NotFound | 无效的VPC，VPC资源不存在，请再次核实您输入的资源信息是否正确。 |

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateDirectConnectGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&vpcId=vpc-dfgg190
&directConnectGatewayName=专线网关
&type=0
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "data":{
        "directConnectGatewayId":"dcg-mmf0dp2b"
    }
}
```

