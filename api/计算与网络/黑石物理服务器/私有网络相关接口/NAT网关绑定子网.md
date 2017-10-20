## 功能描述
SubnetBindBmNatGateway 接口用于将全部IP的子网类型绑定到NAT网关

接口请求域名：bmvpc.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php?Action=SubnetBindBmNatGateway
    &<公共请求参数>
    &natId=<NAT网关ID>
    &vpcId=<vpc网络ID>
    &subnetIds.0=<子网ID>
    &subnetIds.1=<子网ID>
```
### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/document/product/386/6718" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为SubnetBindBmNatGateway。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| natId | 是 | String | 黑石网关统一ID，例如：nat-df5dfd |
| vpcId | 是 | String | 私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-kd7d06of，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。|
| subnetIds.n | 是 | Array | 需要绑定全部IP的子网唯一ID数组。例如：subnetIds.0=subnet-8pca7qqf。可通过<a href="/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。 |


## 响应
### 响应示例
```
{
	"code": 0,
	"message": "",
	"data": {
		"taskId": <NAT异步任务ID>
	}
}
```
### 响应参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data | Array | 返回操作的任务ID，创建结果可调用<a href="https://cloud.tencent.com/document/api/386/9356" title="查询NAT网关操作状态">查询NAT网关操作状态</a>查询 |


## 错误码
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| 10001 | BmVpc.InvalidParameterValue | 参数设置错误，具体错误信息可查看返回的message信息 |
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| -3030 | InvalidBmSubnet.NotFound | 无效的子网。子网资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。 |
| 13014 | BmVpcNat.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确，可通过DescribeBmNatGateway接口查询NAT网关。 |
| 13012 | BmVpcNat.SubnetUsed | 子网已被绑定到其他NAT网关。 |

## 实际案例
### 请求
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=SubnetBindBmNatGateway
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=4557
	&Timestamp=1507692902
	&Region=gz
	&vpcId=300006
	&natId=nat-et8e970y
	&subnetIds.0=subnet-11111
	&subnetIds.1=subnet-22222
	&Signature=4dq8JXWTyg9n8FuVckaIhg8Pnbw%3D
```

### 响应
```
{
	"code": 0,
	"message": "",
	"data": {
		"taskId": 9641
	}
}
```

