## 1. 接口描述
本接口(SetRedisAutoRenew)用于设置自动续费。
接口请求域名：<font style='color:red'>redis.api.qcloud.com </font>


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='/doc/api/372/4153' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为SetRedisAutoRenew。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| redisIds.n  | 是 | String | 实例 ID 组成的数组，数组下标从0开始|
| isAutoRenew | 是 | UInt | 设置自动续费标识，0 - 不设置自动续费，实例到期会通知；1 - 设置自动续费，到期会自动续费；2 - 到期不续费也不通知|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 错误信息描述, 成功时，该值为空 |
| codeDesc | String | 业务侧错误码英文描述。成功时返回Success，错误时返回具体业务错误原因。 |

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|11201|InvalidParameter|业务参数错误|
|10701|InstanceNotExists|没有找到serialId对应的实例|
|11055|InstanceDeleted|实例到期已被删除|
|11061|InstanceIsolated|实例到期已被隔离|
|11060|IsAutoRenewError| 自动续费标识错误(0 - 不设置自动续费，实例到期会通知；1 - 设置自动续费，到期会自动续费；2 - 到期不续费也不通知)|

## 5. 示例
输入
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=SetRedisAutoRenew
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&redisIds.0=crs-ifmymj41
&isAutoRenew=1
</pre>
输出
```
{
    "code":"0",
    "message":"",
	"codeDesc": "Success"
}
```
