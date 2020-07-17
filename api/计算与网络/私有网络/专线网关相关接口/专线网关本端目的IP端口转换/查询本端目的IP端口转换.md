## 1. 接口描述

本接口（DescribeLocalDestinationIPPortTranslationNatRule）用于查询专线网关本端目的 IP 端口转换规则。
接口请求域名：vpc.api.qcloud.com

本接口用于查询指定专线网关的本端目的 IP 端口转换规则

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见<a href="https://cloud.tencent.com/document/product/215/4772" title="公共请求参数"> 公共请求参数 </a>页面。其中，此接口的 Action 字段为 DescribeLocalDestinationIPPortTranslationNatRule。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 系统分配的私有网络 ID，例如 vpc-dfg5445。 |
| directConnectGatewayId | 是 | String | 系统分配的专线网关 ID，例如 dcg-4d545d。 |
| originalIP | 否 | String | 原始 IP。 |
| originalPort | 否 | String | 原始 Port。 |
| translationIP | 否 | String | 转换后 IP。 |
| translationPort | 否 | String |转换后 Port。 |
| proto | 否 | String | 协议。 |
| description | 否 | String | 备注，支持模糊搜索。|
| offset | 否 | Int | 初始行的偏移量，默认为0。 |
| limit | 否 | Int | 每页行数，默认为20。 |

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/document/product/215/4781#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码"> 公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| data.n | Array | 本端 IP 转换规则信息组。|
| data.n.originalIP | String | 原始 IP。 |
| data.n.originalPort | String | 原始 Port。 |
| data.n.translationIP | String | 转换后 IP。|
| data.n.translationPort | String | 转换后 Port。|
| data.n.proto | String | 协议。|
| data.n.description | String | 备注。|

 ## 4. 错误码表
  以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码"> VPC 错误码</a>。
 
| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的 VPC，VPC 资源不存在。请再次核实您输入的资源信息是否正确。可调用<a href="https://cloud.tencent.com/doc/api/245/%e5%88%9b%e5%bb%ba%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c" title="查询私有网络列表"> 查询私有网络列表</a>（DescribeVpcEx）接口查询。|
| InvalidDirectConnectGateway.NotFound | 无效的专线网关，专线网关资源不存在。请再次核实您输入的资源信息是否正确。可调用<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3" title="查询专线网关"> 查询专线网关</a>（DescribeDirectConnectGateway）接口查询。|
| InvalidLocalDestinationIPPortTranslation.NotFound | 要修改的本端目的 IP 端口转换不存在，请再次核实您输入的资源信息是否正确。可调用<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3%e6%9c%ac%e7%ab%af%e7%9b%ae%e7%9a%84IP%e7%ab%af%e5%8f%a3%e8%bd%ac%e6%8d%a2" title="查询专线网关本端目的IP端口转换"> 查询专线网关本端目的 IP 端口转换</a>（DescribeLocalDestinationIPPortTranslationNatRule）接口查询。|

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeLocalDestinationIPPortTranslationNatRule
&<公共请求参数>
&vpcId=vpc-dfgg190
&directConnectGatewayId=dcg-ddf14d
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "data": [
        {
            "originalIP": "10.0.0.1",
            "originalPort": "80-90",
            "translationIP": "138.0.0.1",
            "translationPort": "800-820",
            "proto": "tcp",
            "description": "备注1"
        }
    ]
}
```

