## 1. 接口描述
本接口(CreateBmNatGateway)用于创建黑石NAT网关
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为CreateBmNatGateway。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| natName | 是 | string | NAT网关名称，支持1-25个中文、英文大小写的字母、数字和下划线分隔符。 |
| vpcId | 是 | string | 私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-kd7d06of，可通过<a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。 |
| maxConcurrent | 是 | int | 网关并发连接上限，例如：1000000、3000000、10000000。 |
| assignedEipSet.n | 否 | Array | 绑定网关的弹性IP数组, assignedEipSet和autoAllocEipNum至少传一个，例如：assignedEipSet.0=10.0.0.1 ，更多关于弹性IP的信息请参考弹性IP。|
| subnetIds.n | 否 | Array | 绑定网关的子网唯一ID数组, 例如：subnet-k20jbhp0。可通过<a href="https://www.qcloud.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。|
| subnetAll | 否 | int | 是否包含vpc下的所有子网包括后续新建子网。subnetAll为0时必须传入subnetIds子网信息|
| autoAllocEipNum | 否 | int | 需要新申请的弹性IP个数，系统会按您的要求生产N个弹性IP, assignedEipSet和autoAllocEipNum至少传一个，更多关于弹性IP的信息请参考弹性IP。 |



## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | int | 错误码。0：成功, 其他值：失败|
| message | string | 错误信息|
| data | Array | 返回操作的任务ID，创建结果可调用<a href="" title="查询NAT网关的生产状态">查询NAT网关的生产状态</a>查询 |

 ## 4. 错误码表
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://www.qcloud.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| -3030 | InvalidBmSubnet.NotFound | 无效的子网。子网资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://www.qcloud.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。 |
| 13006 | InvalidBmVpc.NatGatewayLimitExceeded |创建的 NAT 网关数量超过上限。如果需要更多资源，请联系客服申请。每个vpc最多允许创建5个NAT网关 |
| 13010 | BmVpcNat.InvalidEip | 绑定NAT网关的弹性IP不存在。 |
| 13011 | BmVpcNat.InvalidEipVpcId | 弹性IP所属VPC与NAT网关不一致。 |
| 13012 | BmVpcNat.SubnetUsed | 子网已被绑定到其他NAT网关。 |
| 13013 | BmVpcNat.EipUsed | 绑定NAT网关的弹性IP已被使用。 |
| 13015 | BmVpcNat.EipLimitExceeded | 绑定NAT网关的弹性IP达到上限。 |
## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateBmNatGateway
&<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
&natName=zhezhe
&vpcId=vpc-kd7d06of
&maxConcurrent=1000000
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

