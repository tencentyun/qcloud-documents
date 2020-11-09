## 1. 接口描述

本接口(DescribeAddressGroupInstances)用于查询IP地址组关联的云资源。
接口请求域名：vpc.api.qcloud.com。

- 查询时指定 IP 地址组 ID。
- 查询结果包括关联的安全组等云资源。

## 2. 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 <a href="https://cloud.tencent.com/document/api/215/4772" title="公共请求参数">公共请求参数</a> 页面。其中，此接口的 Action 字段为 DescribeAddressGroupInstances。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| addressGroupId | 是 | String | IP 地址组 ID 。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 数字错误码, 0 表示查询调用成功，其他值表示失败。详见错误码页面的 <a href='https://cloud.tencent.com/document/api/215/4781' title='公共错误码'>公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| codeDesc | String | 字符串错误码。 |
| data | Object | 返回信息。 |
| data.taskId | Int | 请求任务 ID，由具体的异步操作接口提供，例如 15454。 | 

## 4. 任务查询输出参数
通过DescribeNetTaskResult接口可以查询任务结果

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0 表示任务查询成功，其他值表示失败。详见错误码页面的 <a href='https://cloud.tencent.com/document/api/215/4781' title='公共错误码'>公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| codeDesc | String | 字符串错误码。 |
| data | Object | 返回信息。 |
| data.status | Int | 任务的当前状态。0：成功，1：失败，2：进行中。 | 
| data.output | Object| 任务执行中间状况详情。任务的最终成败以 data.status 为准。|
| data.data | Object/Array | 仅用于任务为查询类任务时的结果数据或中间结果数据。| 

data.output 结构

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|code | Int | 数字错误码。|
|message | String | 结果描述。|

data.data 结构

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| total  | Int  |  云资源个数 |
| detail  | Array  |  云资源详情。 |
| detail.n.region  | String  |  云资源地域。 |
| detail.n.type  | String  |  云资源类型。|
| detail.n.id  | String  |  云资源 ID。|
| detail.n.name  | String  |  云资源名称。 |

## 5. 错误码表
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见 <a href="https://cloud.tencent.com/doc/api/245/4781" title="公共错误码">公共错误码</a>。


 <table class="t"><tbody><tr>
<th><b>错误码数值</b></th>
<th><b>原因</b></th>
<tr>
<td> 29257 <td> 后台错误，请求失败。
<tr>
<td> 29258 <td> 引用资源不存在。
<tr>
<td> 29259 <td> 关联对象因规则展开过大拒绝您的关联。
<tr>
<td> 29260 <td> 参数模板总数或成员数使用超限。
<tr>
<td> 29254 <td> 鉴权失败。
<tr>
<td> 9003 <td> 参数错误。
<tr>
<td> 9005 <td> 系统忙或有相关资源正在被编辑。
</tbody></table>

## 6. 示例
	执行一个参数模板的异步调用，然后使用 DescribeNetTaskResult 查询结果。
例如查询一个参数模板是否被云资源引用：
### 步骤1

输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeAddressGroupInstances
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&addressGroupId=ipmg-i0836656
</pre>
输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "taskId": 297
    }
}
```

### 步骤2
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeNetTaskResult
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&taskId=297
</pre>
输出
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"status": 0,
		"output": {
			"code": 0,
			"message": "OK"
		},
		"data": {
			"total": 4,
			"detail": [{
					"region": "ca",
					"type": "sg",
					"id": "sg-b2qce888",
					"name": "北美"
				},
				{
					"region": "gz",
					"type": "sg",
					"id": "sg-5y2ta666",
					"name": "createPolicy"
				},
				{
					"region": "sh",
					"type": "sg",
					"id": "sg-gt6an666",
					"name": "上海安全组"
				},
				{
					"region": "gz",
					"type": "sg",
					"id": "sg-jn3hnxyj",
					"name": "广州安全组"
				}
			]
		}
	}
}
```

 
