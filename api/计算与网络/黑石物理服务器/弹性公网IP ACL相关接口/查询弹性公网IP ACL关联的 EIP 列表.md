>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
DescribeEipBm 接口用于查询 ACL 关联的 EIP 列表。

接口访问域名: bmeip.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=DescribeEipBm
	&<公共请求参数>
	&aclId=<EIP实例ID>
	&limit=<返回EIP数量>
	&offset=<分页偏移量>
```

### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数](https://cloud.tencent.com/document/product/386/6718)。其中，此接口的 Action 字段为 DescribeEipBm。

|参数名称|必选|类型|描述|
|-------|-------|-------|-------|
| aclId | 是 | String | ACL 实例 Id |
| offset | 否 | Int | 分页参数。偏移量，默认为 0 |
| limit | 否 | Int | 分页参数。每一页的列表数目 |


>? 查询接口中单次查询一般都有一个默认最大返回记录数，要遍历所有资源，需要使用 limit，offset 进行分页查询；例如我想查询第110~149这40条记录，则可以设置 offset=110，limit=40。
>
 
## 响应
### 响应示例
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"eipSet": [{
			"eipId": "eip-gzmpnudq",
			"eipName": "TMI-EIP-ACL",
			"eip": "139.199.40.58",
			"ispId": 5,
			"status": 2,
			"arrears": 0,
			"unInstanceId": "tcpm-74lqozk0",
			"instanceAlias": "TMI-EIP-ACL-58",
			"freeAt": "2018-03-21 16:59:01",
			"createdAt": "2018-03-13 20:59:14",
			"updatedAt": "2018-03-29 14:49:46",
			"freeSecond": 0,
			"type": 0,
			"payMode": "bandwidth",
			"bandwidth": 1,
			"latestPayMode": "flow",
			"latestBandwidth": 0,
			"vpcId": 202217,
			"vpcName": "normal-202217",
			"natId": null,
			"natUid": null,
			"vpcIp": null,
			"unVpcId": "vpc-4vk5e4bu",
			"exclusive": 0,
			"vpcCidr": "10.123.0.0\/16",
			"aclId": "bmeipacl-2oy40kkm",
			"aclName": "testname"
		}]
	},
	"totalCount": 1
}
```
### 响应参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码，0：成功，其他值：失败，具体含义可以参考 [错误码](https://cloud.tencent.com/document/product/386/6725) |
| message | String | 错误信息 |
| codeDesc | String | 错误码描述 |  
|  totalCount  |  Int |  返回符合过滤条件的 EIP 数量；假如指定 limit，offset，该值有可能大于 data 数组中的数量 |
| data |   Array | 返回 EIP 实例列表，具体结构描述如下 |

**Data 结构**

|参数名称|类型|描述|
|---|---|---|
| data.eipSet | Array | 返回 EIP 信息数组|
| data.eipSet.eipId | String | EIP 实例 ID|
| data.eipSet.eipName | String | EIP 名称|
| data.eipSet.eip | String | EIP 地址|
| data.eipSet.ispId | Int | 运营商 ID 0：电信； 1：联通； 2：移动； 3：教育网； 4：盈科； 5：BGP； 6：中国香港|
| data.eipSet.status | Int | 状态 0：创建中； 1：绑定中； 2：已绑定； 3：解绑中； 4：未绑定； 6：下线中； 9：创建失败|
| data.eipSet.arrears | Int | 是否欠费隔离 1： 欠费隔离； 0： 正常。处在欠费隔离情况下的 EIP 不能进行任何管理操作。|
| data.eipSet.type | Int | EIP 所绑定的资源类型，-1：未绑定资源；0：黑石物理机，字段对应 unInstanceId；1：Nat 网关，字段对应 natUid；2：云服务器or托管资源IP，字段对应vpcIp|
| data.eipSet.unInstanceId | String | EIP 所绑定的服务器实例 ID，未绑定则为空|
| data.eipSet.vpcIp | String | EIP 所绑定的云服务器 IP(托管或者云服务器的 IP），形如："10.1.1.3"。 </br>注意：IP 资源需要通过 bmvpc 模块注册或者申请后才可以绑定 eip，接口使用 [申请子网 IP](https://cloud.tencent.com/document/product/386/7337) 和 [注册子网 IP](https://cloud.tencent.com/document/product/386/7925)：,未绑定则为空|
| data.eipSet.natId | Int | EIP 所绑定的 NAT 网关的数字 ID，形如：1001,，未绑定则为空|
| data.eipSet.natUid | String | EIP 所绑定的 NAT 网关实例 ID，形如："nat-n47xxxxx"，未绑定则为空|
| data.eipSet.freeAt | String | EIP 解绑时间|
| data.eipSet.createdAt | String | EIP 创建时间|
| data.eipSet.updatedAt | String | EIP 更新时间|
| data.eipSet.freeSecond | Int | EIP 未绑定服务器时长（单位：秒）|
| data.eipSet.payMode | String | EIP 计费模式，"flow"：流量计费； "bandwidth"：带宽计费|
| data.eipSet.bandwidth | Int | EIP 带宽计费模式下的带宽上限（单位：MB）|
| data.eipSet.latestPayMode | String | 最近一次操作变更的 EIP 计费模式，"flow"：流量计费； "bandwidth"：带宽计费 |
| data.eipSet.latestBandwidth | Int | 最近一次操作变更的 EIP 计费模式对应的带宽上限值，仅在带宽计费模式下有效（单位：MB）|

## 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|


## 实际案例
 
### 输入
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=DescribeEipBm
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=57333
	&Timestamp=1507730884
	&Region=bj
	&aclId=bmeipacl-2oy40kkm
	&Signature=umZFAAWKzjXEQp4ySgrWAoWOHKI%3D
```

### 输出
```

{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"eipSet": [{
			"eipId": "eip-gzmpnudq",
			"eipName": "TMI-EIP-ACL",
			"eip": "139.199.40.58",
			"ispId": 5,
			"status": 2,
			"arrears": 0,
			"unInstanceId": "tcpm-74lqozk0",
			"instanceAlias": "TMI-EIP-ACL-58",
			"freeAt": "2018-03-21 16:59:01",
			"createdAt": "2018-03-13 20:59:14",
			"updatedAt": "2018-03-29 14:49:46",
			"freeSecond": 0,
			"type": 0,
			"payMode": "bandwidth",
			"bandwidth": 1,
			"latestPayMode": "flow",
			"latestBandwidth": 0,
			"vpcId": 202217,
			"vpcName": "normal-202217",
			"natId": null,
			"natUid": null,
			"vpcIp": null,
			"unVpcId": "vpc-4vk5e4bu",
			"exclusive": 0,
			"vpcCidr": "10.123.0.0\/16",
			"aclId": "bmeipacl-2oy40kkm",
			"aclName": "testname"
		}]
	},
	"totalCount": 1
}

```

