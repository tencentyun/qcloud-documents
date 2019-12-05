>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
DescribeEipAclBm 接口用于查询当前账号下的弹性公网 EIPACL 列表。

接口访问域名: bmeip.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=DescribeEipAclBm
	&<公共请求参数>
	&aclIds.0=<EIP实例ID>
	&aclIds.1=<EIP实例ID>
	&query.0=<字段1>
	&query.1=<字段2>
	&limit=<返回EIPACL数量>
	&offset=<分页偏移量>
```

### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数](/document/product/386/6718)。其中，此接口的 Action 字段为 DescribeEipAclBm。

|参数名称|必选|类型|描述|
|-------|-------|-------|-------|
| aclName | 否 | String | ACL 名称，支持模糊查找 |
| aclIds | 否 | Array(String) | ACL 实例 ID 列表，数组下标从 0 开始 |
| query | 否 | Array(String)| 需要查询的字段列表，支持这些字段名：aclName, status, inrule, outrule, createdAt |
| offset | 否 | Int | 分页参数。偏移量，默认为 0 |
| limit | 否 | Int | 分页参数。每一页的 EIPACL 列表数目 |


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
		"totalNum": 1,
		"eipAclList": [{
			"aclId": "bmeipacl-7mc70i3o",
			"aclName": "testAcl",
			"status": "0",
			"appId": "251000873",
			"inrule": [{
				"ip": "0.0.0.0\/0",
				"protocol": "ANY",
				"action": "drop"
			}],
			"outrule": [{
				"ip": "0.0.0.0\/0",
				"protocol": "ANY",
				"action": "drop"
			}],
			"createdAt": "2018-03-29 14:45:56",
			"eipNum": 0
		}]
	}
}
```
### 响应参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码，0：成功，其他值：失败，具体含义可以参考 [错误码](/document/product/386/6725) |
| message | String | 错误信息 |
| codeDesc | String | 错误码描述 |  
| data |   Object | EIPACL 列表，具体结构描述如 data 结构所示 |

data 结构

|参数名称|类型|描述|
|---|---|---|
| totalNum | Int | 返回 EIPACL 列表总数 |
| eipAclList| Array(Object) | 对象数组。数组元素为设备信息，具体结构描述如 eipAclList 结构所示|

eipAclList 结构

| 参数名称          | 类型     | 描述                                       |
| ------------- | ------ | ---------------------------------------- |
| aclId    | String | ACL 实例 ID                                  |
| aclName         | String    | ACL 实例名称                                |
| status      | Int    | ACL 状态。0：无状态，1：有状态                                 |
| createdAt       | String | EIPACL 创建时间                                |
| eipNum      | Int | EIPACL 已关联的 eip 数目                                 |
| inrule      | Array(Object) | 对象数组。数组的每一个元素是一条入站规则，规则的结构描述如 rule 结构所示                                 |
| outrule      | Array(Object) | 对象数组。数组的每一个元素是一条出站规则，规则的结构描述如 rule 结构所示                                 |

rule 结构

| 参数名称          | 类型     | 描述                                       |
| ------------- | ------ | ---------------------------------------- |
| ip    | String | 源 IP                                  |
| port         | String    | 目标端口                                |
| protocol         | String    | 协议(TCP/UDP/ICMP/ANY)                                |
| action         | String    | 策略（accept/drop）                                |
| description         | String    | 备注                                |


## 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9000|InnerError|内部系统错误|
|9003|ParamInvalid|请求参数不正确|


## 实际案例
 
### 输入
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=DescribeEipAclBm
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=57333
	&Timestamp=1507730884
	&Region=bj
	&aclIds.0=bmeipacl-7mc70i3o
	&Signature=umZFAAWKzjXEQp4ySgrWAoWOHKI%3D
```

### 输出
```

{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"totalNum": 1,
		"eipAclList": [{
			"aclId": "bmeipacl-7mc70i3o",
			"aclName": "testAcl",
			"status": "0",
			"appId": "251000873",
			"inrule": [{
				"ip": "0.0.0.0\/0",
				"protocol": "ANY",
				"action": "drop"
			}],
			"outrule": [{
				"ip": "0.0.0.0\/0",
				"protocol": "ANY",
				"action": "drop"
			}],
			"createdAt": "2018-03-29 14:45:56",
			"eipNum": 0
		}]
	}
}

```

