>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
BindIpsToBmNatGateway 接口用于将子网的部分IP绑定到NAT网关

接口请求域名：bmvpc.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php?Action=BindIpsToBmNatGateway
    &<公共请求参数>
    &natId=<NAT网关ID>
    &unVpcId=<vpc网络ID>
	&ips.0.unSubnetId=<子网ID>
	&ips.0.ipList.0=<子网内IP>
	&ips.0.ipList.1=<子网内IP>
	&ips.1.unSubnetId=<子网ID>
	&ips.1.ipList.0=<子网内IP>
```

### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/document/product/386/6718" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为BindIpsToBmNatGateway。

| 参数名称 | 描述 | 类型 | 必选  |
|---------|---------|---------|---------|
| natId | 黑石NAT网关统一ID，NAT网关需为IP转发方式，例如：nat-df5dfd | String | 是 | 
| unVpcId | 私有网络ID值，例如：vpc-kd7d06of，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。| String | 是 | 
| ips.n | 需要绑定部分IP的子网信息数组，ips中的子网标识subnetId不能为已经绑定的全部IP子网。| Array | 是 |

ips包含字段如下：

| 参数名称 | 描述 | 类型 | 必选  |
|---------|---------|---------|---------|
|ips.n.unSubnetId|子网ID标识|String|是|
|ips.n.ipList|子网下需要绑定NAT的IP列表，IP需要属于该unSubnetId子网|Array|是|

## 响应
### 响应示例
```
{
 "code": 0,
 "message": "",
 "data": {
  "taskId": "<NAT异步任务ID>"
 }
}
```
### 响应参数

| 参数名称 | 描述 | 类型 | 
|---------|---------|---------|
| code |错误码。0: 成功, 其他值: 失败| Int | 
| message | 错误信息| String |
| data |返回操作的任务ID，创建结果可调用<a href="/document/api/386/9356" title="查询NAT网关操作状态">查询NAT网关操作状态</a>查询 | Array | 

## 错误码 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| 10001 | BmVpc.InvalidParameterValue | 参数设置错误，具体错误信息可查看返回的message信息 |
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| -3030 | InvalidBmSubnet.NotFound | 无效的子网。子网资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。 |
| 13014 | BmVpcNat.NotFound | 无效的NAT网关，NAT网关资源不存在。请再次核实您输入的资源信息是否正确，可通过<a href="/document/product/386/9355" title="DescribeBmNatGateway">DescribeBmNatGateway</a>接口查询NAT网关。 |
| 13012 | BmVpcNat.SubnetUsed | 子网已被绑定到其他NAT网关。 |

## 实际案例
### 输入
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=BindIpsToBmNatGateway
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=4557
	&Timestamp=1507692902
	&Region=gz
	&unVpcId=300006
	&natId=nat-et8e970y
	&ips.0.unSubnetId=subnet-111111
	&ips.0.ipList.0=10.11.1.14
	&ips.0.ipList.1=10.11.1.15
	&ips.1.unSubnetId=subnet-222222
	&ips.1.ipList.0=10.11.3.15
	&Signature=4dq8JXWTyg9n8FuVckaIhg8Pnbw%3D
```

### 输出
```
{
	"code": 0,
	"message": "",
	"data": {
		"taskId": 9641
	}
}
```

