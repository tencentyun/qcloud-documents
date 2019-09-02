>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
DescribeEipBm 接口用于查询当前账号下的弹性公网 IP 列表，包括创建中/绑定中/已绑定/解绑中/未绑定/下线中等状态的弹性公网 IP，同时可以查看 EIP 的计费模式以及绑定的资源（黑石物理服务器，NAT 网关以及 VPCIP）等详细信息。

接口访问域名: bmeip.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=DescribeEipBm
	&<公共请求参数>
	&eipIds.0=<EIP实例ID>
	&eipIds.1=<EIP实例ID>
	&limit=<返回EIP数量>
	&offset=<分页偏移量>
	&unVpcId=<EIP所属VPCID>
```

### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数页面](https://cloud.tencent.com/document/product/386/6718)。其中，此接口的 Action 字段为 DescribeEipBm。


| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| eipIds.n | 否 | String | EIP 实例 ID 列表，数组下标从0开始 |
| eips.n | 否 | String | EIP 列表，数组下标从0开始 |
| unInstanceIds.n | 否 | String | 服务器实例 ID 列表，数组下标从0开始，可通过 [DescribeDevice](https://cloud.tencent.com/document/product/386/6728) 接口返回字段中的 instanceId 获取 |
| searchKey | 否 | String | EIP 实例名称，模糊匹配 |
| status.n | 否 | Int | 状态列表，数组下标从0开始<br>0：创建中； 1：绑定中；2：已绑定；3：解绑中； 4：未绑定； 6：下线中； 9：创建失败 |
| offset | 否 | Int | 偏移量，默认为0 |
| limit | 否 | Int | 返回 EIP 数量，默认20, 最大值100 |
| orderBy | 否 | String | 排序字段，支持这些字段名：eipId, eip, status, unInstanceId, arrears, createdAt |
| orderType | 否 | Int | 1倒序，0顺序，默认倒序 |
| unVpcId | 否 | String | EIP 归属的 VPC 的标识，格式形如：vpc-k7j1t2x1，可通过 [查询私有网络列表](https://cloud.tencent.com/document/product/386/6646) 返回的字段 unVpcId 获得 |
| payMode | 否 | String | 计费模式，流量计费：flow，带宽计费：bandwidth |
| 文本1 | 否 | 文本3 | 文本3 |


 >? 查询接口中单次查询一般都有一个默认最大返回记录数，要遍历所有资源，需要使用 limit，offset 进行分页查询；比如我想查询第110~149这40条记录，则可以设置 offset=110，limit=40。
 >

## 响应
### 响应示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "eipSet": []
    },
    "totalCount": 0
}
```
### 响应参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码，0：成功，其他值：失败，具体含义可以参考 [错误码](https://cloud.tencent.com/document/product/386/6725) |
| message | String | 错误信息 |
| codeDesc | String | 错误码描述 |  
|  totalCount  |  Int |  返回符合过滤条件的 EIP 数量；假如指定 limit，offset，该值有可能大于 data 数组中的数量 |
| data |   Array | 返回EIP实例列表，具体结构描述如下 |

**Data 结构**

|参数名称|类型|描述|
|---|---|---|
| data.eipSet | Array | 返回 EIP 信息数组|
| data.eipSet.eipId | String | EIP 实例 ID|
| data.eipSet.eipName | String | EIP 名称|
| data.eipSet.eip | String | EIP 地址|
| data.eipSet.ispId | Int | 运营商 ID 0：电信； 1：联通； 2：移动； 3：教育网； 4：盈科； 5：BGP； 6：中国香港|
| data.eipSet.status | Int | 状态 0：创建中； 1：绑定中； 2：已绑定； 3：解绑中； 4：未绑定； 6：下线中； 9：创建失败|
| data.eipSet.arrears | Int | 是否欠费隔离 1： 欠费隔离； 0： 正常。处在欠费隔离情况下的EIP不能进行任何管理操作。|
| data.eipSet.type | Int | EIP 所绑定的资源类型，-1：未绑定资源；0：黑石物理机，字段对应 unInstanceId；1：Nat 网关，字段对应natUid；2：云服务器 or 托管资源 IP，字段对应 vpcIp|
| data.eipSet.unInstanceId | String | EIP 所绑定的服务器实例 ID，未绑定则为空|
| data.eipSet.vpcIp | String | EIP 所绑定的云服务器 IP（托管或者云服务器的 IP），形如："10.1.1.3"。 </br>**注意：**IP资源需要通过bmvpc模块注册或者申请后才可以绑定 EIP，接口使用 [申请子网 IP](https://cloud.tencent.com/document/product/386/7337) 和 [注册子网 IP](https://cloud.tencent.com/document/product/386/7925)：未绑定则为空|
| data.eipSet.natId | Int | EIP 所绑定的 NAT 网关的数字 ID，形如：1001，未绑定则为空|
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
	&eipIds.0=eip-49kbt5n3
	&eipIds.1=eip-8n4ymhxr
	&limit=5
	&offset=5
	&unVpcId=vpc-k7j1t2x1
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
			"eipId": "eip-49kbt5n3",
			"eipName": "",
			"eip": "111.111.111.111",
			"ispId": 5,
			"status": 4,
			"arrears": 0,
			"unInstanceId": "",
			"freeAt": "2016-10-13 11:23:19",
			"createdAt": "2016-10-13 11:23:18",
			"updatedAt": "2016-10-13 11:23:19",
			"freeSecond": 3600,
			"type": null,
			"payMode": "bandwidth",
			"bandwidth": 10,
			"latestPayMode": "flow",
			"latestBandwidth": 0
		},
		{
			"eipId": "eip-8n4ymhxr",
			"eipName": "",
			"eip": "111.111.111.112",
			"ispId": 5,
			"status": 4,
			"arrears": 0,
			"unInstanceId": "",
			"freeAt": "2016-10-13 11:23:19",
			"createdAt": "2016-10-13 11:23:18",
			"updatedAt": "2016-10-13 11:23:19",
			"freeSecond": 3600,
			"type": null,
			"payMode": "bandwidth",
			"bandwidth": 10,
			"latestPayMode": "flow",
			"latestBandwidth": 0
		}]
    },
    "totalCount": 2
}

```

