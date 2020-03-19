>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
CreateBmNatGateway 接口用于创建黑石NAT网关，可针对CIDR方式、子网全部IP、子网部分IP创建NAT网关

接口请求域名：bmvpc.api.qcloud.com


## 请求
### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php/?Action=CreateBmNatGateway
    &<公共请求参数>
    &natName=<NAT网关名称>
    &unVpcId=<vpc网络ID>
	&maxConcurrent=<网关并发连接上限>
	&autoAllocEipNum=<分配IP的个数>
	&unSubnetIds.0=<子网ID>
	&unSubnetIds.1=<子网ID>
	&forwardMode=<转发方式>
	&ips.0.unSubnetId=<子网ID>
	&ips.0.ipList.0=<子网内IP>
	&ips.0.ipList.1=<子网ID>
	&ips.1.unSubnetId=<子网ID>
	&ips.1.ipList.0=1<子网内IP>
```

### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/document/product/386/6718" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为CreateBmNatGateway。

| 参数名称 | 描述 | 类型 | 必选  |
|---------|---------|---------|---------|
| natName | NAT网关名称，支持1-25个中文、英文大小写的字母、数字和下划线分隔符。 | String | 是 |
| unVpcId |  私有网络ID值，例如：vpc-kd7d06of，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。 | String | 是 |
| maxConcurrent | 网关并发连接上限，例如：1000000、3000000、10000000。 | Int |  是 |
| exclusive |取值为0，1；0和1分别表示创建共享型NAT网关和独占NAT型网关；由于同一个VPC网络内，指向NAT集群的默认路由只有一条，因此VPC内只能创建一种类型NAT网关；创建独占型NAT网关时，需联系对应架构师进行独占NAT集群搭建，否则无法创建独占型NAT网关。| Int | 否 |  
| autoAllocEipNum | 需要新申请的弹性IP个数，系统会按您的要求生产N个弹性IP, assignedEipSet和autoAllocEipNum至少传一个，更多关于弹性IP的信息请参考弹性IP。 | Int |  否 | 
| assignedEipSet.n |绑定网关的弹性IP数组, assignedEipSet和autoAllocEipNum至少传一个，例如：assignedEipSet.0=10.0.0.1 ，更多关于弹性IP的信息请参考弹性IP。当exclusive为0时，assignedEipSet集合中的eip为共享类型EIP，当exclusive为1时，assignedEipSet集合中的eip为独占类型EIP。| Array | 否 | 
| forwardMode | NAT网关的转发方式。当值为0表示ip方式，值为1时表示cidr方式；cidr方式目前支持网段位数不小于24位的子网，通过cidr方式可支持更多的IP接入到NAT网关| Int | 是 | 
| unSubnetIds.n | 需要绑定全部IP的子网唯一ID数组, 子网Id如：subnet-k20jbhp0。可通过<a href="/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。| Array | 否 | 
| ips.n | 需要绑定部分IP的子网信息数组，ips和unSubnetIds中的子网ID标识不能重复。| Array | 否 | 

ips包含字段如下：

| 参数名称 |  描述 |类型 | 必选  |
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
| code | 错误码。0：成功, 其他值：失败| Int |
| message | 错误信息| String |
| data |返回操作的任务ID，创建结果可调用<a href="/document/api/386/9356" title="查询NAT网关操作状态">查询NAT网关操作状态</a>查询 | Array | 


## 错误码

 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| 10001 | BmVpc.InvalidParameterValue | 参数设置错误，具体错误信息可查看返回的message信息 |
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| -3030 | InvalidBmSubnet.NotFound | 无效的子网。子网资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。 |
| 13006 | InvalidBmVpc.NatGatewayLimitExceeded |创建的 NAT 网关数量超过上限。如果需要更多资源，请联系客服申请。每个vpc最多允许创建5个NAT网关 |
| 13010 | BmVpcNat.InvalidEip | 绑定NAT网关的弹性IP不存在。 |
| 13011 | BmVpcNat.InvalidEipVpcId | 弹性IP所属VPC与NAT网关不一致。 |
| 13012 | BmVpcNat.SubnetUsed | 子网已被绑定到其他NAT网关。 |
| 13013 | BmVpcNat.EipUsed | 绑定NAT网关的弹性IP已被使用。 |
| 13015 | BmVpcNat.EipLimitExceeded | 绑定NAT网关的弹性IP达到上限。 |


## 实际案例
### 输入
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=CreateBmNatGateway
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=4557
	&Timestamp=1507692902
	&Region=gz
	&natName=zhezhe
	&unVpcId=vpc-kd7d06of
	&maxConcurrent=1000000
	&autoAllocEipNum=1
	&forwardMode=1
	&unSubnetIds.0=subnet-333333
	&unSubnetIds.1=subnet-444444
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
