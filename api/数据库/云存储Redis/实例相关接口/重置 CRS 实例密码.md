## 1. 接口描述
本接口（ResetRedisPassword）用于重置 Redis 实例密码。
接口请求域名：`redis.api.qcloud.com`

密码规则： 长度为8-16个字符；至少包含字母、数字和字符（`!@#%^()`）中的两种。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 <a href='https://cloud.tencent.com/document/product/213/6976' title='公共请求参数'>公共请求参数</a> 页面。其中，此接口的 Action 字段为 ResetRedisPassword。

| 参数名称 | 是否必选  | 类型 | 描述 |
|:---------|---------|---------|---------|
| redisId | 是 | String | 待操作的实例 ID，可通过 [DescribeRedis](/document/product/239/1384) 接口返回值中的 redisId 获取。|
| password | 是 | String | 实例新密码，密码规则： 长度为8-16个字符；至少包含字母、数字和字符（`!@#%^()`）中的两种 |

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>|
| message | String | 错误信息描述，成功时，该值为空 |
| codeDesc | String | 业务侧错误码英文描述。成功时返回 Success，错误时返回具体业务错误原因 |
| data | Object | 任务 ID |

其中，data 表示任务 ID，其参数构成如下：

| 参数名称 | 类型 | 描述 |
|:---------|---------|---------|
| data.requestId | 任务ID | 任务ID，可通过 [DescribeTaskInfo](/document/product/239/1387) 接口查询任务执行状态


## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|11201|InvalidParameter|业务参数错误|
|10701|InstanceNotExists|没有找到 serialId 对应的实例|
|10707|InstanceLockedError|实例已被锁住，暂时不能执行该操作|
|10702|InstanceStatusAbnormal|实例状态异常,暂时不能执行该操作（例如，流程中，已隔离，已删除）|
|11058|PasswordRuleError|密码规则错误，密码必须是8-16位字符，且至少包含字母、数字和字符（`!@#%^*()`）中的两种|

## 5. 示例
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=ResetRedisPassword
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&redisId=crs-izbob1wh
&password=12D3E@!r5ed
</pre>
返回示例如下：
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"requestId": 375073
	}
}
```
