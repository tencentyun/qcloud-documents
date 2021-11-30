## 1. 接口描述
本接口(UpgradeRedisInquiryPrice)用于查询升级实例价格。
接口请求域名：<font style='color:red'>redis.api.qcloud.com </font>



## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='https://cloud.tencent.com/document/api/239/7200' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为UpgradeRedisInquiryPrice。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| redisId | 是 | String | 实例串号|
| memSize | 是 | UInt | 升级后的容量，1024的整数倍，单位：MB。升级后容量必须大于当前实例容量，大小限制以[查询可售卖规格](http://cloud.tencent.com/doc/api/260/4974) 为准|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 错误信息描述, 成功时，该值为空 |
| codeDesc | String | 业务侧错误码英文描述。成功时返回Success，错误时返回具体业务错误原因。 |
| data | Array | 返回的费用数组 |

**data数组结构：**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| data.price | Int | 升级总费用，单位：分 | 

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|10701|InstanceNotExists|没有找到serialId对应的实例|
|10703|InvalidMemSize|请求的容量不在售卖规格中（memSize应为1024的整数倍，单位：MB）|
|11063|MemSizeNotInRange|请求的容量不在售卖容量范围内（请用[查询售卖规格](http://cloud.tencent.com/doc/api/260/4974)接口查询售卖容量限制）|
|10702|InstanceStatusAbnormal|实例状态异常,暂时不能执行该操作（例如，流程中或已隔离或已删除）|
|11057|ReduceCapacityNotAllowed| 请求容量小于实例实际容量，暂不支持缩容|

## 5. 示例
输入
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=UpgradeRedisInquiryPrice
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&redisId=crs-ifmymj41
&memSize=2048
</pre>
输出
```
{
    "code":"0",
    "message":"",
	"codeDesc": "Success",
    "data":{
        "price": 24460
    }
}
```
