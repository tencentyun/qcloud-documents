## 1. 接口描述

本接口(ModifyNatGateway)用于修改NAT网关
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为ModifyNatGateway。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | string | 私有网络ID或者统一ID，建议使用统一ID，例如：vpc-x7d44d。|
| natId | 是 | string | NAT网关统一ID,例如：nat-df45454。|
| natName | 否 | string | NAT网关名称，取值：1-25个中文、英文大小写的字母、数字和下划线分隔符。 |
| bandwidth | 否 | int | 网关最大外网出带宽(单位:Mbps), 默认: 100Mbps, 具体支持数据请参见<a href="https://cloud.tencent.com/doc/product/215/1682" title="网关说明" >私有网络网关说明</a>。 |


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0: 成功, 其他值: 失败|
| message | String | 错误信息|

 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC，VPC资源不存在。请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询VPC |
| InvalidNatGatewayId.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2NAT%e7%bd%91%e5%85%b3?viewType=preview" title="DescribeNatGateway">DescribeNatGateway</a>接口查询NAT网关 |
| InvalidNatGatewayName | NAT网关名称不合法。NAT网关名称取值范围：1-60个中文、英文大小写的字母、数字和下划线分隔符 |

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=ModifyNatGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&natId=nat-jngbqyfs
&vpcId=314
&natName=cici
</pre>
输出
```
{
    "code":"0",
    "message":""
}
```

