
## 接口描述
LookupEvents 用于对操作日志进行检索，便于用户进行查询相关的操作信息。
接口访问域名：`cloudaudit.api.qcloud.com`


## 请求参数
以下请求参数列表仅列出了接口请求参数。

|参数名称|必选|类型|描述|
|---------|---------|---------|--------|
|EndTime| 是 |DateTime|结束时间|
|LookupAttributes|是|Array|属性数组，目前仅支持一个元素，不填默认返回前10条数据|
|MaxResults|否|Number|日志返回的条数，不填默认返回10条，最多支持50条|
|NextToken|否|String|加载更多日志的时候使用|
|StartTime|是|DateTime|开始时间|

其中 LookupAttributes 的参数如下：

|参数名称|必选|类型|描述|
|---------|---------|---------|--------|
|AttributeKey|否|	String |搜索类型（枚举值），包括 Username：用户名，EventName：事件名称，ResourceType：资源类型，ResourceName：资源名称，EventSource：事件源，EventId：事件 ID|
|AttributeValue|否|	String	| Value 值|


## 响应参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| Events | Array | 事件数组 |
| NextToken| String | 加载更多时使用|

其中 Events 数组的参数如下：


| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| CloudAuditEvent | String | 事件字符串 |
| EventId | String |事件 ID|
|EventName|String|事件名称|
|EventSource|String|事件源|
|EventTime|String|事件时间|
|SecretId|String|访问密钥|
|EventRegion|String|区域|
|ErrorCode|Number|错误码。0 代表正常，其他代表错误|
|RequestID|String|请求 ID|
|SourceIPAddress|String|源 IP 地址|
|Resources|Object|资源|
|Username|String|用户名。主账号为：root，子账号为：子账号 ID，角色用户为：roleUser|

其中 Resources 的参数如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| ResourceName | String | 资源名称 |
| ResourceType | String |资源类型|



## 实际案例
### 请求

```
{
	"EndTime": "Number",
	"LookupAttributes": [{
		"AttributeKey": "String",
		"AttributeValue": "String"
	}],
	"MaxResults": "Number",
	"NextToken": "String",
	"StartTime": "Number"
}
```
### 响应

```
{
	"Events": [{
		"CloudAuditEvent": "String",
		"EventId": "String",
		"EventName": "String",
		"EventSource": "String",
		"EventTime": "String",
		"SecretId": "String",
		"EventRegion": "String",
		"ErrorCode": "Number",
		"EventTime": "String",
		"RequestID": "String",
		"SourceIPAddress": "String",
		"Resources": [{
			"ResourceName": "String",
			"ResourceType": "String"
		}],
		"Username": "String"
	}],
	"NextToken": "String"
}
```
