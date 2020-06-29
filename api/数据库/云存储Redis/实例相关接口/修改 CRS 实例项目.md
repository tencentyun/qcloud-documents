## 1. 接口描述 
本接口（ModifyRedisProject）用于修改 Redis 实例所属项目。
接口请求域名：`redis.api.qcloud.com`

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 <a href='https://cloud.tencent.com/document/api/239/7200' title='公共请求参数'>公共请求参数</a>。其中，此接口的 Action 字段为 ModifyRedisProject。

| 参数名称   | 是否必选 | 类型   | 描述                                                         |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| redisIds.n | 是       | String | 可通过 [DescribeRedis](http://cloud.tencent.com/doc/api/260/1384) 接口查询实例 ID 组成的数组，数组下标从0开始 |
| projectId  | 是       | UInt   | 项目ID，取值以“用户账户” > “用户账户相关接口查询” > [项目列表](https://cloud.tencent.com/doc/api/403/4400) 返回的 projectId 为准 |

## 3. 输出参数
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code <td> Int <td> 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>
<tr>
<td> message <td> String <td> 错误信息
<tr>
<td> codeDesc <td> String <td> 业务侧错误码英文描述。成功时返回 Success，错误时返回具体业务错误原因
</tbody></table>

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|11201|InvalidParameter|业务参数错误|
|10701|InstanceNotExists|没有找到 serialId 对应的实例|

## 5. 示例
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=ModifyRedisProject
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&redisIds.0=crs-ifmymj41
&projectId=1004306
</pre>

返回示例如下：
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success"
}
```
