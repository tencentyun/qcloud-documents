## 1. 接口描述

本接口(EipBindNatGateway)用于NAT网关绑定EIP
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为EipBindNatGateway。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| natId | 是 | string | 高可用网关统一ID，例如：nat-df5dfd |
| vpcId | 是 | string | 私有网络ID或统一ID，建议使用统一ID，例如：vpc-dfd5dfgd |
| assignedEipSet.n | 否 | array | 弹性IP。assignedEipSet 和 autoAllocEipNum 这两个入参需至少传一个，例如：assignedEipSet.0=183.23.0.0.1 |
| autoAllocEipNum | 否 | int | 需要新申请的弹性IP个数, 取值范围[0, 3]。assignedEipSet 和 autoAllocEipNum 这两个入参需至少传一个|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0: 成功, 其他值: 失败|
| message | String | 错误信息|
| taskId | Int | 任务ID，操作结果可以用taskId查询，详见<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">查询任务执行结果接口</a>。 |

 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC，VPC资源不存在。请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询VPC |
| InvalidNatGatewayId.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2NAT%e7%bd%91%e5%85%b3?viewType=preview" title="DescribeNatGateway">DescribeNatGateway</a>接口查询NAT网关 |

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=EipBindNatGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&natId=nat-8pbrkzh6
&vpcId=314
&autoAllocEipNum=1
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "taskId":16167
}
```

