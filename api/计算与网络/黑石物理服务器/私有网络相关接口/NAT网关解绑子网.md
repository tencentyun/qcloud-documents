## 1. 接口描述

本接口(SubnetUnBindBmNatGateway)用黑石于NAT网关解绑子网
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为SubnetUnBindBmNatGateway。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| natId | 是 | String | NAT网关统一ID，例如：nat-8pbrkzh6|
| vpcId | 是 | String | 私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-kd7d06of，可通过<a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。|
| subnetIds.n | 是 | array | 子网唯一ID。例如：subnetIds.0=subnet-8pca7qqf。可通过<a href="https://www.qcloud.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。 |


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | int | 错误码。0：成功，其他值：失败|
| message | string | 错误信息|
| data | Array | 返回操作的任务ID，创建结果可调用<a href="" title="查询黑石NAT网关绑定EIP的任务状态">查询黑石NAT网关绑定EIP的任务状态</a>查询 |

 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://www.qcloud.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| -3030 | InvalidBmSubnet.NotFound | 无效的子网。子网资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://www.qcloud.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。 |
| 13014 | BmVpcNat.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确，可通过DescribeBmNatGateway接口查询NAT网关。 |



## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=SubnetUnBindBmNatGateway
&<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
&natId=nat-8pbrkzh6
&vpcId=vpc-ddf411
&assignedEipSet.0=183.60.249.122
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

