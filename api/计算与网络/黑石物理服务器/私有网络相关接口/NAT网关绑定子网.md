## 1. 接口描述

本接口(SubnetBindBmNatGateway)用于黑石NAT网关绑定子网
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为EipBindNatGateway。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| natId | 是 | string | 黑石网关统一ID，例如：nat-df5dfd |
| vpcId | 是 | string | 私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-kd7d06of，可通过<a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。|
| subnetIds.n | 否 | array | 子网唯一ID。subnetIds 和 subnetAll 这两个入参需至少传一个，例如：subnetIds.0=	subnet-8pca7qqf。可通过<a href="https://www.qcloud.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。 |
| subnetAll | 否 | int | 是否包含所有子网包括后续新建子网，取值为 0 或者 1|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data | Array | 返回操作的任务ID，创建结果可调用<a href="" title="查询黑石NAT网关绑定子网的任务状态">查询黑石NAT网关绑定子网的任务状态</a>查询 |

 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://www.qcloud.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| -3030 | InvalidBmSubnet.NotFound | 无效的子网。子网资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://www.qcloud.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。 |
| 13014 | BmVpcNat.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确，可通过DescribeBmNatGateway接口查询NAT网关。 |
| 13012 | BmVpcNat.SubnetUsed | 子网已被绑定到其他NAT网关。 |

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=SubnetBindBmNatGateway
&<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
&natId=nat-8pbrkzh6
&vpcId=vpc-ddf411
&autoAllocEipNum=1
</pre>
输出
```
{
	"code": 0,
	"message": "",
	"data": {
		"taskId": 9641
	}
}
```

