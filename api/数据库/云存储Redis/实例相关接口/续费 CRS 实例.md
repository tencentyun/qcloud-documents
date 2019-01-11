## 1. 接口描述
本接口(RenewRedis)用于续费实例。
接口请求域名：<font style='color:red'>redis.api.qcloud.com </font>



## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='/doc/api/372/4153' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为RenewRedis。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| redisId | 是 | String | 实例串号,可通过[查询 Redis 实例列表接口](http://cloud.tencent.com/doc/api/260/1384)查询|
| period | 是 | UInt | 购买时长，单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 错误信息描述, 成功时，该值为空 |
| codeDesc | String | 业务侧错误码英文描述。成功时返回Success，错误时返回具体业务错误原因。 |
| data | Array |返回的订单数组|

**data数组结构：**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| data.dealId | String | 唯一订单号，通过 [DescribeRedisDealDetail](https://cloud.tencent.com/doc/api/260/5329) 可以查询订单详情 |

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|10701|InstanceNotExists|没有找到serialId对应的实例|
|11055|InstanceDeleted|实例到期已被回收|
|11056|InstanceBeenLocked|实例实例正被其它流程锁定，暂时不能执行该操作|
|11065|PeriodExceedMaxLimit|购买时长超过最大时长限制|
|11066|PeriodLessThanMinLimit|购买时长小于最小时长限制|
|100207|OperationConstraints.AccountBalanceNotEnough| 账号余额不足，请充值|

## 5. 示例
输入
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=RenewRedis
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&redisId=crs-ifmymj41
&period=1
</pre>
输出
```
{
    "code":"0",
    "message":"",
	"codeDesc": "Success",
	"data":{
		"dealId":"432586"
	}
}
```
