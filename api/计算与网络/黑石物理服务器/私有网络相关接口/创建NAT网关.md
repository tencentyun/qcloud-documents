## 功能描述
CreateBmNatGateway 接口用于创建黑石NAT网关，可针对全部子网、子网全部IP、子网部分IP创建NAT网关

接口请求域名：bmvpc.api.qcloud.com


## 请求
### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php/?Action=CreateBmNatGateway
    &<公共请求参数>
    &natId=<NAT网关ID>
    &natName=<NAT网关名称>
    &vpcId=<vpc网络ID>
	&maxConcurrent=<网关并发连接上限>
	&autoAllocEipNum=<分配IP的个数>
	&subnetIds.0=<子网ID>
	&subnetIds.1=<子网ID>
	&ips.0.subnetId=<子网ID>
	&ips.0.ipList.0=<子网内IP>
	&ips.0.ipList.1=<子网ID>
	&ips.1.subnetId=<子网ID>
	&ips.1.ipList.0=1<子网内IP>
```

### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为CreateBmNatGateway。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| natName | 是 | String | NAT网关名称，支持1-25个中文、英文大小写的字母、数字和下划线分隔符。 |
| vpcId | 是 | String | 私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-kd7d06of，可通过<a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。 |
| maxConcurrent | 是 | Int | 网关并发连接上限，例如：1000000、3000000、10000000。 |
| assignedEipSet.n | 否 | Array | 绑定网关的弹性IP数组, assignedEipSet和autoAllocEipNum至少传一个，例如：assignedEipSet.0=10.0.0.1 ，更多关于弹性IP的信息请参考弹性IP。|
| subnetAll | 否 | Int | 是否包含vpc下的所有子网包括后续新建子网的IP。当subnetAll为1时，subnetIds和ips的参数传入将忽略；当subnetAll为0时，需至少传入subnetIds子网或ips信息一个。|
| autoAllocEipNum | 否 | Int | 需要新申请的弹性IP个数，系统会按您的要求生产N个弹性IP, assignedEipSet和autoAllocEipNum至少传一个，更多关于弹性IP的信息请参考弹性IP。 |
| subnetIds.n | 否 | Array | 需要绑定全部IP的子网唯一ID数组, 子网Id如：subnet-k20jbhp0。可通过<a href="https://www.qcloud.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。|
| ips.n | 否 | Array | 需要绑定部分IP的子网信息数组，ips和subnetIds中的子网ID标识不能重复。ips包含字段如下：
| natName | 是 | string | NAT网关名称，支持1-25个中文、英文大小写的字母、数字和下划线分隔符。 |
| vpcId | 是 | string | 私有网络ID值，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-kd7d06of，可通过<a href="https://cloud.tencent.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询。 |
| maxConcurrent | 是 | int | 网关并发连接上限，例如：1000000、3000000、10000000。 |
| assignedEipSet.n | 否 | array | 绑定网关的弹性IP数组, assignedEipSet和autoAllocEipNum至少传一个，例如：assignedEipSet.0=10.0.0.1 ，更多关于弹性IP的信息请参考弹性IP。|
| subnetAll | 否 | int | 是否包含vpc下的所有子网包括后续新建子网的IP。当subnetAll为1时，subnetIds和ips的参数传入将忽略；当subnetAll为0时，需至少传入subnetIds子网或ips信息一个。|
| autoAllocEipNum | 否 | int | 需要新申请的弹性IP个数，系统会按您的要求生产N个弹性IP, assignedEipSet和autoAllocEipNum至少传一个，更多关于弹性IP的信息请参考弹性IP。 |
| subnetIds.n | 否 | array | 需要绑定全部IP的子网唯一ID数组, 子网Id如：subnet-k20jbhp0。可通过<a href="https://cloud.tencent.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。|
| ips.n | 否 | array | 需要绑定部分IP的子网信息数组，ips和subnetIds中的子网ID标识不能重复。ips包含字段如下：


| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|ips.n.subnetId|是|String|子网ID标识|
|ips.n.ipList|是|Array|子网下需要绑定NAT的IP列表，IP需要属于该subnetId子网|

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
| code | Int | 错误码。0：成功, 其他值：失败|
| message | String | 错误信息|
| data | Array | 返回操作的任务ID，创建结果可调用<a href="https://www.qcloud.com/document/api/386/9356" title="查询NAT网关操作状态">查询NAT网关操作状态</a>查询 |
| code | int | 错误码。0：成功, 其他值：失败|
| message | string | 错误信息|
| data | array | 返回操作的任务ID，创建结果可调用<a href="https://cloud.tencent.com/document/api/386/9356" title="查询NAT网关操作状态">查询NAT网关操作状态</a>查询 |


## 错误码

 
| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| 10001 | BmVpc.InvalidParameterValue | 参数设置错误，具体错误信息可查看返回的message信息 |
| -3047 | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>接口查询VPC。 |
| -3030 | InvalidBmSubnet.NotFound | 无效的子网。子网资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>接口查询子网。 |
| 13006 | InvalidBmVpc.NatGatewayLimitExceeded |创建的 NAT 网关数量超过上限。如果需要更多资源，请联系客服申请。每个vpc最多允许创建5个NAT网关 |
| 13010 | BmVpcNat.InvalidEip | 绑定NAT网关的弹性IP不存在。 |
| 13011 | BmVpcNat.InvalidEipVpcId | 弹性IP所属VPC与NAT网关不一致。 |
| 13012 | BmVpcNat.SubnetUsed | 子网已被绑定到其他NAT网关。 |
| 13013 | BmVpcNat.EipUsed | 绑定NAT网关的弹性IP已被使用。 |
| 13015 | BmVpcNat.EipLimitExceeded | 绑定NAT网关的弹性IP达到上限。 |


## 实际案例
### 请求
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=CreateBmNatGateway
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=4557
	&Timestamp=1507692902
	&Region=gz
	&natName=zhezhe
	&vpcId=vpc-kd7d06of
	&maxConcurrent=1000000
	&autoAllocEipNum=1
	&subnetIds.0=subnet-333333
	&subnetIds.1=subnet-444444
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