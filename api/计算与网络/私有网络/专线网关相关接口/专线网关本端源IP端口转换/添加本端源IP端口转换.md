## 1. 接口描述
本接口（CreateLocalSourceIPPortTranslationNatRule）用于添加专线网关本端源 IP 端口转换。
接口请求域名：vpc.api.qcloud.com 

1) 私有网络内源 IP 端口映射为指定 IP 池内随机 IP 的随机端口主动访问，只有 NAT 类型的专线网关支持。
2) 转换后 IP 池内 IP 不能在 VPC 网段内，IP 池支持单个 IP、IP 段(例如183.63.0.1 - 183.63.0.10)和 CIDR 格式。


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见<a href='https://cloud.tencent.com/document/product/215/4772' title='公共请求参数'> 公共请求参数 </a>页面。其中，此接口的 Action 字段为 CreateLocalSourceIPPortTranslationNatRule。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 系统分配的私有网络 ID，支持升级前的 vpcId，也支持升级后的 unVpcId，例如 vpc-dgd45。 |
| directConnectGatewayId | 是 | String | 系统分配的专线网关 ID，例如 dcg-dgd454d。 |
| localSourceIPPortTranslation.n  | 是 | Array | 本端源地址转换数组。 |
| localSourceIPPortTranslation.n.translationIPPool  | 是 | String | 转换后 IP 池。 |
| localSourceIPPortTranslation.n.description  | 否 | String | 备注信息。 |


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/document/product/215/4781#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'> 公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| data | Array | 返回的数据。 |
| data.taskId | Int  | 任务 ID。操作结果可以用 taskId 查询，详见<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3"> 查询任务执行结果接口</a>。 |
| codeDesc | String | 错误码。 |

 ## 4. 错误码表
  以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码"> VPC 错误码</a>。
	
| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的 VPC。VPC 资源不存在，请再次核实您输入的资源信息是否正确。可调用<a href="https://cloud.tencent.com/doc/api/245/%e5%88%9b%e5%bb%ba%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c?viewType=preview" title="查询私有网络列表"> 查询私有网络列表</a>（DescribeVpcEx）接口查询。|
| InvalidDirectConnectGateway.NotFound | 无效的专线网关。专线网关资源不存在，请再次核实您输入的资源信息是否正确。可调用<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3?viewType=preview" title="查询专线网关"> 查询专线网关</a>（DescribeDirectConnectGateway）接口查询。|
| InvalidTranslationIPPool.NotInVpcCidr | 无效的转换后 IP 池。转换后 IP 池不在 VPC 网段内。|
| InvalidTranslationIP.Duplicate | 无效的转换后 IP 池。转换后 IP 池重复，转换后 IP 池已经在该网关的本端源 IP 端口转换规则中，转换后 IP 池不可重复。|
| LocalSourceIPPortTranslationLimitExceeded | 您添加的本端源IP端口转换规则已达上限。如果需要更多资源，请联系客服申请。更多 VPC 资源限制信息详见<a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制"> VPC 使用限制</a>。|

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateLocalSourceIPPortTranslationNatRule
&vpcId=vpc-csnmo39l
&directConnectGatewayId=dcg-mm01ughx
&localSourceIPPortTranslation.0.translationIPPool=183.12.63.0-183.12.63.20
&localSourceIPPortTranslation.0.description=barttest
&公共请求参数
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "data":{
        "taskId":"17922"
    },
    "codeDesc":"Success"
}
```

