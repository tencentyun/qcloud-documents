>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
EipAclBmApply 接口用于创建黑石弹性公网 EIPACL。创建成功后，便可以绑定黑石弹性公网 IP 等相关资源。
 
接口访问域名: bmeip.api.qcloud.com
 

## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipAclBmApply
	&<公共请求参数>
	&aclName=<ACL名称>
	&status=<有状态/无状态>
```
### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数](/document/product/386/6718)。其中，此接口的 Action 字段为 EipAclBmApply。

|参数名称|必选|类型|描述|
|-------|----|---|----|
| aclName | 是 | String | ACL 名称 |
| status | 是 | Int | ACL 状态 0：无状态，1：有状态 |

 > 平台对用户每地域能申请的 EIPACL 数目是 100。

## 响应
### 响应示例
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"aclId": "bmeipacl-7mc70i3o",
		"status": 0,
		"aclName": "testAcl",
		"createdAt": "2018-03-29 14:45:56"
	}
}
```
### 响应参数

响应参数部分包含两层结构，外层展示接口的响应结果，内层展示具体的接口内容，包括申请到的 EIP 实例 ID 列表以及异步任务 ID。

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考 [错误码](/document/product/386/6725)。 |
| message |   String | 错误信息 |
| data |   Array | 返回申请的eip实例对应的异步任务信息，具体结构描述如下 |

data 结构

|参数名称|类型|描述|
|---|---|---|
| data.aclId | String | 返回申请中的 ACL 实例 ID|
| data.status | Int | 返回申请中的 ACL 实例状态|
| data.aclName | String | 返回 ACL 实例名称|
| data.createdAt | String | 返回 ACL 实例创建时间|


## 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9000|InnerError|内部系统错误|
|9003|ParamInvalid|请求参数不正确|
|40002|EipAclLimit|申请总数超过限额|



## 实际案例

### 输入

```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipBmApply
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=13716
	&Timestamp=1507781567
	&Region=bj
	&Signature=TX6qOTgRhljuPI%2BqHdfo6O%2FunlE%3D
	&aclName=testAcl
	&status=0
```

### 输出

```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"aclId": "bmeipacl-7mc70i3o",
		"status": 0,
		"aclName": "testAcl",
		"createdAt": "2018-03-29 14:45:56"
	}
}

```

