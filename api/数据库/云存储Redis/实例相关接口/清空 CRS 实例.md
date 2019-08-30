## 1. 接口描述
 
本接口（ClearRedis）用于清空 Redis 实例。
接口请求域名：`redis.api.qcloud.com`

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='https://cloud.tencent.com/document/api/239/7200' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为ClearRedis。

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>是否必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> redisId <td> 是 <td> String <td> 实例 ID
<tr>
<td> password <td> 是 <td> String <td> 实例密码
</tbody></table>

 

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a> |
| message| String |错误信息 |
| codeDesc | String | 业务侧错误码英文描述。成功时返回Success，错误时返回具体业务错误原因 |
| data | Array | 返回的数组|

**data数组结构：**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| data.requestId | Int | 任务 ID，可通过 [DescribeTaskInfo](/doc/api/260/1387) 查询 任务执行结果 |

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|11201|InvalidParameter|业务参数错误|
|10701|InstanceNotExists|没有找到 serialId 对应的实例|
|10707|InstanceLockedError|实例已被锁住，暂时不能执行该操作|
|10702|InstanceStatusAbnormal|实例状态异常,暂时不能执行该操作（例如，流程中或已隔离或已删除）|
|10501|PasswordEmpty| 密码为空|
|10712|PasswordError| 密码错误|


## 5. 示例
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=ClearRedis
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&redisId=crs-ifmymj41
&password=49A2d!e@f12e
</pre>
返回示例如下：
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"requestId": 11965
	}
}
```
