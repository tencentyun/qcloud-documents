## 1. 接口描述

本接口(DescribeLocalIPTranslationAclRule)用于查询本端IP转换 ACL策略。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeLocalIPTranslationAclRule。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 系统分配的私有网络ID，例如：vpc-dfg5445。 |
| directConnectGatewayId | 是 | String | 系统分配的专线网关ID，例如：dcg-4d545d。 |
| originalIP | 是 | String | 原始IP。 |
| translationIP | 是 | String | 转换后IP。 |
| aclRules.n | 否 | Array | ACL策略ID数组，例如：aclRules.0=25。 |

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| data.n | Array | acl策略信息数组。 |
| data.n.aclRuleId | Int | ACL规则ID，例如：25。 |
| data.n.protocol | String | 协议，例如TCP。 |
| data.n.sourcePort | String | 访问的源端口，例如：900。 |
| data.n.destinationCidr | String | 访问的目的IP，例如：10.0.0.2/16。 |
| data.n.destinationPort | String | 访问的目的端口，例如：80-90。|

 ## 4. 错误码表
  以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确。可调用<a href="https://cloud.tencent.com/doc/api/245/%e5%88%9b%e5%bb%ba%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c?viewType=preview" title="查询私有网络列表">查询私有网络列表</a>(DescribeVpcEx)接口查询。|
| InvalidDirectConnectGateway.NotFound | 无效的专线网关。专线网关资源不存在，请再次核实您输入的资源信息是否正确。可调用<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3?viewType=preview" title="查询专线网关">查询专线网关</a>(DescribeDirectConnectGateway)接口查询。|
| InvalidLocalIPTranslation.NotFound | 无效的本端IP转换规则。本端IP转换规则不存在，请再次核实您输入的资源信息是否正确。|

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeLocalIPTranslationAclRule
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&vpcId=vpc-dfgg190
&directConnectGatewayId=dcg-ddf14d
&originalIP=10.0.0.5
&translationIP=138.0.0.11
</pre>
输出
```
{
    "code":"0",
    "message":""，
    "data":[
				{
							"aclRuleId":67,
							"protocol":"TCP",
							"sourcePort":"80",
							"destinationCidr":"10.0.0.2/18",
							"destinationPort":"90"
				}
		]
}
```

