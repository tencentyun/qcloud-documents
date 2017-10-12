## 功能描述
UnbindIpsToBmNatGateway 用于将子网的部分IP从NAT网关中解绑

接口请求域名：bmvpc.api.qcloud.com

## 请求
语法示例：
```
GET https://vpc.api.qcloud.com/v2/index.php?Action=UnbindIpsToBmNatGateway
    &<公共请求参数>
    &natId=<NAT网关ID>
    &vpcId=<vpc网络ID>
	&ips.0.subnetId=<子网ID>
	&ips.0.ipList.0=<子网内IP>
	&ips.0.ipList.1=<子网内IP>
	&ips.1.subnetId=<子网ID>
	&ips.1.ipList.0=<子网内IP>
```

### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为UnbindIpsToBmNatGateway。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| natId | 是 | string | NAT网关统一ID，例如：nat-8pbrkzh6|
| vpcId | 是 | string | 私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-kd7d06of，可通过<a href="https://cloud.tencent.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。|
| ips.n | 是 | array | 需要解绑部分IP的子网信息数组，ips中的子网标识subnetId不能为已经绑定的全部IP子网。ips包含字段如下：

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|ips.n.subnetId|是|string|子网ID标识|
|ips.n.ipList|是|array|子网下需要解绑NAT的IP列表，IP需要属于该subnetId子网|


## 响应
响应示例：
```
{
	"code": 0,
	"message": "",
	"data": {
		"taskId": 9641
	}
}
```
### 响应参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | int | 错误码。0：成功，其他值：失败|
| message | string | 错误信息|
| data | array | 返回操作的任务ID，创建结果可调用<a href="https://cloud.tencent.com/document/api/386/9356" title="查询黑石NAT网关解绑子网部分IP的任务状态">查询黑石NAT网关解绑子网部分IP的任务状态</a>查询 |

## 错误码
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| 10001 | BmVpc.InvalidParameterValue | 参数设置错误，具体错误信息可查看返回的message信息 |
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| -3030 | InvalidBmSubnet.NotFound | 无效的子网。子网资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。 |
| 13014 | BmVpcNat.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确，可通过DescribeBmNatGateway接口查询NAT网关。 |

## 实际案例
### 请求
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=UnbindIpsToBmNatGateway
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=4557
	&Timestamp=1507692902
	&Region=gz
	&vpcId=300006
	&natId=nat-et8e970y
	&ips.0.subnetId=subnet-111111
	&ips.0.ipList.0=10.11.1.14
	&ips.0.ipList.1=10.11.1.15
	&ips.1.subnetId=subnet-222222
	&ips.1.ipList.0=10.11.3.15
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